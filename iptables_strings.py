WELCOME = """
iptables Manager
Cecking for compatability
"""

MENU_OPTIONS = """
iptables Manager

1. Activate iptables
2. Add rule
3. Edit rule
4. Delete rule
5. List rules
0. Exit

"""

NO_IPTABLES = """0
Could not find iptables 

There could be several reasons why iptables is not found on your system:

1. iptables is not installed: This is the most common reason. It's usually pre-installed on many Linux distributions, but not on other systems.

2. iptables is installed, but it's not in your system's PATH

Exiting...

"""

ACTIVATE = """
Note activating the iptables might get you locked out of the system
Please check your IP address and add it on the next step.
If IP tables are active and presistent a restart will not reset the access rules.

Please make sure iptables are presistent, a guid is available here:
https://medium.com/@oryaacov/3-ways-to-make-iptables-persistent-a77e956ee78

"""

ACTIVATE_COMPLETED = """
Iptables activation has been successfully completed.

To ensure the iptables service starts on boot and your rules are saved, follow these steps:

For systemd-based systems (like Ubuntu, Debian, CentOS 7 and above):
1. Create a service file for iptables, typically at /etc/systemd/system/iptables.service
2. Enable the service using the command: sudo systemctl enable iptables
3. Start the service using the command: sudo systemctl start iptables

For systems using service and chkconfig (like CentOS 6 and below):
1. Save the current iptables rules using the command: sudo service iptables save
2. Ensure the service starts on boot using the command: sudo chkconfig iptables on

Please note that these commands should be run as root or with sudo, and the exact commands can vary between different Linux distributions. Always check the specific documentation for your system.
"""

INVALID_RULE_TYPE_MSG = "Invalid rule type. Please type 1 for ACCEPT or 2 DROP."
INVALID_IP_MSG = "Invalid IP address format."
INVALID_PORT_MSG = "Invalid port format. Use a single port number or a range (e.g., 80, 22-25)."

RULE_ADDED_MSG = "Rule added successfully: {}"
RULE_EDITED_MSG = "Rule {} edited successfully."
RULE_DELETED_MSG = "Rule {} deleted successfully."

NO_RULES_FOUND_MSG = "No rules found in the INPUT chain."
