import socket

# Function to scan for CCTV camera ports on a target IP address
def scan_cctv_ports(target):
    camera_ports = [80, 554]  # Common ports used by CCTV cameras
    open_ports = []

    for port in camera_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

# Function to display progress
def display_progress(current, total):
    percent_complete = (current / total) * 100
    print(f"Progress: {current}/{total} ({percent_complete:.2f}%)")

# Main function
if __name__ == '__main__':
    subnet = "192.168.1"  # Adjust the subnet to match your network configuration
    potential_cctv_devices = []

    total_targets = 255
    completed_targets = 0

    for i in range(1, 256):
        target_ip = f"{subnet}.{i}"
        open_ports = scan_cctv_ports(target_ip)
        
        if open_ports:
            potential_cctv_devices.append((target_ip, open_ports))
        
        completed_targets += 1
        display_progress(completed_targets, total_targets)
    
    if potential_cctv_devices:
        print("Potential CCTV cameras on your network:")
        for ip, ports in potential_cctv_devices:
            print(f"IP Address: {ip}, Open Ports: {ports}")
    else:
        print("No potential CCTV cameras found on your network.")
