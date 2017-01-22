#import argparse
#
#parser = argparse.ArgumentParser()
#parser.add_argument("one", help="This is the first arg.")
#parser.add_argument("--two", help="This is the second arg.")
#
#args = parser.parse_args()
#
#print(args.one)
#if args.two:
#    print(args.two)
#
#
import argparse
from netmiko import ConnectHandler

class DeviceParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("ip", help="the IP address of the remote cisco device.")
        parser.add_argument("--device_type", help="the device type of the remote device (cisco by default).")
        parser.add_argument("--username", help="the username to login with.")
        parser.add_argument("--password", help="the password to login with.")

        args = parser.parse_args()

        self.ip = args.ip
        if args.device_type:
            self.device_type = args.device_type
        else:
            self.device_type = 'cisco_ios'

        if args.username:
            self.device_type = args.username
        else:
            self.username = 'justin'

        if args.password:
            self.device_type = args.password
        else:
            self.password = 'cisco'

        self.args = {
            'device_type' : self.device_type,
            'ip' : self.ip,
            'username' : self.username,
            'password' : self.password,
            }

    def net_connect(self):
        """
        establish a netmiko connection to remote device.
        """
        connection = ConnectHandler(**self.args)
        if connection.find_prompt():
            return connection
        else:
            raise Exception('could not connect')


    def get_ip(self):
        print(self.ip)

class CiscoDevices:
    """
    Class containing methods for executing commands on remote cisco devices, with netmiko as the transport.
    """
    def __init__(self, ip, device_type=None, username=None, password=None):
        """
        Initialize a cisco_devices instance.

        Accepts the following args:

            ip          -           (mandatory) the IP address of the remote cisco device.
            device_type -           (optional) will use cisco by default.
            username    -           (optional) will use default username.
            password    -           (optional) will use default password.
        """
        self.ip = ip
        if device_type != None:
            self.device_type = device_type
        else:
            self.device_type = 'cisco_ios'
        if username != None:
            self.username = username
        else:
            self.username = 'justin'
        if password != None:
            self.password = password
        else:
            self.password = 'cisco'
        self.args = {
            'device_type' : self.device_type,
            'ip' : self.ip,
            'username' : self.username,
            'password' : self.password,
            }

    def net_connect(self):
        """
        establish a netmiko connection to remote device.
        """
        connection = ConnectHandler(**self.args)
        if connection.find_prompt():
            return connection
        else:
            raise Exception('could not connect')

####

if __name__ == '__main__':
#    nme = CiscoDevices('10.0.1.1')
#    connection = nme.net_connect()
#    print(connection.base_prompt)
#    connection.disconnect()
#    d = DeviceParser() 
#    d.get_ip()
#    print(d.device_type)
#    print(d.username)
#    print(d.password)
#
#    nme = CiscoDevices('10.0.1.1')
#    connection = nme.net_connect()
#    print(connection.base_prompt)
#    connection.disconnect()
#
    device = DeviceParser()
    connection = device.net_connect()
    print(connection.base_prompt)
    
