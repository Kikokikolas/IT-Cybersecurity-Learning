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