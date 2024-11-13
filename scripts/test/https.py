import network
import time
import urequests

# Configure the Wi-Fi interface
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    wifi.connect(ssid, password)
    start_time = time.time()

    # Wait for connection
    while not wifi.isconnected():
        if time.time() - start_time > 10:
            print("Connection timeout!")
            return False
        time.sleep(1)

    print(f"Connected to {ssid}!")
    return True

# Fetch content via HTTPS
def fetch_https(url):
    try:
        # Make the HTTPS request
        response = urequests.get(url, timeout=10)

        # Print the response status and content
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        print(response.text)

        response.close()
    except Exception as e:
        print("Error during HTTP request:", e)

# Get user input from the terminal
def get_user_input():
    ssid = input("Enter Wi-Fi SSID: ")
    password = input("Enter Wi-Fi Password: ")
    url = input("Enter the URL to fetch via HTTPS: ")
    return ssid, password, url

# Main program
ssid, password, url = get_user_input()

# Connect to Wi-Fi
if not connect_to_wifi(ssid, password):
    print("Unable to connect to Wi-Fi.")
else:
    # Fetch content via HTTPS
    fetch_https(url)
