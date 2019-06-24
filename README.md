# Veracross API Python Library
Provides an easy way to pull information from the Veracross API in Python.

Rate limiting and pagination will be handled automatically.

Usage Example:
```python
import veracross_api as v

c = {'school_short_name': 'abc',
        'vcuser': 'username',
        'vcpass': 'password'
}

# Create a new object with library
vc = v.Veracross(c)

# Follow the guidelines specified here: https://api.veracross.com/docs
# Specify the endpoint documented in the api or just one record from that target.
# Examples of endpoint are: facstaff, students, classes, courses, course_schedules, enrollments, etc.
# To return one record from that target, just specify the id number.
# Additional parameters are passed using a dictionary.

# Return all faculty and staff
data = vc.pull("facstaff")
print(data)

# Return one faculty and staff member by id
data = vc.pull("facstaff/99999")
print(data)

# Pass url parameters in a dictionary to the pull method.
# Return all faculty staff updated after 2019-01-01
param = {"updated_after": "2019-01-01"}
data = vc.pull("facstaff", parameters=param)
print(data)

# Return the amount of requests left in rate limiting
vc.rate_limit_remaining

# Return the amount of time left before the limit is reset
vc.rate_limit_reset

```

All data will be returned as a dictionary.

