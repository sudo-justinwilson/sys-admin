from netmiko import ConnectionHandler

class BaseCiscoDevice:
    """
    This is a base class that represents a Cisco device. It has basic behaviours that should be defined by subclasses. 
    """
    ###     start nested interface class      ###
    
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

            # end nested Interface class
    
    def __init__(self):
        """
        For subclasses to override.
        """
        pass



class CiscoSwitch(BaseCiscoDevice):
    """
    This will be used as a base class for Cisco switches.
    """
    ###     start nested interface class      ###
    
    # this is a simple nested class to abstractly define an interface:
    class Interface:
        """
        Abstract an interface. Override base class definition.
        """
        __slots__ = 'name','vlan'
        def __init__(self, name):
            """
            This will create a simple interface.
            """
            self.name = name
            self.vlan = vlan
        
            			
    ###     end nested interface class      ###

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


        # the below methods where moved from the nested Interface class, and need to be refactored as it is now in the CiscoSwitch namespace.

    def set_interface_attributes("""OUTPUT OF: 'show run | section interface'"""):
    
        for line in ssh.send_config_command(['show run | section interface']):
        	# interface [Gi|Fa|Vlan...]
        if line.startswith('interface'):
            self.name = line.split()[-1]
        
        	# description
            if line.startswith('description'):
                self.description = str(line.split()[1:])
        
        	# shutdown
            if line.lstrip()startswith('shutdown'):
                self.shutdown = True
        
        	# port-type nni
            if line.lstrip().startswith('port-type'):
                line.split()[1]
        
        	# switchport mode [trunk|access]
            if line.lstrip().startswith('switchport'):
        
                		# switchport trunk
        		        if 'trunk' in line.split()[1]:
        
                    # switchport trunk native vlan <vlan>
                    if 'native' in line.split()[2]:
        
                        # switchport trunk native vlan
                        self.native_vlan = line.split()[-1]
        
                    # switchport trunk allowed vlan
                    if 'allowed' in line.split()[2]:
                        # return a list of vlans
                        # this could be problematic if a vlan range is used. (EG: 100-200... TODO)
                        self.vlans_allowed = line.split()[4].split(',')
        
                # switchport access <vlan>
                if 'access' in line.split()[1]:
                    self.vlan = line.split()[-1]
        
                # switchport mode [trunk|vlan]
                if 'mode' in line.split()[1]:
                    self.mode = line.split()[2]
        
        # rep segment
            if line.lstrip().startswith('rep'):
                if 'segment' in line.split()[1]:
                    self.rep_segment = line.split()[-1]
            
