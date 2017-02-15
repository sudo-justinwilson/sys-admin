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

    def _get_running_config(self):
        """
        This method has to be over-ridden by subclasses.
        """
        raise Exception('self.get_running_config has to be over-ridden!')
    



class BaseCiscoSwitch(BaseCiscoDevice):
    """
    This will be used as a base class for Cisco switches.
    """
    ###     start nested interface class      ###
    
    # this is a simple nested class to abstractly define an interface:
    class Interface:
        """
        Abstract an interface. Override base class definition.
        """
        __slots__ = 'name','mode'
        def __init__(self, name, mode):
            """
            This will create a simple interface.
            """
            self.name = name
            # access port or trunk?
            self.mode = mode
        
            			
    ###     end nested interface class      ###

    def __init__(self, ip_address, username, password=None, port=22):
        """
        Create a CiscoDevice instance.
        """
        self.ip_address = ip_address
        self.username = username
        if password is not None:
            self.password = password
        self.port = port

class CiscoSwitchNetmiko(BaseCiscoSwitch):
    """
    Class that describes a Cisco IOS switch using netmiko to communicate with the switch.
    """

    def ssh_connection(self):
        """
        Establish an SSH connection using netmiko.
        """
        try:
            this_device = {
                'device_type' : 'cisco_ios',
                'ip' : self.ip_address,
                'username' : self.username,
                'password' : self.password,
                'port' : self.port,
                }
            connection = ConnectionHandler(**this_device)
            return connection
        except KeyError as e:
            print('The value "', e, '" has not been defined.')

    # up to here
    # I think "exec_command" is a waste of time...
    def exec_command(self, command, expect=None):
        """
        Send a show command and return the output.

        Mandatory args:
        command:
            the command to send to privileged exec mode
        
        Optional args:
        expect:
            expect string
        """
        try:
            ssh_session = self.ssh_connection()
        except Exception as e:
            print('Could not connect to host because of the following error:')
            print(e)
        if expect_string:
            output = ssh_session.send_command(command, expect_string=expect)
        else:
            output = ssh_session.send_command(command)
        return output

    def _get_running_config(self)
        """
        Return running-config from switch.
        """
        ssh = self.ssh_connection()
        output = ssh.send_command('show run')
        return output


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
            
