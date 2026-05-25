# 🚀 F5 VIP Inventory Exporter

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Netmiko](https://img.shields.io/badge/Netmiko-Network%20Automation-green)
![F5 BIG-IP](https://img.shields.io/badge/F5-BIG--IP-red)
![CSV Export](https://img.shields.io/badge/Output-CSV-orange)

---

## 📖 Overview

**F5 VIP Inventory Exporter** is a lightweight Python network automation script that connects to an 
**F5 BIG-IP Load Balancer** using **SSH and Netmiko**, retrieves Virtual Server (VIP) configuration details using 
**TMSH commands**, and exports the collected data into a CSV file.

This project demonstrates practical **Network Automation**, **Python Scripting**, **Netmiko**, **Regex Parsing**, and 
**Infrastructure Reporting** skills commonly used by Network Engineers and Network Automation Engineers.

---

## ✨ Features

✅ Connects securely to F5 BIG-IP devices via SSH

✅ Executes TMSH commands remotely

✅ Retrieves Virtual Server (VIP) information

✅ Extracts VIP names and destination addresses

✅ Generates CSV inventory reports

✅ Lightweight and easy to customize

✅ Ideal for network automation learning and portfolio projects

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Automation Development |
| Netmiko | SSH Connectivity |
| Regex | Output Parsing |
| CSV | Report Generation |
| F5 BIG-IP | Load Balancer Platform |
| TMSH | Configuration Retrieval |

---

## 📋 Command Executed

The script executes the following F5 BIG-IP command:

```bash
tmsh list ltm virtual one-line
```

This command retrieves:

- VIP Name
- Destination IP Address
- Destination Port
- Virtual Server Configuration Details

---

## 📊 Sample Output

### CSV Report

| VIP_Name | Destination |
|-----------|-------------|
| /Common/web_vip | /Common/10.10.10.100:443 |
| /Common/api_vip | /Common/10.10.10.101:443 |
| /Common/mail_vip | /Common/10.10.10.102:25 |

Generated file:

```text
vip_inventory.csv
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/f5-vip-inventory-exporter.git
```

Move into the project directory:

```bash
cd f5-vip-inventory-exporter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Python packages:

```bash
pip install netmiko
```

Or:

```bash
pip install -r requirements.txt
```

requirements.txt:

```text
netmiko
```

---

## 🚀 Usage

Update the device information inside the script:

```python
f5 = {
    "device_type": "linux",
    "host": "10.10.10.10",
    "username": "admin",
    "password": "password"
}
```

Run the script:

```bash
python vip_inventory.py
```

The script will connect to the F5 BIG-IP device, collect VIP details, and generate:

```text
vip_inventory.csv
```

---

## 📂 Project Structure

```text
f5-vip-inventory-exporter/
│
├── vip_inventory.py
├── requirements.txt
├── README.md
└── vip_inventory.csv
```

---

## 🎯 Use Cases

- F5 VIP Inventory Collection
- Load Balancer Documentation
- Configuration Auditing
- Migration Validation
- Infrastructure Reporting
- Network Automation Learning
- Network Engineering Portfolio Projects

---

## 🔒 Security Note

For production environments:

- Avoid hardcoding credentials
- Use environment variables
- Use secure credential vaults
- Restrict SSH access appropriately

---

## 📈 Future Enhancements

- [ ] Multi-device support
- [ ] Excel report export
- [ ] HTML reporting
- [ ] Email notifications
- [ ] Operational status collection
- [ ] Logging support
- [ ] Configuration auditing

---

## 👨‍💻 Author

**Ishant Patil**

Network Engineer | Python Enthusiast | Network Automation Learner

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐**.

It helps improve visibility and supports future network automation projects.

---