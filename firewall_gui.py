        # Clear previous custom rules first (simple cleanup, not full flush)
        subprocess.run(["sudo", "iptables", "-F"], stdout=subprocess.DEVNULL)

        # Block IPs
        for ip in rules["blocked_ips"]:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

        # Block Ports
        for port in rules["blocked_ports"]:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "udp", "--dport", str(port), "-j", "DROP"])

        # Block Protocols
        for proto in rules["blocked_protocols"]:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", proto.lower(), "-j", "DROP"])

        self.live_output.insert(tk.END, ">>> Applied iptables rules.\n")


# 🔥 Launch
if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallGUI(root)
    root.mainloop()
