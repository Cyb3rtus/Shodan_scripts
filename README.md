# Shodan_scripts

This script prints out properties of an IP address through the Shodan API. Do you have several IPs in a file? Do:
`while read -r ips; do ./shodan_ip_info.py $ips; sleep 2; done < your_ip_file.txt > shodan_scan.txt`.
This reads from a file of IPs, puts a 2 second sleep per request (shodan asks for a 1 second rate limit) and writes the output to a text file.
Make sure to make the script executable with `chmod +x shodan_ip_info.py`
