from dnslib import DNSRecord, DNSHeader, RR, A, QTYPE
from socketserver import UDPServer, BaseRequestHandler
import socket

BLOCKED_DOMAINS = {
    "example.com",
    "ads.example.net",
    "tracking.example.org"
}

BLOCK_IP = "0.0.0.0"

class DNSHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        request = DNSRecord.parse(data)
        domain = str(request.q.qname).rstrip(".")

        print(f"Received query for: {domain}")

        response = DNSRecord(
            DNSHeader(id=request.header.id, qr=1, aa=1, ra=1),
            q=request.q
        )

        if domain in BLOCKED_DOMAINS:
            print(f"Blocked domain: {domain}")
            response.add_answer(RR(domain, QTYPE.A, rdata=A(BLOCK_IP)))
        else:
            placeholder_ip = "192.168.1.1"
            print(f"Resolving domain {domain} to {placeholder_ip}")
            response.add_answer(RR(domain, QTYPE.A, rdata=A(placeholder_ip)))

        socket.sendto(response.pack(), self.client_address)

def start_dns_server(host="0.0.0.0", port=5354):
    with UDPServer((host, port), DNSHandler) as server:
        print(f"DNS server running on {host}:{port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down DNS server.")

if __name__ == "__main__":
    start_dns_server()
