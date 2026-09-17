# DHCP

DHCP (Dynamic Host Configuration Protocol) is the network service responsible for automatically configuring network settings for any device that connects to a network.

Without DHCP, every time you connected your phone to Wi-FI or plugged your Ubuntu machine into an ethernet cable, you would have to manually open your settings and type in:

1 An available IP address
2 The subnet Mask
3 The Default Gateway (your routers IP)
4 The DNS servers

DHCP handles all of this less in a second

## How DHCP Works: The D.O.R.A Process

When your computer connects to a network, it doesn't know its own IP address or where the router is. It starts a 4-step "handshake" with the DHCP Server (which usually runs inside your home router):

[ Your Computer / Ubuntu ]                  [ DHCP Server / Router ]
             |                                           |
             | -------- 1. DISCOVER (Broadcast) -------> | "Is there a DHCP server here? I need an IP."
             | <------- 2. OFFER ----------------------- | "Here's an offer: you can use 192.168.1.50."
             | -------- 3. REQUEST --------------------> | "I accept! Please reserve 192.168.1.50 for me."
             | <------- 4. ACK ------------------------- | "Confirmed. It's yours for the next 24 hours."
             |                                           |
This process is called DORA (Discover, Offer, Request, Acknowledge), and it automatically provides your computer with its network configuration.