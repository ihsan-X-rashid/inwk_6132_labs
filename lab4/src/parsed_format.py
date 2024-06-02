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

# Execute the command
output = net_connect.send_command("show ip interface brief")

# Disconnect from the device
net_connect.disconnect()

# Print the type of the output
print(type(output))

