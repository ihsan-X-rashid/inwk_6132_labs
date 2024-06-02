import logging
import requests
from requests.auth import HTTPBasicAuth
import json
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# Load YAML file
with open('lab_Ex_routers.yaml', 'r') as file:
    routers = yaml.safe_load(file)

# Define user credentials
USER = 'student'
PASS = 'Meilab123'

def set_interface(router_ip, interface_name, ip_address):
    BASE_URL = f'http://{router_ip}/restconf/api/running/'
    url = BASE_URL + f'interfaces/interface/{interface_name}'
    auth = HTTPBasicAuth(USER, PASS)
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    data = {
        "ietf-interfaces:interface": {
            "name": interface_name,
            "description": "Configured through Restconf",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_address,
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    response = requests.put(url, auth=auth, headers=headers, data=json.dumps(data))
    
    if response.status_code == 204:
        logging.info(f"Request was successful on {router_ip}, Interface: {interface_name}, Code: {response.status_code}")
        return "success!"
    else:
        logging.error(f"Error encountered during request on {router_ip}, Interface: {interface_name}, Code: {response.status_code}")
        return response.text

# Iterate over the routers and configure interfaces
for router_name, router_info in routers['routers'].items():
    management_ip = router_info['management_ip']
    for interface_name, ip_address in router_info['interfaces'].items():
        result = set_interface(management_ip, interface_name, ip_address)
        print(f"{router_name} {interface_name}: {result}")

