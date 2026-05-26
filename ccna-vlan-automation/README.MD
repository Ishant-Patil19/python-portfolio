# 🚀 Cisco VLAN & Access Port Automation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cisco IOS](https://img.shields.io/badge/Cisco-IOS-green)
![Netmiko](https://img.shields.io/badge/Netmiko-Network%20Automation-orange)
![CCNA](https://img.shields.io/badge/CCNA-Automation-red)

---

## 📖 Overview

Cisco VLAN & Access Port Automation is a Python-based network automation script that connects to Cisco IOS switches using SSH and Netmiko, creates a VLAN, and configures an interface as an access port in the specified VLAN.

This project demonstrates practical Network Automation concepts commonly used by Network Engineers, NOC Engineers, Infrastructure Engineers, and CCNA learners.

---

## ✨ Features

✅ Connect to Cisco IOS switches via SSH

✅ Create VLANs automatically

✅ Configure switch ports as access ports

✅ Assign interfaces to specific VLANs

✅ Save configuration to startup-config

✅ Interactive user input

✅ Password masking using getpass

✅ Simple and beginner-friendly Python automation project

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Automation Development |
| Netmiko | SSH Connectivity |
| Cisco IOS | Network Device Configuration |
| getpass | Secure Password Input |
| CCNA Concepts | VLANs & Access Ports |

---

## 📋 Automated Configuration

The script automatically generates commands similar to:

```cisco
conf t

vlan 10
 name USERS

interface GigabitEthernet1/0/5
 switchport mode access
 switchport access vlan 10

end

write memory
```

---

## 🖥 Example Execution

```text
Switch IP: 192.168.1.10
Username: admin
Password:

VLAN ID: 10
VLAN Name: USERS
Interface: GigabitEthernet1/0/5
```

Output:

```text
Connecting to switch...

Creating VLAN 10...
Configuring interface GigabitEthernet1/0/5...

Configuration saved successfully.

VLAN deployment completed.
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ccna-vlan-automation.git
```

Move into the project folder:

```bash
cd ccna-vlan-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Install manually:

```bash
pip install netmiko
```

or

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
python vlan_access_port_automation.py
```

Provide:

- Switch IP Address
- Username
- Password
- VLAN ID
- VLAN Name
- Interface Name

The script will:

1. Connect to the switch
2. Create the VLAN
3. Configure the access port
4. Assign the VLAN
5. Save the configuration

---

## 📂 Project Structure

```text
cisco-vlan-access-port-automation/
│
├── vlan_access_port_automation.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 Learning Objectives

This project helps demonstrate:

- Python for Network Automation
- Netmiko Device Connectivity
- Cisco IOS Configuration Automation
- VLAN Management
- Access Port Configuration
- SSH Automation
- CCNA Practical Skills
- Infrastructure Automation

---

## 🔒 Security Best Practices

For production environments:

- Avoid hardcoded credentials
- Use environment variables
- Use secure credential vaults
- Restrict management access
- Enable AAA authentication

---

## 📈 Future Enhancements

- [ ] Bulk VLAN deployment from CSV
- [ ] Multi-switch support
- [ ] Configuration rollback
- [ ] VLAN existence validation
- [ ] Interface validation
- [ ] Logging support
- [ ] Configuration backup before changes
- [ ] HTML reporting

---

## 👨‍💻 Author

**Ishant Patil**

Network Engineer | Python Enthusiast | Network Automation Learner

---

## ⭐ Support

If you found this project useful, consider giving it a Star ⭐.

It helps support future network automation projects.

---