# Routers and Switches

## Switches

A switch connects multiple devices in the same local area network. It does not care about IP addresses, it only cares about physical hardware addresses known as MAC Addresses (ex AA:BB:CC:11:22:33)

### How a switch knows how to send data

The Learning Process: When you plug your Linux PC into a switch port and send a frame, the switch looks at the Source MAC Address and records "PC A is on Port 1"

The Forwarding Process: When PC A wants to send data to PC B, the switch checks its table for PC B MAC address:

If found in the table: It forwards the data only to the specific port where PC B is connected.

If NOT found (Unknown Unicast) - it floods the packet to every single port (except the one it came from) until PC B responds and reveals its port location.

## Routers

A router connects different networks together (e.g., your home subnet 192.168.1.0/24 to the Internet). It works exclusively with IP Addresses.

How a Router Knows Where to Send Data:
A router maintains a Routing Table. This table acts like a roadmap containing network destinations, netmasks, and the best path (next hop) to reach them.

Looking at the Destination: When a packet arrives, the router strips off the Layer 2 MAC header and looks at the Destination IP Address.

Consulting the Routing Table: It matches the destination IP against its routes using the Longest Prefix Match rule (the most specific subnet rule wins).

Finding the Next Hop:

If the destination IP is on a directly connected network, it hands the packet off locally.

If the destination IP is out on the Internet, it forwards the packet to its Default Gateway (the next upstream router).

Feature,Switch,Router
Network Level,Same Subnet (Local),Different Subnets / Internet
OSI Layer,Layer 2 (Data Link),Layer 3 (Network)
Address Type Used,MAC Addresses,IP Addresses
Core Decision Table,MAC Address Table,Routing Table
Traffic Handling,Forwards locally or floods unknown ports,Forwards along the best IP route or drops invalid packets

