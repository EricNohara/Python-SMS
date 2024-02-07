from urllib.request import urlopen
from urllib.error import URLError

def detect_internet_connection():
    """Return if url can be opened, else keep waiting."""
    print("Waiting for network connection to execute...")
    while True:
        try:
            response = urlopen('https://www.google.com/', timeout=5)
            print("Network connection established!")
            return
        except URLError:
            pass