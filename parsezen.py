def parse_zendump(zendump_file):
    """
    Parse the values from a Zennos dump csv file.

    dump_file =     the name of the zendump file
    fields =        an iterable, containing strings for the fields in the zendump file that you want to be parsed
    """

    class Device:
        # abstract a device to store device attributes
        def __init__(self, title, ip):
            self.title = title
            self.ip = ip

    # create an empty list to store devices
    device_list = []

    for line in open(zendump_file).readlines():
        # define attributes:
        ip = ''
        title = ''
        
        for field in line.split():
            if 'setManageIp' in field:
                ip = field.split('=')[-1]
            if 'setTitle' in field:
                title = field.split('=')[-1]
            if len(ip) > 0 and len(title) > 0:
                device = Device(title, ip)
                device_list.append(device)
    
    return device_list
    # the returned device_list object is a list of Device instances.
    # EG: [device.ip for device in device_list]  would return a list of the ip addresses in the device_list...
