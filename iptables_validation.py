from ipaddress import ip_address  # Import for IP validation


def validate_ip_address(ip):
    """Validates an IP address format."""
    if not ip:
        return False  # Empty IP address is not valid

    try:
        ip_object = ip_address(ip)
        return True
    except (ValueError, ipaddress.AddressValueError):
        return False


def validate_port_range(port):
    """Validates a port number or range format."""
    if not port:
        return True  # No port is valid
    try:
        if "-" in port:
            start, end = port.split("-")
            if not start.isdigit() or not end.isdigit() or int(start) > int(end):
                return False
        else:
            if not port.isdigit():
                return False
        return True
    except ValueError:
        return False
