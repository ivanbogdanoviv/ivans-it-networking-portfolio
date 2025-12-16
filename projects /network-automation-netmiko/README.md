# 🔌 Network Automation (Python + Netmiko)

Automates common Cisco IOS device tasks via SSH using Python and Netmiko.

This project demonstrates **entry-level network automation fundamentals** suitable for IT Support, Junior Technician, and Network Support internship roles.

---

## 🧠 What This Project Demonstrates

- Inventory-based multi-device automation
- Read-only auditing using Cisco *show* commands
- Structured Python scripting
- Safe automation practices (no hardcoded credentials)
- Clear, recruiter-friendly documentation

---

## 📂 Project Structure

- `src/` — Python source code
- `sample-data/` — Sample device inventory (no real devices or credentials)

---

## ▶ How to Run

1. Install the required dependency:

```bash
pip install netmiko
```

2. Run the automation script:

```bash
python src/show_commands.py
```

---

## 🔐 Security Notes

- Credentials are **never stored** in source code
- Sample inventory uses **test IP addresses only**
- No production configurations are included
