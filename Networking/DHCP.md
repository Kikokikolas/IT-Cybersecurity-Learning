# DHCP

DHCP (Dynamic Host Configuration Protocol) is the network service responsible for automatically configuring network settings for any device that connects to a network.

Without DHCP, every time you connected your phone to Wi-FI or plugged your Ubuntu machine into an ethernet cable, you would have to manually open your settings and type in:

1. An available IP address
2. The subnet mask
3. The default gateway (your router's IP)
4. The DNS servers

DHCP handles this automatically, usually within a few seconds.

## How DHCP Works: The D.O.R.A Process

When your computer connects to a network, it doesn't know its own IP address or where the router is. It starts a 4-step "handshake" with the DHCP Server (which usually runs inside your home router):

```text
[ Your Computer / Ubuntu ]                  [ DHCP Server / Router ]
             |                                           |
             | -------- 1. DISCOVER (Broadcast) -------> | "Is there a DHCP server here? I need an IP."
             | <------- 2. OFFER ----------------------- | "Here's an offer: you can use 192.168.1.50."
             | -------- 3. REQUEST --------------------> | "I accept! Please reserve 192.168.1.50 for me."
             | <------- 4. ACK ------------------------- | "Confirmed. It's yours for the next 24 hours."
             |                                           |
```

This process is called DORA (Discover, Offer, Request, Acknowledge), and it automatically provides your computer with its network configuration. This example describes DHCP for IPv4; IPv6 uses different mechanisms, including DHCPv6 and SLAAC.

## IP Leases and Renewals

A DHCP address is assigned for a limited period called a **lease**. The 24 hours in the example above is just an example; the network administrator configures the lease duration.

- By default, the client tries to renew with the original server halfway through the lease (T1).
- If that server does not respond, the client tries to contact any available DHCP server at 87.5% of the lease duration (T2).
- If the lease expires without renewal, the client must stop using that address and obtain a valid configuration again.

The server can specify different T1 and T2 values. A successful renewal lets a device keep its address without repeating the full initial DORA exchange.

## Address Pools and Reservations

An **address pool** is the range of addresses a DHCP server can assign. For example, a home network might use:

| Setting | Example |
| --- | --- |
| Network | `192.168.1.0/24` |
| Subnet mask | `255.255.255.0` |
| Default gateway | `192.168.1.1` |
| DHCP pool | `192.168.1.100` to `192.168.1.200` |

A **reservation** associates a particular client with a specific IP address, commonly using its MAC address or client identifier. This is useful for a printer that should keep the same address while still receiving settings automatically.

A **static IP** is configured manually on the device. Keep manually assigned addresses outside the DHCP pool, or exclude them on the server, to avoid address conflicts.

## Ports and DHCP Relays

DHCPv4 uses **UDP port 67 on the server** and **UDP port 68 on the client**. A client initially uses broadcasts because it does not yet know the server's address.

Routers normally do not forward these broadcasts between subnets. A **DHCP relay** forwards DHCP messages between clients and a server on another subnet, allowing one server to serve multiple networks or VLANs.

## Basic Troubleshooting on Ubuntu

These commands help inspect the configuration without changing it:

```bash
# Show IPv4 addresses assigned to each interface
ip -4 address show

# Show routes, including the default gateway
ip route show

# Show DNS settings on systems using systemd-resolved
resolvectl status
```

If a device cannot connect, check whether it has an address in the expected subnet, a default route, and the correct DNS settings. An automatically assigned `169.254.x.x` address can indicate that the device did not obtain a DHCP lease; it is a link-local address and does not normally provide access beyond the local link.

Also check that the DHCP server is reachable, its address pool is not exhausted, and the device is connected to the intended network or VLAN. A valid DHCP lease alone does not guarantee internet access.

## Security Considerations

A **rogue DHCP server** can send clients incorrect gateway or DNS settings, potentially redirecting their traffic. A **DHCP starvation attack** attempts to exhaust the available leases so legitimate devices cannot obtain addresses.

On supported managed switches, **DHCP snooping** helps block unauthorized server replies by allowing them only on trusted ports. Rate limits and access controls can also help reduce abuse.
