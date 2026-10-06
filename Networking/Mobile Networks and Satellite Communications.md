# Mobile / Celular Networks

A mobile network/celular network is the network used by phones for sms, calls and mobile internet: 3G, 4G/LTE and 5G.

        Cell Tower
            📡
       /     |      \
      /      |       \
 Phone     Phone     Phone
  📱        📱        📱

When a phone uses 4G or 5G

Phone
  ↓ radio signal
Cell Tower
  ↓
Mobile Operator Network
  ↓
Internet
  ↓
Server

An example is openning google.com without Wi-Fi:

Phone
↓
5G antenna
↓
Vodafone / MEO / NOS network
↓
Internet
↓
Google server

The communication between the phone and the antenna is made in radio frequences(RF)

The phone identifies himself to the network by his SIM/eSIM, which contains the information to authenticate the user.

## Handover/ Handoff

Imagine that you go on a car:

Tower A             Tower B             Tower C
  📡                  📡                  📡
   \                   |                  /
    📱 → → → → → → → 📱 → → → → → → → 📱

While moving, the phone lets a cell and connects to the next one.
This is called handover, the network tries to do this transition without interrupt the connection to the internet

## Generations

2G -> mainly voice and SMS
3G -> mobile Internet
4G -> fast IP-based data
5G -> higher speed, lower latency, many more connected devices

## Security concerns

There is a big difference between

Wi-Fi
Phone → Access Point → LAN → Internet

Cellular
Phone → Cell Tower → Mobile Provider → Internet

# Satellite Communications - SATCOM

Here its different

Instead of communicating with a on ground antenna, we can communicate with a satellite

Ground Station
     📡
      ↑
    Uplink
      ↑
   🛰 Satellite
      ↓
   Downlink
      ↓
     📡
Ground Station

Uplink = Terra -> satélite
Downlink = satélite -> Terra

## GEO, MEO and LEO Satellites

Not every satellites are at the same height

### LEO - Low Earth Orbit
Low Earth Orbit

Satellites that are near the earth

        🛰 🛰 🛰
     🛰       🛰
   🛰    🌍     🛰
     🛰       🛰
        🛰 🛰

They are closer so:
    - less distance for the signal
    - less latency
    - less power needed
    - each satelite covers little areas

So normally you need alot of satelites in constelation

### MEO- Medium Earth Orbit
Between LEO and GEO

Earth

        LEO
       🛰

          MEO
           🛰

                      GEO
                       🛰

One of the most known uses of MEO is satellite navigation

GPS satellites orbit around 20 200km of altitude, in medium earth orbit

### GEO - Geostationary Earth Orbit

A GEO satellite orbits the earth synced with earth rotation. In our point of view its always in the same place.

             🛰
             |
             |
             |
             🌍

This is used to telivision by satellite, tellecomunications, internet, meteorology communication. The problem about this satellites its the latency.
The signal has to travell a long distance
Earth
 ↓
~36,000 km
 ↓
Satellite
 ↓
~36,000 km
 ↓
Earth

| Orbit | Meaning | Distance | Latency | Coverage |
|---|---|---|---|---|
| **LEO** | Low Earth Orbit | Low | Low | Smaller |
| **MEO** | Medium Earth Orbit | Medium | Medium | Medium |
| **GEO** | Geostationary Earth Orbit | High | High | Very large |


## Starlink example

When we open for example youtube.com using starlink internet, the dataflow is this:

Your device
   ↓
Wi-Fi Router
   ↓
Starlink Dish / User Terminal
   ↓
Starlink Satellite
   ↓
Starlink Ground Gateway
   ↓
Starlink Point of Presence (PoP)
   ↓
Internet
   ↓
YouTube Server

1) The pc sends the request

We enter youtube.com

The pc creates the network packets and send them by wi fi to the router

Laptop
   ↓ Wi-Fi
Starlink Router

2) Router -> Starlink Antenna
The router is connected to starlink user terminal, the antenna in the exterior.

Laptop
   ↓
Router
   ↓
Starlink Dish

This is not a normal antenna its a phased-array antenna. This allows to guide eletronical radio beams to a satellite without needing to move physically the antenna. The starlink satellites do the same.

3)  Antenna -> Satellite

Starlink Dish
      ↑
      │ radio signal
      │
      🛰
Starlink Satellite

4) What does the satellite do?

The satellite needs to send the packet to a infrastructure connected to the internet.

The normal way is to send directly to a on ground station

Your Dish
    ↓
Satellite
    ↓
Starlink Gateway
    ↓
Fiber
    ↓
Internet

User Terminal → satellites → Gateway Site → fiber → Point of Presence → Internet.

5) The satellites can talk with each other

The satellites can have: Optical Inter-Satellite Links - ISLs

or simply:

Space Lasers

So this can happen

Your Dish
     ↓
    🛰
     ↓ laser
    🛰
     ↓ laser
    🛰
     ↓
Ground Gateway
     ↓
Internet
