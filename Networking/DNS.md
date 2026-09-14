# Domain Name System (DNS)

The **Domain Name System (DNS)** translates domain names into IP addresses.

```text
example.com -> 93.184.216.34
```

Computers communicate using IP addresses, but IP addresses are difficult for
people to remember. DNS allows us to use names such as `google.com` instead.

## What Happens When You Visit a Website?

Suppose you enter:

```text
https://www.example.com
```

Before the browser can send an HTTP or HTTPS request, it must discover the IP
address of `www.example.com`.

```text
User
   |
   | enters www.example.com
   v
Browser
   |
   | asks for the IP address
   v
DNS resolver
   |
   | returns the answer
   v
IP address: 93.184.216.34
   |
   v
Browser
   |
   | sends the HTTP/HTTPS request
   v
Web server
   |
   v
Webpage
```

In short:

- **DNS:** Finds the server's IP address.
- **HTTP/HTTPS:** Requests the webpage or other data from the server.

## Who Answers the DNS Request?

A computer does not normally know the IP address of every website. Instead, it
asks a **DNS recursive resolver**.

The resolver might be operated by:

- An Internet service provider (ISP)
- Cloudflare: `1.1.1.1`
- Google: `8.8.8.8`
- Another DNS provider

If the resolver does not already have the answer in its cache, it may perform
several queries on behalf of the computer.

## The DNS Resolution Process

The complete process looks roughly like this:

```text
Browser
   |
   v
Recursive DNS resolver
   |
   v
Root DNS server
   |
   v
.com TLD server
   |
   v
Authoritative DNS server
   |
   v
IP address
   |
   v
Resolver
   |
   v
Browser
```

### Root DNS Server

The resolver asks the root server where it can find information about the
`.com` domain. The root server points the resolver towards the `.com` DNS
infrastructure.

### Top-Level Domain (TLD) Server

TLD means **Top-Level Domain**.

Examples include:

- `.com`
- `.org`
- `.net`
- `.pt`
- `.uk`

The `.com` TLD server can tell the resolver which authoritative name servers
are responsible for `example.com`.

### Authoritative DNS Server

The authoritative DNS server stores the official DNS records for a domain. It
can provide the final answer, for example:

```text
www.example.com -> 93.184.216.34
```

The resolver returns this answer to the computer, and the browser can then
connect to the web server.

## DNS Caching and TTL

DNS uses caching to avoid repeating the entire lookup every time a domain is
requested. A DNS answer may be cached by:

- The computer
- The local router
- The recursive resolver
- The ISP

If an answer is already cached, the process is shorter:

```text
Browser
   |
   v
Resolver
   |
   v
Cached answer
   |
   v
Browser
```

This is faster, but cached records are not kept forever.

### TTL: Time to Live

**TTL** specifies approximately how many seconds a DNS record may remain in a
cache before the resolver asks for an updated version.

For example:

```text
Record: example.com -> 192.0.2.10
TTL:    3600 seconds
```

A TTL of `3600` means that the record may generally be cached for one hour.

## DNS Records

DNS stores different kinds of information in records. The most common records
are listed below.

| Record | Purpose | Example |
| --- | --- | --- |
| `A` | Maps a hostname to an IPv4 address. | `example.com -> 192.0.2.10` |
| `AAAA` | Maps a hostname to an IPv6 address. | `example.com -> 2001:db8::1` |
| `CNAME` | Creates an alias for another hostname. | `www.example.com -> example.com` |
| `MX` | Identifies the mail servers that receive email for a domain. | `example.com -> mail.example.com` |
| `NS` | Identifies the authoritative name servers for a domain. | `example.com -> ns1.provider.com` |
| `TXT` | Stores text associated with a domain. | Domain verification or email security data |
| `PTR` | Maps an IP address to a hostname for reverse DNS. | `8.8.8.8 -> dns.google` |

### A and AAAA Records

- `A` records map hostnames to IPv4 addresses.
- `AAAA` records map hostnames to IPv6 addresses.

```text
example.com  A     -> 192.0.2.10
example.com  AAAA  -> 2001:db8::1
```

### CNAME Records

CNAME means **Canonical Name**. It creates an alias that points to another
hostname.

```text
www.example.com  CNAME  -> example.com
example.com      A      -> 192.0.2.10
```

### MX Records

MX means **Mail Exchange**. It specifies which mail servers receive email for
a domain.

```text
example.com  MX  -> mail.example.com
```

### NS Records

NS means **Name Server**. It identifies the authoritative DNS servers
responsible for a domain.

```text
example.com  NS  -> ns1.provider.com
example.com  NS  -> ns2.provider.com
```

### TXT Records

TXT records store text associated with a domain. They are commonly used for
domain verification and email security mechanisms such as SPF, DKIM, and
DMARC.

```text
example.com  TXT  -> "text information"
```

### PTR Records and Reverse DNS

PTR records are used for reverse DNS lookups. Instead of asking for an IP
address from a hostname, a reverse lookup asks for a hostname from an IP
address.

```text
Normal lookup:   google.com -> IP address
Reverse lookup:  IP address -> hostname

8.8.8.8  PTR  -> dns.google
```

## DNS Ports

DNS normally uses:

- **UDP port 53** for most queries because it is fast and has low overhead.
- **TCP port 53** when a response is too large for UDP or when a reliable TCP
   connection is required, including some DNS operations.

In Wireshark, you can filter DNS traffic with:

```text
dns
```

or with a port filter:

```text
udp.port == 53
```

A typical DNS exchange might look like this:

```text
PC -> DNS server: Standard query A example.com
DNS server -> PC: Standard query response A 93.184.216.34
```
