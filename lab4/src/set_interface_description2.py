from netmiko import Netmiko
import logging

# Enable logging for netmiko
logging.basicConfig(filename='netmiko_log.txt', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_from_file('changes.txt')
    print(output)
    net_connect.disconnect()

