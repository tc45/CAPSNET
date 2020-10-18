from ipaddress import ip_address, IPv4Address

ip1 = ["1.1.1.1",
        "1.1.1.777",
       "host12345",
       "10.1.1.0/24",
        "10.1.1.0/37",
       "fe80::/12",
       "fe80::abcd/12",
        "fe80::abcd/129",
       ]


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


def validCIDR(IP : str) -> str:
    valid_return = False
    output = {}

    # Replace backslash with forward slash
    value = IP.replace("\\", "/")

    if "/" in value:
        # Split string into CIDR and IP
        split = value.split("/")
        output['ip_address'] = split[0]
        output['cidr'] = split[1]
        # Check if first of string has IPv4 address
        if validIPAddress(output['ip_address']) == "IPv4":
            # Check if back of string has d digit less than or equal to 32
            if int(output['cidr']) <= 32:
                valid_return = True
                output['protocol'] = "IPv4"
        # Check if first of string has IPv4 address
        elif validIPAddress(output['ip_address']) == "IPv6":
            # Check if back of string has d digit less than or equal to 32
            if int(output['cidr']) <= 128:
                valid_return = True
                output['protocol'] = "IPv6"

    if valid_return:
        return output
    else:
        return False


for ip in ip1:
    cidr_details = validCIDR(ip)
    if isinstance(cidr_details, dict):
        print(ip)
        print("Protocol: " + cidr_details['protocol'])
        print("IP: " + cidr_details['ip_address'])
        print("CIDR: " + cidr_details['cidr'])
    else:
        print(ip + " is not a valid IPv4 or IPv6 format address.")
