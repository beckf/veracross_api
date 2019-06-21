"""
Veracross API Class

This class provides an easy interface to the Veracross API for python.

Rate limiting and pagination will be handled automatically.

Example of usage:

c = {'school_short_name': 'abc',
        'vcuser': 'username',
        'vcpass': 'password'
}

import veracross_api as v
vc = Veracross(c)
data = vc.pull("facstaff")
print(data)
data = vc.pull("facstaff/99999")
print(data)
param = {"updated_after": "2019-01-01"}
data = vc.pull("facstaff", parameters=param)
print(data)

Returned will be a dictionary of data.
"""


import requests
import math
import time
from urllib import parse

__author__ = "Forrest Beck"


class Veracross(object):

    def __init__(self, config):
        self.rate_limit_remaining = 300
        self.rate_limit_reset = 0
        self.session = requests.Session()
        self.config = config

        if 'school_short_name' in config:
            self.api_url = 'https://api.veracross.com/{}/v2/'.format(str(config['school_short_name']))

        if 'vcurl' in config:
            self.api_url = config['vcurl']

    def __repr__(self):
        return "VC API connected to " + str(self.api_url) + " as " + str(self.config["vcuser"])

    def set_timers(self, limit_remaining, limit_reset):
        """
        Sets the rate limits
        :param limit_remaining: Count of API calls remaining from header X-Rate-Limit-Remaining
        :param limit_reset: Reset Timer from header X-Rate-Limit-Reset
        :return: None
        """
        self.rate_limit_remaining = int(limit_remaining)
        self.rate_limit_reset = int(limit_reset)
        if self.rate_limit_remaining == 1:
            time.sleep(self.rate_limit_reset + 1)

    def set_auth(self):
        """
        Ensures auth header is in place.
        :return: None
        """
        if not self.session.auth:
            self.session.auth = (self.config['vcuser'], self.config['vcpass'])

    def pull(self, source, parameters=None):
        """
        Get Veracross Data with pagination
        :param source: VC Source (households, facstaff, facstaff/99)
        :param parameters: Optional API parameters normally in GET request
        :return: records in a list of dictionaries
        """
        try:
            self.set_auth()

            if parameters is not None:
                s = self.api_url + source + ".json?" + parse.urlencode(parameters, safe=':-')
            else:
                s = self.api_url + source + ".json"

            r = self.session.get(s)

            if r.status_code == 200:
                if 'X-Total-Count' in r.headers:
                    pages = math.ceil(int(r.headers['X-Total-Count']) / 100)
                else:
                    self.set_timers(r.headers['X-Rate-Limit-Remaining'],
                                    r.headers['X-Rate-Limit-Reset'])
                    return r.json()

                page = 1
                records = []

                while page <= pages:
                    self.set_timers(r.headers['X-Rate-Limit-Remaining'],
                                    r.headers['X-Rate-Limit-Reset'])
                    if parameters is None:
                        r = self.session.get(s + "?page=" + str(page))
                    else:
                        r = self.session.get(s + "&page=" + str(page))

                    records += r.json()
                    page += 1
                return records
            else:
                return None
        except:
            return None
