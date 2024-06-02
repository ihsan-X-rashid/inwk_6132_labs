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

# Iterate through the devices and execute commands
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip interface brief", use_textfsm=True)
    net_connect.disconnect()

    print(f"Interfaces for {device['ip']}:")
    print("-" * 100)
    
    # Print each interface name
    for interface in output:
        print(interface['interface'])
    
    print("-" * 100)

