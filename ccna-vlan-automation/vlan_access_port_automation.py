from netmiko import ConnectHandler
from getpass import getpass

switch = {
    "device_type": "cisco_ios",
    "host": input("Switch IP: "),
    "username": input("Username: "),
    "password": getpass("Password: "),
}

vlan_id = int(input("VLAN ID: "))
vlan_name = input("VLAN Name: ")
interface = input("Interface: ")

connection = ConnectHandler(**switch)

commands = [
    f"vlan {vlan_id}",
    f"name {vlan_name}",
    f"interface {interface}",
    "switchport mode access",
    f"switchport access vlan {vlan_id}"
]

output = connection.send_config_set(commands)

print("\nConfiguration Output:\n")
print(output)

save_output = connection.save_config()

print("\nConfiguration Saved:\n")
print(save_output)

connection.disconnect()
print("\nVLAN configuration completed successfully.")