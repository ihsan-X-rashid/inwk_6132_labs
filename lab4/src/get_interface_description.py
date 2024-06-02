from netmiko import ConnectHandler

# Device configurations
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Iterate through the devices and execute commands
for device in (r1, r2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()
    
    print("-" * 100)
    print(output)
    print("-" * 100)

