blocked_ips = {"192.168.1.10", "192.168.1.20", "192.168.1.30"}
blocked_ips.add("192.168.1.40")
blocked_ips.add("192.168.1.50")
blocked_ips.remove("192.168.1.20")
print(blocked_ips)