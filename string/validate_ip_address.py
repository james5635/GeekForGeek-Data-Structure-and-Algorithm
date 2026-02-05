"""
Program to Validate IP Address

Given a string, check if it is a valid IPv4 or IPv6 address.

Approach: String parsing and validation - O(1) Time and O(1) Space
For IPv4: Four octets, each 0-255, separated by dots.
For IPv6: Eight groups, each 1-4 hex digits, separated by colons.
"""


def validate_ip_address(ip):
    """
    Validate if the given string is a valid IP address.

    Args:
        ip: Input string to validate

    Returns:
        "IPv4", "IPv6", or "Neither"
    """

    def is_valid_ipv4(parts):
        if len(parts) != 4:
            return False
        for part in parts:
            if not part or len(part) > 3:
                return False
            if part[0] == "0" and len(part) > 1:
                return False
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return True

    def is_valid_ipv6(parts):
        if len(parts) != 8:
            return False
        hex_chars = set("0123456789abcdefABCDEF")
        for part in parts:
            if not part or len(part) > 4:
                return False
            for char in part:
                if char not in hex_chars:
                    return False
        return True

    def expand_ipv6(ip):
        """Expand compressed IPv6 notation (::) to full form."""
        if "::" not in ip:
            return ip.split(":")

        # Can only have one ::
        if ip.count("::") > 1:
            return None

        # Split by ::
        left, right = ip.split("::")
        left_parts = left.split(":") if left else []
        right_parts = right.split(":") if right else []

        # Calculate how many zero groups to insert
        num_zeros = 8 - len(left_parts) - len(right_parts)
        if num_zeros < 1:  # Must have at least one zero group represented by ::
            return None

        # Build expanded parts
        expanded = left_parts + ["0"] * num_zeros + right_parts
        return expanded if len(expanded) == 8 else None

    # Check for IPv4
    if "." in ip and ":" not in ip:
        parts = ip.split(".")
        if is_valid_ipv4(parts):
            return "IPv4"

    # Check for IPv6
    elif ":" in ip and "." not in ip:
        parts = expand_ipv6(ip)
        if parts and is_valid_ipv6(parts):
            return "IPv6"

    return "Neither"


def main():
    """Test cases for IP address validation."""
    test_cases = [
        ("192.168.1.1", "IPv4"),
        ("255.255.255.255", "IPv4"),
        ("256.256.256.256", "Neither"),
        ("192.168.1", "Neither"),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
        ("2001:db8:85a3::8a2e:370:7334", "IPv6"),  # Compressed notation
        ("2001:0db8:85a3:0:0:8A2E:0370:7334:", "Neither"),
        ("abc", "Neither"),
    ]

    print("=" * 50)
    print("Validate IP Address")
    print("=" * 50)

    for ip, expected in test_cases:
        result = validate_ip_address(ip)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{ip}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()
