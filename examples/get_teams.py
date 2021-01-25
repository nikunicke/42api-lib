#Note that you can import already created instance of IntraAPIClient from intra.py
from intra import ic
from config import campus_id

import json


#Instead of writing everything in .get, you can create a payload
payload = {
    'filter[primary_campus_id]':campus_id
}

#You can shorten the url if you have properly configured your config.yml
response = ic.get("teams", params = payload)
data = response.json()

for user in data:
    print(f"{user}")