#!/usr/bin/python

"""
This is a script to look up who the vendor is from a MAC address. it uses the website http://macvendors.com/ (it sends a POST request to http://api.macvendors.com/<MAC>	<- <MAC> == hex mac address.
	MAC addresses are fed from a file with the format:
		<MAC> <IP> <STATIC or DHCP EXPIRATION>
	adjust the script accordingly to meet your needs.
"""

import os
import sys

# replace the the target file accordingly:
MACFILE = '/home/justin/tmp/lanips-form'
WEBSITE = 'http://api.macvendors.com/'

data = open(MACFILE)

# read file into a string:
rawdata = data.read()

# split string into a list:
splitdata = rawdata.split("\n")

# split further so that each entry is it's own list:
datalist = []

for line in splitdata:
	datalist.append(line.split(","))

# lookup each vendor for each MAC:
for entry in datalist:
	mac = entry[0]
	base = WEBSITE
	url = base + mac
	template = """str(os.popen('%s %s').read())"""
	command = 'curl -s'
	poststring = template % (command, url)
	vendor = eval(poststring)
	entry.append(vendor)
	print'The Vendor for', entry[1], 'is: ', vendor	
