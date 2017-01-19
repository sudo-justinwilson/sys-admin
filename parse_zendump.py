
# I used a string, but file.readlines() is a list...V
zendump = open('zendump.csv').readlines()

ip_list = []
devices = []

for item in [element for element in [line.split(',') for line in sample.splitlines()] if len(element) > 1]:
	ip_list +=      [field.split('=')[1].replace("'", "") for field in item if 'ManageIp' in field]
	devices +=      [field.split('=')[1].replace("'", "").rstrip('.barangaroo.com.au') for field in item if 'setTitle' in field]

device = dict(zip(devices, ip_list))

-----




for item in [element for element in [line.split(',') for line in open('zendump.csv').readlines().splitlines()] if len(element) > 1]:
	ip_list +=      [field.split('=')[1].replace("'", "") for field in item if 'ManageIp' in field]
	devices +=      [field.split('=')[1].replace("'", "").rstrip('.barangaroo.com.au') for field in item if 'setTitle' in field]

device = dict(zip(devices, ip_list))
