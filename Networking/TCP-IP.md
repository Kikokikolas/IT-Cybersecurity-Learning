# TCP/IP

TCP/IP is the collection of protocols used for communication across networks.

## Main Protocols

- **IP (Internet Protocol)**: Addresses devices and routes packets between
	networks.
- **TCP (Transmission Control Protocol)**: Provides reliable, ordered delivery
	of data and detects transmission errors.
- **UDP (User Datagram Protocol)**: Sends datagrams without establishing a
	connection, which reduces overhead but does not guarantee delivery.

## Encapsulation

When data travels across a network, each layer adds information needed by the
next layer. The receiving device removes these headers in reverse order.

```text
Application data
				|
				v
TCP segment
				|
				v
IP packet
				|
				v
Link-layer frame
```