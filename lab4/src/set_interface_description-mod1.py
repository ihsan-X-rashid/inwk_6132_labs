from netmiko import Netmiko

devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

description = 'Description set with Netmiko'
loopback_number = 1
loopback_ip = '10.1.1.1'
loopback_mask = '255.255.255.0'

# Configuration commands for the Loopback interface
loopback_config = [
    f"interface Loopback{loopback_number}",
    f"ip address {loopback_ip} {loopback_mask}",
    f"description {description}"
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print(output)
    net_connect.disconnect()

