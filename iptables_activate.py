import subprocess

from iptables_strings import (ACTIVATE, ACTIVATE_COMPLETED)

def activate_iptables():
    """Activates iptables with specific rules."""
    print(ACTIVATE)
    
    # ask for user IP
    user_ip = input("Please write your IP address: ") or None
    
    try:
        commands = [
            ["iptables", "-A", "INPUT", "-m", "state", "--state", "ESTABLISHED,RELATED", "-j", "ACCEPT"],
            ["iptables", "-A", "INPUT", "-i", "lo", "-m", "comment", "--comment", "Allow loopback connections", "-j", "ACCEPT"],
            ["iptables", "-A", "INPUT", "-p", "icmp", "-m", "comment", "--comment", "Allow Ping to work as expected", "-j", "ACCEPT"],   
        ]
        
        if user_ip is not None:
            commands.append(["iptables", "-A", "INPUT", "-s", user_ip, "-j", "ACCEPT"])
            
        commands.append(["iptables", "-P", "INPUT", "DROP"])
        commands.append(["iptables", "-P", "FORWARD", "DROP"])

        for command in commands:
            subprocess.run(command, check=True)
            

        print(ACTIVATE_COMPLETED)
    except subprocess.CalledProcessError:
        print("Failed to activate iptables. Please check manually.")