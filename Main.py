import paramiko

# Switch login info
switch_ip = "192.168.1.1"
username = "admin"
password = "your_password"
port = 22

# Output file
output_file = "switch_config.txt"

def get_switch_config(ip, username, password, port=22):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)

        # Start interactive shell
        chan = ssh.invoke_shell()

        # Give it time to connect
        chan.recv(9999)

        # Send commands
        chan.send("terminal length 0\n")  # Don't paginate output
        chan.send("show running-config\n")
        
        # Wait for output
        buff = ""
        while not buff.endswith("#"):
            resp = chan.recv(9999).decode("utf-8")
            buff += resp

        # Close connection
        ssh.close()

        # Save config to file
        with open(output_file, "w") as f:
            f.write(buff)

        print(f"Configuration saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_switch_config(switch_ip, username, password, port)
