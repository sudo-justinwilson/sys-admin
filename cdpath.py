import cdplinkedlist

"""
This is to get the hostname and IP address of the CDP neighbourse.
"""

count = 0
d = {}
cdpath = cdplinkedlist.LinkedQueue()

for i in range(len(c)):
  if 'Device ID' in c[i]:
    d['device_id'] = c[i].split(':')[1].lstrip()
  if 'IP address' in c[i]:
    d['ip_address'] = c[i].split(':')[1].lstrip()
  if 'Interface:' in c[i]:
    d['local_port'] = c[i].split(',')[0].split(':')[1].lstrip()
    d['remote_port'] = c[i].split(',')[1].split(':')[1].lstrip()
    cdpath.enqueue(d)
    d = {}
