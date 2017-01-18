import xmltodict, requests

"""
This script uses the Cisco Prime (3.0) API to query for a monitored devices details.
"""

# set credentials and url for Cisco Prime:
username = 'login_name'
password = 'your_password'
# set this to IP address or DNS name of the Prime instance:
prime_address = 'prime.example.com'
# I use this script for monitoring wifi access points, so I will append 'AccessPoints' to the 
# base URL so that requests are relative to the 'AccessPoints' resource.
# (see API docs for other resource keywords in Prime):
resource = 'AccessPoints'
# create base URL for Prime API calls:
prime_url = 'https://%s:%s@%s/webacs/api/v1/data/%s' % (username, password, prime_address, resource)

# set HTTP GET params (see API docs for more info):
args = {
    '.full' : 'true',       # return full details of device
    'name' : 'name_of_devie_to_be_queried',     # this will query one device. omit for all devices
    }

# make the request and store the returned data in 'device':
device = requests.get(prime_url, params=args, verify=False)

# the response should be in xml (there should be a way to request that the response is in json.. todo), so we will parse the XML into an OrderedDict
# Note that this depends on the fields of the requested resource, so the keys will probably be different:
device_data = xmltodict.parse(device.text)['queryResponse']['entity']['accessPointsDTO']

# device_data is now essentially a dict, and values can be retieved by keys, EG:
# get the devices IP address:
device_data['ipAddress']
# and the device name:
device_data['name']
