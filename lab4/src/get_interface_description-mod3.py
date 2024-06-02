from netmiko import ConnectHandler

# List of devices in the topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",  # Router 4
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]

# Iterate through the devices and execute commands
for device in devices:
    net_connect = ConnectHandler(**device)
    
    # Show interface description
    output = net_connect.send_command("show interface description")
    print(f"Interface description for {device['ip']}:")
    print("-" * 100)
    print(output)
    print("-" * 100)
    
    # Show IP interface brief
    output = net_connect.send_command("show ip interface brief")
    print(f"IP interface brief for {device['ip']}:")
    print("-" * 100)
    print(output)
    print("-" * 100)
    
    # Show version
    output = net_connect.send_command("show version")
    print(f"Version information for {device['ip']}:")
    print("-" * 100)
    print(output)
    print("-" * 100)
    
    # Show running configuration
    output = net_connect.send_command("show running-config")
    print(f"Running configuration for {device['ip']}:")
    print("-" * 100)
    print(output)
    print("-" * 100)
    
    net_connect.disconnect()

