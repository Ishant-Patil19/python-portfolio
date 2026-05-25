from netmiko import ConnectHandler
import csv
import re

f5 = {
    "device_type": "linux",
    "host": "10.10.10.10",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**f5)
output = connection.send_command("list ltm virtual one-line")

connection.disconnect()

vip_list = []
for line in output.splitlines():
    vip_match = re.search(
        r'ltm virtual\s+(\S+)',
        line
    )

    destination_match = re.search(
        r'destination\s+(\S+)',
        line
    )

    if vip_match:
        vip_list.append([
            vip_match.group(1),
            destination_match.group(1)
            if destination_match
            else "N/A"
        ])

with open("vip_inventory.csv","w", newline=" " ) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["VIP_Name", "Destination"])
    writer.writerows(vip_list)

print("VIP inventory exported.")
