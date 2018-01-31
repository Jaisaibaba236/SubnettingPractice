#Just Started

class IPAddressing:

    #invoke this method when any instance is getting created for this class
    def __init__(self,ip):
       self.ip_address = ip

    def subnetting(self):
       my_ip_list = self.ip_address.split('.')
       #print(my_ip_list)

ipaddress = IPAddressing('192.168.10.2')
ipaddress.subnetting()
