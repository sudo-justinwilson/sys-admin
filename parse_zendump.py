# this is to parse a zenoss export csv file:
def parse_zendump(file_in, file_out):
    """
    This takes a zendump from a Zenoss instance, and parses it for device names, and IP addresses.
    """
    # create empty lists to store the values in:
    ip_list = []
    devices = []
    
    
    # the data is quite nested, and I am only interested in the device name and IP address:
    for item in [element for element in [line.split(',') for line in open(zen_file).readlines()] if len(element) > 1]: 
        ip_list +=      [field.split('=')[1].replace("'", "") for field in item if 'ManageIp' in field]
        devices +=      [field.split('=')[1].replace("'", "").rstrip('.barangaroo.com.au') for field in item if 'setTitle' in field]
    
    # create a dict out of the device names and IP addresses:
    devices_dict = dict(zip(tmp_devices, ip_tmp)) 
    
    # write the dict to file_out:
    with open(file_out, 'w') as output:
        for k, v in devices_list.viewitems():
            output.write(k + " : " + v + "\n")

