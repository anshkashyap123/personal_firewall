# 🛡️ Personal Firewall (Python)

A lightweight personal firewall built using Python, Scapy, and Tkinter. It filters network traffic based on customizable rules and provides real-time packet monitoring with a GUI.

## 🔧 Features

- Block traffic based on IPs, ports, and protocols
- Live traffic monitoring in a GUI
- Packet logging for auditing
- Optional system-level enforcement with iptables (Linux only)

## 📦 Requirements

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/en/latest/)
- Tkinter (GUI library)

### Install Dependencies

#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk -y
pip3 install scapy
```

#### On Windows:
```bash
# Make sure Python is installed from https://www.python.org/
pip install scapy
```

#### On macOS:
```bash
brew install python3
pip3 install scapy
```

## 🚀 How to Run

Clone the repository and run the Python script:

```bash
git clone https://github.com/yourusername/personal-firewall.git
cd personal-firewall
python personal_firewall.py
```

If you want to apply system-level rules with `iptables`, run with sudo:
```bash
sudo python3 personal_firewall.py
```

## 📂 File Structure

```
personal-firewall/
├── personal_firewall.py       # Main firewall script
├── firewall_log.txt           # Log file for blocked packets
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🔐 License

This project is licensed under the MIT License.
