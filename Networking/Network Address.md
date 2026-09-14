# Network Addresses

Imagine that your home network is:

`192.168.1.0/24`

The `/24` notation means that the subnet mask is:

`255.255.255.0`

## Addresses in the Network

| Address | Meaning |
| --- | --- |
| `192.168.1.0` | **Network address** or **Network ID** |
| `192.168.1.1` | Often the **default gateway** |
| `192.168.1.2` | Device address |
| `192.168.1.50` | Device address |
| `192.168.1.254` | Device address |
| `192.168.1.255` | **Broadcast address** |

There are 256 total addresses, but only 254 usable host addresses. The network address and broadcast address are reserved.

## What Is the Network Address?

The network address identifies the network itself.

It is like the name of a street.

For `192.168.1.0/24`, the `.0` is the network identifier.

## What Is the Broadcast Address?

The broadcast address is used to send a packet to every device on the same subnet.

For `192.168.1.0/24`, the broadcast address is:

`192.168.1.255`

```text
PC1 ─┐
PC2 ─┤
PC3 ─┤── Switch
PC4 ─┘
```

When a packet is sent to `192.168.1.255`, it is addressed to the entire local subnet.

Therefore, you do not normally assign `192.168.1.255` to a computer.

## What Is the Subnet Mask?

The subnet mask tells the computer which part of the IP address represents the network and which part represents the host or device.

Example:

```text
IP address:   192.168.1.50
Subnet mask:  255.255.255.0
```

With `255.255.255.0`, you can think of the address like this:

```text
192.168.1 . 50
─────────   ──
 Network    Host
```

`192.168.1` identifies the network, while `50` identifies the host.

### What Does `/24` Mean?

Instead of writing `255.255.255.0`, we often use `/24`. They mean the same thing:

```text
192.168.1.50/24
```

```text
IP address:   192.168.1.50
Subnet mask:  255.255.255.0
```

IPv4 addresses have 32 bits:

```text
8 bits . 8 bits . 8 bits . 8 bits
```

With `/24`, the first 24 bits represent the network and the remaining 8 bits represent the host:

```text
NETWORK                 HOST
11111111.11111111.11111111.00000000
    8   +   8   +   8          = 24
```

In decimal notation, this is `255.255.255.0`.

## What Is the Default Gateway?

The default gateway is the device a computer uses to reach other networks. In most home networks, the default gateway is the router's IP address.

Example:

```text
IP address:       192.168.1.50
Subnet mask:      255.255.255.0
Default gateway:  192.168.1.1
```

If the computer wants to communicate with a device outside `192.168.1.0/24`, it sends the traffic to the default gateway. The router then forwards the traffic to the appropriate network.


### Example

```text
PC                         Router                  Internet
192.168.1.50  ───────────>  192.168.1.1  ────────>
```

The computer might have this configuration:

```text
IP address:       192.168.1.50
Subnet mask:      255.255.255.0
Default gateway:  192.168.1.1
DNS server:       8.8.8.8
```

The computer first checks whether the destination is inside its local subnet.

- `192.168.1.80` is in the same subnet, so the computer can communicate with it directly.
- `142.250.x.x` is outside the local subnet, so the computer sends the packet to the router through the default gateway.

The router then forwards the traffic towards the other network or the Internet.

> **Important:** The default gateway does not have to be `.1`. It can use any valid host address on the subnet, as long as the computer can reach it.

It could be:
192.168.1.254
or
192.168.1.100

as long as it's correctly configured as the router's interface in that subnet.

.1 is simply a very common convention.

## 192.168.x.x and Divisions

192.168.x.x belongs to the private IPv4 address ranges.

The official private ranges are:

| Private range                   |  CIDR |
| ------------------------------- | ----: |
| `10.0.0.0 – 10.255.255.255`     |  `/8` |
| `172.16.0.0 – 172.31.255.255`   | `/12` |
| `192.168.0.0 – 192.168.255.255` | `/16` |

These addresses are reserved for private networks and are not globally routable on the public internet

This is why your laptop might have:

192.168.1.24

and my laptop somewhere else could also have:
192.168.1.24

without a problem, because they are in two different private networks

Earlier we said:

192.168.1.0 = Network
192.168.1.255 = Broadcast

But that's because we used:

/24
255.255.255.0

Consider instead:

192.168.1.0/26

/26 means:

255.255.255.192

Now that original /24 network has been broken into smaller subnets:

| Network            | Usable hosts  | Broadcast |
| ------------------ | ------------- | --------- |
| `192.168.1.0/26`   | `.1 – .62`    | `.63`     |
| `192.168.1.64/26`  | `.65 – .126`  | `.127`    |
| `192.168.1.128/26` | `.129 – .190` | `.191`    |
| `192.168.1.192/26` | `.193 – .254` | `.255`    |

Now look at this:

192.168.1.64

In a /24, .64 could be a normal computer.

But in this /26:

192.168.1.64

is a network address.

And:

192.168.1.63

is a broadcast address.

That's why the rule:

.0 = network and .255 = broadcast

is not universally true.

The subnet mask determines them.

So basically if we have /26 it means 26 bits are for the network so 32-26 are for the hosts in this case 6 bits are for the hosts

if we have 24 bits in the network we have 1 network , if we have 6 bits = 64 hosts we can divide the network in 4 subnetworks so our interval of 0 to 255 is divided into 4 subnets.

In each subnet we use 64 addresses but one is for the Network ID and the other is used for the broadcast in each subnet so for each subnet we have 62 hosts. 62 x 4 is 248 so we have 248 usable hosts in total. The defaultgateway has a usable host.

## Diagram

Lets take a look at this example:

IP Address: 192.168.10.45
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.10.1

This is something like this:
Network
192.168.10.0/24

           Router
       192.168.10.1
            │
            │
     ┌──────┴──────┐
     │             │
192.168.10.45   192.168.10.80
    PC              PC

Broadcast:
192.168.10.255

If it wants to communicate with 192.168.10.80 -> same subnet no default gateway needed
If it wants to communicate with 192.168.20.80 -> different subnet default gateway needed
If it wants to communicate with 8.8.8.8 -> different network default gateway needed

If we used /26 for communicating beteween subnets we would use the gateway also