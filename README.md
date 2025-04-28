Cisco Switch Configuration Backup
Overview
This Python script connects to a Cisco switch over SSH, retrieves the full running configuration, and saves it into a local text file.
It uses paramiko for secure SSH communication and is designed to work with minimal setup.

Features
Connects to Cisco switches via SSH

Runs show running-config

Saves the output to a .txt file

No pagination issues (terminal length 0 command included)

Requirements
Python 3.x

paramiko library

Install dependencies:

bash
Copy
Edit
pip install paramiko
How to Use
Edit the script and update:

switch_ip → your switch IP address

username → your SSH username

password → your SSH password

Make the script executable:

bash
Copy
Edit
chmod +x get_switch_config.py
Run the script:

bash
Copy
Edit
./get_switch_config.py
The switch configuration will be saved in switch_config.txt.

Example
bash
Copy
Edit
$ python get_switch_config.py
Configuration saved to switch_config.txt
Notes
Make sure SSH is enabled on your Cisco switch.

User credentials must have permission to run show running-config.

The script can be extended easily to support multiple switches from a list.
