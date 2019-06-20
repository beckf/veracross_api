# Veracross API Python Library
Provides an easy way to pull information from the Veracross API in Python.

Rate limiting and pagination will be handled automatically.

Usage Example:
```python
import veracross_api as v

c = {'vcurl': 'https://api.veracross.com/XschoolshortnameX/v2',
        'vcuser': 'username',
        'vcpass': 'password'
        }

vc = v.Veracross(c)
data = vc.pull("facstaff")
print(data)
data = vc.pull("facstaff/99999")
print(data)
data = vc.pull("facstaff", "updated_after=2018-05-01")
print(data)
```

All data will be returned as a dictionary.

