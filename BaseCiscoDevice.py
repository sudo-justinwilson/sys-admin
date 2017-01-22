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

    def __init__(self, name, **kwargs):
        """
        Create an CiscoDevice instance.
        """
        self.name = name

    def cdp_neighbours(self, args):
        """
        Returns a {linked?} list of CDP neighbours.
        """
        ssh = ConnectionHandler(**args)



