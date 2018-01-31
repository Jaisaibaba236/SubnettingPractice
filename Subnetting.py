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

def binary(a):
   s=''
   t={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
   for c in oct(a)[1:]:
      s+=t[c]
   return s

binary(234)
