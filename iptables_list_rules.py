import subprocess

from iptables_strings import (
    NO_RULES_FOUND_MSG,
)


def list_rules():
    """Lists all iptables rules for the INPUT chain in a formatted way."""

    output = subprocess.run(["iptables", "-S", "INPUT"], capture_output=True, text=True, check=True).stdout
    # Split lines, remove empty lines, and format nicely
    rules = [line.strip() for line in output.splitlines() if line.strip()]
    if not rules:
        print(NO_RULES_FOUND_MSG)
        return

    print("** iptables Rules (INPUT chain): **")
    for i, rule in enumerate(rules):
        print(f"{i+1}. {rule}")
