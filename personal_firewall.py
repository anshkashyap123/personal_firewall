    proto = packet.proto
    dport = None

    if TCP in packet:
        dport = packet[TCP].dport
    elif UDP in packet:
        dport = packet[UDP].dport

    for rule in rules:
        if (rule["ip"] == ip_layer.src or rule["ip"] == "any") and \
           (str(rule["port"]) == str(dport) or rule["port"] == "any") and \
           (str(rule["protocol"]) == str(proto) or rule["protocol"] == "any"):
            if rule["action"] == "block":
                logging.info(f"Blocked: {ip_layer.src}:{dport} -> {ip_layer.dst}")
                print(f"[BLOCKED] {ip_layer.src}:{dport} -> {ip_layer.dst}")
                return False

    print(f"[ALLOWED] {ip_layer.src}:{dport} -> {ip_layer.dst}")
    return True

def packet_callback(packet):
    check_packet(packet)

print("[*] Starting firewall... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
