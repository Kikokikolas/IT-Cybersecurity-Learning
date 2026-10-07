# Mobile Networks and Satellite Communications

## Mobile / Cellular Networks

A mobile network, or cellular network, is the network used by phones for SMS, calls, and mobile internet: 3G, 4G/LTE, and 5G.

```text
        Cell Tower
            📡
       /     |      \
      /      |       \
 Phone     Phone     Phone
  📱        📱        📱
```

When a phone uses 4G or 5G:

```text
Phone
  ↓ radio signal
Cell Tower
  ↓
Mobile Operator Network
  ↓
Internet
  ↓
Server
```

An example is opening `google.com` without Wi-Fi:

```text
Phone
  ↓
5G Antenna
  ↓
Vodafone / MEO / NOS Network
  ↓
Internet
  ↓
Google Server
```

Communication between the phone and the antenna uses radio frequencies (RF).

The phone identifies itself to the network through its SIM/eSIM, which contains the information needed to authenticate the user.

### Handover / Handoff

Imagine that you are travelling in a car:

```text
Tower A             Tower B             Tower C
  📡                  📡                  📡
   \                   |                  /
    📱 → → → → → → → 📱 → → → → → → → 📱
```

While moving, the phone leaves one cell and connects to the next one.
This is called **handover**. The network tries to make this transition without interrupting the internet connection.

### Generations

- **2G**: Mainly voice and SMS.
- **3G**: Mobile internet.
- **4G**: Fast IP-based data.
- **5G**: Higher speeds, lower latency, and many more connected devices.

### Security Concerns

There is a big difference between Wi-Fi and cellular network paths:

**Wi-Fi:**

```text
Phone → Access Point → LAN → Internet
```

**Cellular:**

```text
Phone → Cell Tower → Mobile Provider → Internet
```

## Satellite Communications (SATCOM)

Instead of communicating with an antenna on the ground, we can communicate with a satellite.

```text
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
```

- **Uplink**: Earth → satellite.
- **Downlink**: Satellite → Earth.

### GEO, MEO, and LEO Satellites

Not all satellites orbit at the same altitude.

#### LEO — Low Earth Orbit

LEO satellites are close to Earth.

```text
        🛰 🛰 🛰
     🛰       🛰
   🛰    🌍     🛰
     🛰       🛰
        🛰 🛰
```

Because they are closer:

- The signal travels a shorter distance.
- Latency is lower.
- Less power is needed.
- Each satellite covers a smaller area.

Therefore, a constellation normally needs many satellites.

#### MEO — Medium Earth Orbit

MEO is between LEO and GEO.

```text
Earth

        LEO
       🛰

          MEO
           🛰

                      GEO
                       🛰
```

One of the best-known uses of MEO is satellite navigation.

GPS satellites orbit at an altitude of around 20,200 km, in medium Earth orbit.

#### GEO — Geostationary Earth Orbit

A GEO satellite orbits Earth in sync with Earth's rotation. From our point of view, it is always in the same place.

```text
             🛰
             |
             |
             |
             🌍
```

These satellites are used for satellite television, telecommunications, internet access, and weather monitoring. One problem with these satellites is latency: the signal has to travel a long distance.

```text
Earth
  ↓
~36,000 km
  ↓
Satellite
  ↓
~36,000 km
  ↓
Earth
```

| Orbit | Meaning | Distance | Latency | Coverage |
| --- | --- | --- | --- | --- |
| **LEO** | Low Earth Orbit | Low | Low | Smaller |
| **MEO** | Medium Earth Orbit | Medium | Medium | Medium |
| **GEO** | Geostationary Earth Orbit | High | High | Very large |

### Starlink Example

When we open `youtube.com` using Starlink internet, for example, the data flow looks like this:

```text
Your Device
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
```

#### 1. The PC Sends the Request

We enter `youtube.com`.

The PC creates the network packets and sends them to the router over Wi-Fi.

```text
Laptop
   ↓ Wi-Fi
Starlink Router
```

#### 2. Router → Starlink Antenna

The router is connected to the Starlink user terminal, the antenna outside.

```text
Laptop
   ↓
Router
   ↓
Starlink Dish
```

This is a **phased-array antenna**. It can electronically steer radio beams towards a satellite without physically moving the antenna. Starlink satellites do the same.

#### 3. Antenna → Satellite

```text
Starlink Dish
      ↑
      │ radio signal
      │
      🛰
Starlink Satellite
```

#### 4. What Does the Satellite Do?

The satellite needs to send the packet to infrastructure connected to the internet.

The usual way is to send it directly to a ground station.

```text
Your Dish
    ↓
Satellite
    ↓
Starlink Gateway
    ↓
Fiber
    ↓
Internet
```

```text
User Terminal → Satellites → Gateway Site → Fiber → Point of Presence → Internet
```

#### 5. The Satellites Can Talk to Each Other

Satellites can have **optical inter-satellite links (ISLs)**, or simply, **space lasers**.

This allows the following path:

```text
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
```

Instead of dish → satellite → ground gateway, we can have dish → satellite → satellite → satellite → ground gateway.

This creates a **mesh network in space**. Starlink indicates that its satellites use optical connections to create a global network capable of redirecting traffic between them.

```text
Satellite A → Satellite B → Satellite C → Gateway
```

#### 6. What Are the Lasers For?

If you are on a boat in the middle of the Atlantic with no Starlink ground station nearby, the traffic can follow this path:

```text
Ship
  ↓
Starlink Dish
  ↓
🛰 Satellite 1
  ↓ laser
🛰 Satellite 2
  ↓ laser
🛰 Satellite 3
  ↓
Gateway in Europe
  ↓
Internet
```

The satellite therefore does not need a ground station nearby. This is one of the main reasons internet access is possible on oceans, in remote areas, and on aeroplanes.

#### 7. When the Traffic Reaches the Gateway

Eventually, the data needs to leave the space network.

```text
🛰
  ↓
Starlink Gateway
```

These stations are connected to terrestrial infrastructure through fiber connections to Starlink's network.

The traffic then arrives at a **point of presence (PoP)**.

```text
Satellite
  ↓
Gateway
  ↓
Fiber
  ↓
Starlink PoP
  ↓
Internet
```
