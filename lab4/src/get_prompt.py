from netmiko import Netmiko
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101", # R1 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

"""from netmiko import Netmiko
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102", # R2 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

from netmiko import Netmiko
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103", # R3 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())

from netmiko import Netmiko
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.104", # R4 Mgmt Interface
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}
net_connect = Netmiko(**device)
print(net_connect.find_prompt())"""
