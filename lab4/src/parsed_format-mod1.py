from netmiko import Netmiko

# Define the device details
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Establish the connection
net_connect = Netmiko(**device)

# Execute the command with TextFSM parsing
output = net_connect.send_command("show ip interface brief", use_textfsm=True)

# Disconnect from the device
net_connect.disconnect()

# Print the type of the output
print(type(output))

# Print each interface name
for interface in output:
    print(interface['interface'])

