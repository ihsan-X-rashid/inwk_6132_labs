from netmiko import Netmiko
import re

# Device connection details
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Connect to the device
net_connect = Netmiko(**device)

# Send the command
output = net_connect.send_command("show ip route")

# Disconnect from the device
net_connect.disconnect()

# Function to parse the command output
def parse_show_ip_route(output):
    routes = []
    lines = output.splitlines()
    for line in lines:
        # Match lines that start with protocol (O, C, S, etc.)
        match = re.match(r"^([A-Z]+)\s+(\d+\.\d+\.\d+\.\d+/\d+).*?(\d+)/(\d+)", line)
        if match:
            protocol, network, distance, metric = match.groups()
            routes.append({
                "protocol": protocol,
                "network": network,
                "distance": distance,
                "metric": metric
            })
    return routes

# Parse the output
parsed_routes = parse_show_ip_route(output)

# Print the desired information
for route in parsed_routes:
    print(f"Protocol: {route['protocol']}, Network: {route['network']}, Distance: {route['distance']}, Metric: {route['metric']}")

