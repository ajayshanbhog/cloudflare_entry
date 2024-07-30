import requests
import os 
from dotenv import load_dotenv

#Load Environment variables from .env files 
load_dotenv()

# Your Cloudflare API credentials
api_key = os.getenv('API_KEY')
zone_id = os.getenv('ZONE_ID')

# Subdomain and IP address for the A record
subdomain = os.getenv('SUBDOMAIN')
ip_address = os.getenv("IP_ADDR")

# Construct the API endpoint
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

# Construct the request headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Construct the request body
data = {
    'type': 'A',
    'name': subdomain,
    'content': ip_address,
    'ttl': 0,  # TTL (Time to Live) set to Auto
    'proxied': False  # Proxy of IP Addr is set to False
}

# Send the API request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("DNS record added successfully.")
else:
    print(f"Failed to add DNS record. Status code: {response.status_code}, Response: {response.json()}")
