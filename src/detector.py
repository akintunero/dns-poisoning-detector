import scapy.all as scapy
import time


def detect_dns_poisoning(timeout=60):
    suspicious_responses = []
    start_time = time.time()

    def process_packet(packet):
        if packet.haslayer(scapy.DNSRR):
            ip = packet[scapy.IP]
            dns = packet[scapy.DNS]
            if dns.ancount > 0:
                rdata = dns.an.rdata
                if isinstance(rdata, str):
                    if not is_valid_ip(rdata):
                        suspicious_responses.append((ip.src, dns.qd.qname.decode(), rdata))

    while time.time() - start_time < timeout:
        scapy.sniff(filter="udp port 53", prn=process_packet, store=0, timeout=1)

    return suspicious_responses


def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(0 <= int(part) <= 255 for part in parts)
