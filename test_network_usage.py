import psutil

def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent + net_io.bytes_recv

def main():
    network_usage = get_network_usage()
    print(f"Total Network Usage: {network_usage} bytes")
    print(f"Total Network Usage: {network_usage / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    main()
