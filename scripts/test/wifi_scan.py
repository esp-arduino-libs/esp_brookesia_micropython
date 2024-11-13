import network
import time

# Configure the Wi-Fi interface
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Scan for nearby networks
def scan_networks():
    print("Scanning for nearby networks...")
    networks = wifi.scan()

    if not networks:
        print("No networks found.")
        return

    # Display the scan results
    print("Found the following networks:")
    for network in networks:
        ssid = network[0].decode('utf-8')  # Name of the network
        bssid = network[1]  # BSSID of the network
        channel = network[2]  # Channel
        rssi = network[3]  # Signal strength
        authmode = network[4]  # Authentication mode
        hidden = network[5]  # Whether the network is hidden

        print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}, RSSI: {rssi}, Authmode: {authmode}, Hidden: {hidden}")

# Connect to a Wi-Fi network
def connect_to_wifi(ssid, password):
    wifi.connect(ssid, password)
    start_time = time.time()

    # Wait for the connection
    while not wifi.isconnected():
        if time.time() - start_time > 10:
            print("Connection timeout!")
            return False
        time.sleep(1)

    print(f"Connected to {ssid}!")
    return True

# Perform Wi-Fi scan
scan_networks()
