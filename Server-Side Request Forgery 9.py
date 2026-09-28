import urllib.parse
import ipaddress
import socket
import requests

ALLOWED_DOMAINS = {"://trustedpartner.com", "example.com"}

def get_secure_url(user_input):
    try:
        parsed_url = urllib.parse.urlparse(user_input)
        
        if parsed_url.scheme != "https":
            raise ValueError("Invalid protocol. Only HTTPS is allowed.")
            
        hostname = parsed_url.hostname
        if not hostname or hostname not in ALLOWED_DOMAINS:
            raise ValueError("Access to the requested domain is restricted.")
            
        ip_address_str = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(ip_address_str)
        
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local:
            raise ValueError("Access to internal networks is forbidden.")
            
        response = requests.get(user_input, timeout=5, allow_redirects=False)
        return response.text

    except (ValueError, socket.gaierror, requests.RequestException) as e:
        return f"Secure Request Failed: {str(e)}"
