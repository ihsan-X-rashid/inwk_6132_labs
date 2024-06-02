from netmiko import Netmiko

# List of devices in the topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",  # Router 4
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
    # Add more devices as needed
]

for device in devices:
    net_connect = Netmiko(**device)
    print(f"Connected to {device['ip']}")

    # Get the default prompt
    default_prompt = net_connect.find_prompt()
    print(f"Default prompt: {default_prompt}")

    # Send disable command and get the prompt
    net_connect.send_command_timing("disable")
    disable_prompt = net_connect.find_prompt()
    print(f"Disable command prompt: {disable_prompt}")

    # Enable command and get the prompt
    net_connect.enable()
    enable_prompt = net_connect.find_prompt()
    print(f"Enable command prompt: {enable_prompt}")

    # Disconnect from the device
    net_connect.disconnect()
    print(f"Disconnected from {device['ip']}\n")

