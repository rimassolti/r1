import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve the IP address"

def main():
    url = input("Enter the URL: ")
    ip_address = get_ip_address(url)
    print(f"IP address of {url}: {ip_address}")

if __name__ == "__main__":
    main()