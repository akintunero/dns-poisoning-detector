import ipaddress
import yaml
from pathlib import Path

def load_config(config_path="config/config.yaml"):
    """Load configuration from YAML file."""
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)

def is_valid_ip(ip_str):
    """Check if the given string is a valid IP address."""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def create_directory_if_not_exists(directory_path):
    """Create a directory if it doesn't exist."""
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def format_dns_response(response):
    """Format DNS response for reporting."""
    return f"Source: {response[0]}, Domain: {response[1]}, IP: {response[2]}"

def is_suspicious_ip(ip, trusted_servers):
    """Check if an IP is suspicious (not in trusted servers list)."""
    return ip not in trusted_servers