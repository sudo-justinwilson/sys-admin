from netmiko import ConnectionHandler



class BaseCiscoDevice:
    """
    This will be used as a base class for Cisco devices (switches, routers and maybe firewalls...).
    """
    
    # this is a simple nested class to abstractly define an interface:
    class Interface:
        """
        Abstract an interface. Concrete sub-classes may make this richer.
        """
        __slots__ = 'name'
        def __init__(self, name):
            """
            This will create a simple interface.
            """
            self.name = name

    def __init__(self, name, params):
        """
        Create an CiscoDevice instance.
        """
        self.name = name
        self._params = params

    def cdp_neighbours(self, args):
        """
        Returns a {linked?} list of CDP neighbours.
        """
        ssh = ConnectionHandler(**args)



    def vlan_allowed(self, trunk, vlan):
        """
        Returns True if vlan is allowed on trunk.
        """
        if vlan in self.trunk.vlans:
            return True
        else:
            return False

    def make_path(self, rep_segment, vlan):
        """
        This should be on a DS.
        """
        for trunk in self.rep_segment.interfaces:
            allow_vlan(trunk, vlan)

    def allow_vlan(self, trunk, vlan):
        """
        This allows a vlan on a trunk.
        """
        self.ssh_connection.send_config_commands([
            'interface ' + trunk,
            'switchport trunk vlan allowed add ' + vlan,
            ])
        running_config = self.ssh_connection.send_commands([
            'show run interface ' + trunk,
            ])
        flag = False
        for line in running_config.splitlines():
            if vlan in line:
                flag = True
        if flag == False:
            raise Exception('There was an error')
            break
        else:
            if flag == True:
            self.ssh_connection.send_command([
                'write'
                ])
        print('success for vlan ' + vlan + ' for interface ' + trunk)

    def interfaces(self, name=None):
        """
        Return a list of interfaces on this device.
        """
        interfaces = []
        interfaces += [word for word in self.running_config.splitlines()if re.match("[[:digit:]]", word)]
        return interfaces 
