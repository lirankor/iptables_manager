#!/usr/bin/env python3

import subprocess
import re
from iptables_validation import validate_ip_address, validate_port_range
from iptables_actions import (
    is_iptables_installed,
    add_rule,
    edit_rule,
    delete_rule,
)
from iptables_list_rules import (list_rules)
from iptables_get_rule import (get_rule)
from iptables_activate import (activate_iptables)

from iptables_strings import (
    MENU_OPTIONS,
    NO_IPTABLES,
    WELCOME,
    INVALID_RULE_TYPE_MSG,
)


def main():
    while True:
        print(WELCOME)
        
        # check if we can continue
        if is_iptables_installed():
            print("Manager ready")
        else:
            print(NO_IPTABLES)
            break
        
        
        print(MENU_OPTIONS)
        choice = input("Enter your choice: ")

        if choice == "1":
            activate_iptables()
                
        elif choice == "2":
            selected_rule = input("Enter rule type 1:ACCEPT 2:DROP): ")
            if selected_rule == "1":
                rule_type = "ACCEPT"
            elif selected_rule == "2":
                rule_type = "DROP"
            else:
                print(INVALID_RULE_TYPE_MSG)                
            ip = input("Enter IP address (optional): ")
            port = input("Enter port number/range (optional): ")
            comment = input("Enter comment (optional): ")
            add_rule(rule_type, ip, port, comment)
        elif choice == "3":
            list_rules()
            rule_number = int(input("Enter rule number to edit: "))+1
            new_type = input("Enter new rule type (optional): ").upper() or None
            new_ip = input("Enter new IP address (optional): ") or None
            new_port = input("Enter new port number, for range seperate by (:) example: 8999:9003 (optional): ") or None
            new_comment = input("Enter new comment to help identify the rule (optional): ") or None
            edit_rule(rule_number, new_type, new_ip, new_port, new_comment)
        elif choice == "4":
            list_rules()
            rule_number = int(input("Enter rule number to delete: "))+1
            delete_rule(rule_number)
        elif choice == "5":
            list_rules()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose from the menu options.")


if __name__ == "__main__":
    main()
