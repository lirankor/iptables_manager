import subprocess
import re


def get_rule(rule_number):
    """Gets the specific rule at the given number (if it exists)."""

    output = subprocess.run(["iptables", "-S", "INPUT"], capture_output=True, text=True, check=True).stdout
    matches = re.findall(rf"\d+ target \S+", output, re.MULTILINE)
    if matches and rule_number <= len(matches):
        return matches[rule_number - 1]
    else:
        return None
