import requests

# This file demonstrates a simple use case for the outdated 'requests' library.
# The version used here is intentionally old (2.20.0) as defined in pyproject.toml.

def check_status(url):
    """
    Makes a simple GET request and prints the HTTP status code.
    """
    try:
        # Note: The version of 'requests' used here should ideally be updated 
        # for better security and features. Renovate will fix this.
        response = requests.get(url)
        print(f"Successfully checked {url}")
        print(f"HTTP Status Code: {response.status_code}")
        # Print the version we are currently using, which Renovate should update
        print(f"requests library version: {requests.__version__}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_status("https://www.google.com")

