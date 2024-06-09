## iptables Manager: Manage Your Linux Firewall with Ease

This Python script provides a user-friendly interface to manage iptables, the default firewall software on most Linux distributions. It simplifies firewall configuration by offering an interactive menu for adding, editing, deleting, and listing rules.

**Features:**

* **Intuitive Interface:**  Navigate through adding, editing, deleting, and listing rules with a clear menu system.
* **Simplified Rule Management:** No need to write complex iptables commands directly. Define rules based on IP address, port, comment, and desired action (ACCEPT or DROP).
* **Input Validation:**  Ensures proper rule creation by validating user input for IP addresses and port ranges.

**Benefits:**

* **User-Friendly:** Makes firewall management accessible even for those unfamiliar with complex iptables commands.
* **Efficient:** Saves time and effort compared to manually crafting iptables rules.
* **Organized:** Provides a clear overview of your firewall rules with the `list rules` option.

**Getting Started:**

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/lirankor/iptables-manager.git](https://github.com/lirankor/iptables-manager.git)
   ```

2. **Install Dependencies: No external dependencies required!**
3. **Make Executable (Optional):** 
   ```
   Bash
   chmod +x iptables_manager.py
   ```
4. **Run the Script:**
   ```
   Bash
   ./iptables_manager.py
   ```

** Usage: **
The script presents a menu with options for activating iptables, adding, editing, deleting, and listing rules. Follow the on-screen instructions to manage your firewall effectively.

*** Important Note: ***
* **Modifying firewall rules can impact your system's security. Use this script with caution and understand the implications of each rule.
* **For advanced firewall configurations, refer to the official iptables documentation.

**License:**
This project is licensed under the *GNU General Public License (GPL) v3*. Refer to the LICENSE file for details.

**Contribution:**
We welcome contributions to improve this script. Feel free to submit pull requests to the GitHub repository.

  
