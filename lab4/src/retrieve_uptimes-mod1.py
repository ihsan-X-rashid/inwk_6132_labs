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
    
    # Extract uptime information
    result = output.find('uptime is')
    if result != -1:
        uptime_info = output[result:result + 50].split("\n")[0]  # Adjust to capture the full uptime string
        print(f"{device['ip']} => {uptime_info}")
    else:
        print(f"Could not find uptime information for {device['ip']}")
