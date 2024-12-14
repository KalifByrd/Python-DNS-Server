# Python DNS Server with DNS Sinking

This is a simple DNS server built with Python using the `dnslib` library. The server listens for DNS queries and provides responses. It also supports DNS sinking to block specified domains by resolving them to `0.0.0.0`.

## Features

- **DNS Sinking**: Block specified domains by resolving them to `0.0.0.0`.
- **Custom Resolutions**: Configure placeholder IPs for non-blocked domains.
- **Simple and Lightweight**: Easy to use and modify.
- **Extensible**: Can be extended to support additional DNS record types and query forwarding.

## Requirements

- Python 3.7+
- `dnslib` library

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>

   ```

2. Install dependencies:

   ```bash
   pip install dnslib

   ```

## **Usage**

### **Running the Server**

1. Save the script as `dns_server.py` (if not already done).
2. Run the script:

   ```bash
   python dns_server.py

   ```

3. The server will start listening for DNS queries on `0.0.0.0:5353`.

### **Configure Your Network**

- Set your DNS server to the IP of the machine running the script.
- Ensure port `5353` is used for DNS queries.

### **Modifying Blocked Domains**

Update the `BLOCKED_DOMAINS` set in the script to include domains you want to block:  
BLOCKED_DOMAINS \= {  
 "example.com",  
 "ads.example.net",  
 "tracking.example.org"

- }

### **Default Behavior**

- Blocked domains resolve to `0.0.0.0`.
- Non-blocked domains resolve to a placeholder IP (`192.168.1.1` by default).
- Logs incoming queries and resolution actions.

## **Extending Functionality**

### **Forward Non-Blocked Queries**

You can extend the script to forward non-blocked queries to a public DNS resolver (e.g., Google DNS `8.8.8.8`) for real DNS resolution.

### **Add Support for Additional Record Types**

Currently, the server supports `A` records. You can add support for `AAAA`, `CNAME`, etc., by modifying the `DNSHandler` class.

## **Example Output**

When the server receives queries, it logs actions to the console:
