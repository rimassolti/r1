import socket
import requests

def get_ip_address(url):
    try:
        # Try to resolve the IP address using socket.gethostbyname()
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        # If socket.gethostbyname() fails, try to resolve using a custom resolver
        resolvers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
        for resolver in resolvers:
            try:
                socket.gethostbyname(url, resolver)
                return ip_address
            except socket.gaierror:
                pass
        # If all custom resolvers fail, try to resolve using a public API
        try:
            response = requests.get(f"https://api.ipify.org/?host={url}")
            return response.text
        except requests.exceptions.RequestException:
            pass
        # If all methods fail, return an error message
        return "Unable to resolve the IP address"

def main():
    url = input("Enter the URL: ")
    ip_address = get_ip_address(url)
    print(f"IP address of {url}: {ip_address}")

if __name__ == "__main__":
    main()