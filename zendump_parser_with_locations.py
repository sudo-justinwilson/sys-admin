import jinja2

class ParseZenDump:
    """
    An object to manipulate and parse zendump csv files.
    """

    class Device:
        """
        Abstract a device.
        """
        def __init__(self, title, ip):
            self.title = title
            self.ip = ip

    def __init__(self, path_to_zendump):
        """
        Create a ParseZenDump instance.

        path_to_zendump =  a string which is the path to the zendump csv file
        """
        self.file = path_to_zendump


    def parse_zendump(self, zendump_file=None):
        """
        Parse the values from a Zennos dump csv file.
    
        dump_file =     the name of the zendump file
        fields =        an iterable, containing strings for the fields in the zendump file that you want to be parsed
        """
        if zendump_file == None:
            zendump_file = self.file

        # create an empty list to store devices
        device_list = []
    
        for line in open(zendump_file).readlines():
            # define attributes:
            ip = ''
            title = ''
            
            for field in line.split():
                if 'setManageIp' in field:
                    ip = field.split('=')[-1].lstrip("'").rstrip("',")
                if 'setTitle' in field:
                    title = field.split('=')[-1].lstrip("'").rstrip("',\"").rstrip(".ICN.barangaroo.com.au")
                if len(ip) > 0 and len(title) > 0:
                    device = ParseZenDump.Device(title, ip)
                    device_list.append(device)
        
        return device_list

    def device_dict(self):
        """
        Return a dict that contains the device titles as the keys, and the IP addresses as the values.
        """
        # create a device_list
        device_list = self.parse_zendump()
        device_dict = {}
        for item in device_list:
            device_dict[item.title] = item.ip
        return device_dict

    def parse_to_etc_hosts(self):
        """
        Parse a device_dict to an /etc/hosts file.
        """
        # create a device_dict:
        dd = self.device_dict()
        hosts_template = """{% for device in devices %}\
        {{ device[1] }}\t\t {{ device[0] }}
        {% endfor %}"""
        template = jinja2.Template(hosts_template)
        return template.render(devices = dd.iteritems())

    def parse_to_ansible_hosts(self):
        """
        Parse a device_dict to Ansible inventory format.
        """
        dd = self.device_dict()
        ansible_template = """{% for device in devices %}
[{{ device[0] }}]
{{ device[0] }} ansible_host={{ device[1] }}
{% endfor %}"""
        template = jinja2.Template(ansible_template)
        return template.render(devices=dd.iteritems())

    def group_devices(self, string):
        """
        Filter devices beginning with string.
        """
        devices = self.device_dict()
        group = {}
        for device in devices.iterkeys():
            if device.startswith(string):
                group[device] = devices[device]
        return group
        

if __name__ == '__main__':
    f = '../scrapbook/zenbatchdump_2017-01-17.csv'
    parser = ParseZenDump(f)
    #dl = parser.parse_zendump()
    #for item in dl:
    #    print item
    #print [item.title for item in dl]
    #dd = parser.device_dict()
    #for item in dd.viewitems():
    #    print(item)
    group = parser.group_devices('BC3')
    print(group)
