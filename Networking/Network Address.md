Imagine your home network ist:

192.168.1.0/24

/24 means that subnet mask is:

255.255.255.0

So we have:

| Address         | Meaning                          |
| --------------- | -------------------------------- |
| `192.168.1.0`   | **Network address / Network ID** |
| `192.168.1.1`   | Often the **default gateway**    |
| `192.168.1.2`   | Normal device                    |
| `192.168.1.50`  | Normal device                    |
| `192.168.1.254` | Normal device                    |
| `192.168.1.255` | **Broadcast address**            |

So there is 256 total addresses, but only 254 usable host addresses.

## What is the Network Address?

The network address identifies the network itslef

Its like the name of the street.

So the .0 is the network identifier

## What is the Broadcast Address?

The broadcast address means:

Send this packet to every device on this subnet.

For: 192.168.1.0/24

The broadcast is:
192.168.1.255

Imagine:
PC1 ─┐
PC2 ─┤
PC3 ─┤
PC4 ─┤
     Switch

If something is sent to:
    192.168.1.255

    it is adressed to the entire local subnet

Therefore you dont normally give: 192.168.1.255 to a computer.

## What is the Subnet Mask?

IP: 192.168.1.1
Subnet Mask: 255.255.255.0

The subnet mask tells the computer:

Which part of the IP represents my network, and which part represents the host/device?

With:

255.255.255.0

you can think of:

192.168.1 . 50
─────────   ──
 Network    Host

 So: 192.168.1 identifies the network

 And 50 identifies the host

 ### /24 meaning    

 Instead of writing 255.255.255.0 often we see /24
 So these mean the same thing

 192.168.1.50/24

 and

 IP:   192.168.1.50
Mask: 255.255.255.0

Why is it 24?

IPv4 has 32 bits

8 bits . 8 bits . 8 bits . 8 bits

With /24

NETWORK                 HOST
11111111.11111111.11111111.00000000
   8   +   8   +   8
            =
           24

Which in decimal is 255.255.255.0