#!/usr/bin/env python3
import shodan
import sys
api = shodan.Shodan('YOUR_API_KEY_HERE')

# This script prints out properties of an IP address through the Shodan API.
# Do you have several IPs in a file? Do:
# while read -r ips; do ./shodan_ip_info.py $ips; sleep 2; done < your_ip_file.txt > shodan_scan.txt
# this reads from a file of IPs, puts a 2 second sleep per request (shodan asks for a 1 second rate limit) and 
# writes the output to a text file
# Make sure to make the script executable with "chmod +x shodan_ip_info.py"



if len(sys.argv) != 2:
    print("Usage: python3 shodan_ips.py <IP-address>")
    sys.exit(1)

ip_address = sys.argv[1]

try:
    info = api.host(ip_address)
    print(f"IP: {info['ip_str']}")
    print(f"Organization: {info.get('org', 'N/A')}")
    print(f"OS: {info.get('os', 'N/A')}")
    print(f"Vulns: {info.get('vulns', 'N/A')}")
    print(f"ASN: {info.get('asn', 'N/A')}")
    print(f"ISP: {info.get('isp', 'N/A')}")
    print(f"Hostnames: {info.get('hostnames', 'N/A')}")
    print(f"Ports: {info.get('ports', 'N/A')}")
    print("_________________________________")
    # Add more relevant information as needed
except shodan.APIError as e:
    print(f"Error: {e}")
