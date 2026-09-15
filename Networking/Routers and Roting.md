# Router

A router connects different networks and decides where packets should go next. More precisely, when a router receives an IP packet, it looks at the destination IP address, checks its routing table, and chooses the next hop or outgoing interface.

Imagine:

PC
192.168.1.10
    |
    |
Router A
192.168.1.1
10.0.0.1
    |
    |
Router B
10.0.0.2
172.16.0.1
    |
    |
Server
172.16.0.50

Your PC wants to send something to:

172.16.0.50

It first checks:

Is 172.16.0.50 in my local subnet?

If your PC is:

192.168.1.10/24

then its local network is:

192.168.1.0/24

172.16.0.50 is clearly not local, so the PC sends the packet to its default gateway:

192.168.1.1

That router receives the packet.

Then the router does not ask:

"What website is this?"

It asks:

"Which route matches destination IP 172.16.0.50?"

That is routing.

## The routing table

A router has something like this: 
Destination        Next Hop        Interface

192.168.1.0/24     directly        eth0
10.0.0.0/24        directly        eth1
172.16.0.0/24      10.0.0.2        eth1
0.0.0.0/0          ISP router      wan0

Suppose the destination is:

172.16.0.50

The router sees:

172.16.0.0/24 → next hop 10.0.0.2

So:

Packet
destination = 172.16.0.50
        ↓
Router checks routing table
        ↓
Match: 172.16.0.0/24
        ↓
Next hop = 10.0.0.2
        ↓
Send packet to Router B

Router B then repeats the same process. A router essentially chooses a next hop based on its routing/forwarding database.

And notice something important:

The destination IP stays 172.16.0.50.

Router A doesn't change it to Router B's IP just because Router B is the next hop.

Conceptually:

Final destination:
172.16.0.50

Next hop:
10.0.0.2

Those are two different ideas.

## Directly connected routes

If a router has an interface:

192.168.1.1/24

it automatically knows:

192.168.1.0/24

is directly connected.

Likewise:

10.0.0.1/24

means it knows:

10.0.0.0/24

is directly connected.

It doesn't need another router to reach those networks.

Router
├── eth0: 192.168.1.1/24
│          ↓
│       192.168.1.0/24 directly connected
│
└── eth1: 10.0.0.1/24
           ↓
        10.0.0.0/24 directly connected

Directly connected networks are fundamental entries in the routing table.

Static routes

Imagine Router A does not automatically know how to reach:

172.16.0.0/24

but you know Router B can reach it.

You can manually tell Router A:

To reach 172.16.0.0/24
send packets to 10.0.0.2

That is a static route.

Conceptually:

172.16.0.0/24 → 10.0.0.2

Static routes are routes manually configured by an administrator and remain until they are changed or removed.

They're useful when:

network is small
routes rarely change
you want predictable paths

But imagine having:

500 routers
20,000 networks

Configuring all routes manually would become horrible.

That brings us to dynamic routing.

Dynamic routing

Routers can communicate with other routers and learn routes automatically.

Protocols include:

OSPF
BGP
RIP
EIGRP
IS-IS

For example:

Router A              Router B
   |                     |
   | "I know 192.168..." |
   |-------------------->|
   |                     |
   | "I know 172.16..."  |
   |<--------------------|

The routers build/update their routing tables based on information learned through routing protocols.

Dynamic routing is useful because when the network changes, routers can recalculate routes automatically instead of requiring an administrator to manually update every route.

You don't need to learn OSPF/BGP deeply yet. Just remember:

Static Routing
→ administrator manually defines routes

Dynamic Routing
→ routers learn routes using routing protocols
The default route

You already know the default gateway, so now connect it to routing.

A router can also have a default route:

0.0.0.0/0

Meaning:

If I don't know a more specific route, send it this way.

Example:

192.168.1.0/24 → directly connected
10.0.0.0/24    → directly connected
172.16.0.0/24  → 10.0.0.2
0.0.0.0/0      → ISP

If the destination is:

8.8.8.8

none of the first routes match.

So:

8.8.8.8
   ↓
No specific route
   ↓
0.0.0.0/0
   ↓
ISP

That's why a default route is sometimes called the gateway of last resort.

How does the router choose between multiple routes?

This part is very important.

Imagine the routing table contains:

10.0.0.0/8
10.1.0.0/16
10.1.2.0/24

And your destination is:

10.1.2.50

Technically, all three match.

But the router chooses the most specific route:

10.1.2.0/24

This is called:

Longest Prefix Match.

Think:

10.0.0.0/8       very broad
10.1.0.0/16      more specific
10.1.2.0/24      most specific ✅

Specific destination routes take precedence over a general default route.

This concept becomes extremely important in networking.

Routing vs switching

Also don't mix these two:

Switch
→ mainly forwards Ethernet frames using MAC addresses
→ usually inside a LAN

Router
→ forwards IP packets using IP addresses
→ connects different IP networks

Very simplified:

Same network:
PC → Switch → PC

Different network:
PC → Switch → Router → another network
And what happens at every router?

Imagine:

PC → Router A → Router B → Router C → Server

Each router independently does:

1. Receive packet
2. Read destination IP
3. Check routing table
4. Select best route
5. Determine next hop/interface
6. Forward packet

Then the next router repeats it.

This is called hop-by-hop forwarding.

Packet
 ↓
Router A
 ↓
Router B
 ↓
Router C
 ↓
Destination

## The communication

When a router sends information, it travels in the internet by optic fiber cables and chains of conected networks.

## #Tier 3/ Tier 2 communications
The routers in the way:

ISPs

Normally the routers in the path are from the locals ISPs. In case of Portugal is MEO, Vodafone, NOS, Digi,etc. The router from our houses connects to the central route of the ISP. if the site is the same ISP or if it is close to you, the travel ends.

## Network traffic / Interligation

This are from neutral associations of IT. They do the crossing betwwen ISPs.

## The Giants of the internet / Tier 1 Providers

Big corporations, Telia (Arelion), Lumen(L3),NTT, Cogent, Tata Communications.

What they do? They are the owners of the submarin fiber optic cables that cross oceans and theya re the owners of huge routers that connect continents.

Local ISPs pay this companys Tier1 to send traffic to the other side of the world.


