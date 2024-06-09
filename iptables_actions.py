import subprocess
import re
from iptables_validation import validate_ip_address, validate_port_range
from iptables_strings import (
    INVALID_RULE_TYPE_MSG,
    INVALID_IP_MSG,
    INVALID_PORT_MSG,
    RULE_ADDED_MSG,
    RULE_EDITED_MSG,
    RULE_DELETED_MSG,
)

def is_iptables_installed():
    """Checks if iptables is installed."""
    try:
        subprocess.run(["iptables", "-V"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def build_rule_command(rule_type, ip, port, comment):
    """
    Builds the iptables rule command based on provided options.

    Args:
        rule_type (str): ACCEPT or DROP
        ip (str, optional): IP address to allow/block
        port (str, optional): Port number or range
        comment (str, optional): Rule comment

    Returns:
        str: The complete iptables rule command
    """

    if rule_type not in ("ACCEPT", "DROP"):
        raise ValueError("Invalid rule type. Please choose ACCEPT or DROP.")

    ip_rule = f"-s {ip}" if ip else ""
    if port:
        if "-" in port:
            port_rule = f"-p tcp --dport {port}"
        else:
            port_rule = f"-p tcp -m multiport --dports {port}"
    else:
        port_rule = ""

    comment_rule = f"-m comment --comment \"{comment}\"" if comment else ""

    return f"iptables -A INPUT {ip_rule} {port_rule} {comment_rule} -j {rule_type}"


def add_rule(rule_type, ip="", port="", comment=""):
    """Adds an iptables rule based on the specified type, IP, port, and comment."""

    if not validate_ip_address(ip) and ip:
        print(INVALID_IP_MSG)
        return

    if not validate_port_range(port) and port:
        print(INVALID_PORT_MSG)
        return

    try:
        command = build_rule_command(rule_type, ip, port, comment)
        if isinstance(command, str):
            command = command.split()
        subprocess.run(command, check=True)
        print(RULE_ADDED_MSG.format(' '.join(command)))  # Use f-string for formatting
    except ValueError as e:
        print(e)


def edit_rule(rule_number, new_type=None, new_ip=None, new_port=None, new_comment=""):
    """Edits an existing iptables rule based on the specified number and optional changes."""

    current_rule = get_rule(rule_number)
    if not current_rule:
        print(f"Rule {rule_number} not found.")
        return

    # Build the new rule command
    command = "iptables -R INPUT "
    command += current_rule.replace("-A", "-R")  # Replace -A with -R for edit

    # Update rule components based on user input with validation
    if new_type:
        if new_type not in ("ACCEPT", "DROP"):
            print(INVALID_RULE_TYPE_MSG)
            return
        target = f"-j {new_type}"
        command += target + " "
    if new_ip:
        if not validate_ip_address(new_ip):
            print(INVALID_IP_MSG)
            return
        command += f"-s {new_ip} "
    if new_port:
        if not validate_port_range(new_port):
            print(INVALID_PORT_MSG)
            return
        if "-" in new_port:
            port_rule = f"-p tcp --dport {new_port}"
        else:
            port_rule = f"-p tcp -m multiport --dports {new_port}"
        command += port_rule + " "
    if new_comment:
        command += f"-m comment --comment \"{new_comment}\""

    # Delete the old rule and add the new one
    subprocess.run(["iptables", "-D", "INPUT", str(rule_number)], check=True)
    subprocess.run(command.split(), check=True)
    print(RULE_EDITED_MSG.format(rule_number))  # Use f-string for formatting


def delete_rule(rule_number):
    """Deletes an existing iptables rule based on the specified number."""

    subprocess.run(["iptables", "-D", "INPUT", str(rule_number)], check=True)
    print(RULE_DELETED_MSG.format(rule_number))  # Use f-string for formatting
