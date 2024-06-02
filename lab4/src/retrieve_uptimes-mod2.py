from netmiko import Netmiko

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

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    
    # Extract Configuration Register information
    config_register = None
    for line in output.splitlines():
        if "Configuration register is" in line:
            config_register = line
            break
    
    if config_register:
        print(f"{device['ip']} => {config_register}")
    else:
        print(f"Could not find Configuration Register information for {device['ip']}")

