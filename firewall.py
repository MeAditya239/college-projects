import ipaddress

class Firewall:
    def __init__(self):
        self.allowed_ips = set()
    def add_allowed_ip(self, ip):
        try:
            ip_address = ipaddress.ip_address(ip)
            self.allowed_ips.add(ip_address)
        except ValueError:
            print(f"Invalid IP address: {ip}")

    def remove_allowed_ip(self, ip):
        if ip in self.allowed_ips:
            self.allowed_ips.remove(ip)

    def is_allowed(self, ip):
        try:
            ip_address = ipaddress.ip_address(ip)
            return ip_address in self.allowed_ips
        except ValueError:
            print(f"Invalid IP address: {ip}")
            return False

if __name__ == "__main__":
    firewall = Firewall()

    num_ips = int(input("Enter the number of trusted IPs: "))
    for i in range(num_ips):
        ip = input(f"Enter trusted IP {i + 1}: ")
        firewall.add_allowed_ip(ip)

    num_requests = int(input("Enter the number of incoming requests: "))
    for i in range(num_requests):
        ip = input(f"Enter IP for incoming request {i + 1}: ")
        if firewall.is_allowed(ip):
            print(f"Incoming connection from {ip} allowed.")
        else:
            print(f"Incoming connection from {ip} blocked.")
