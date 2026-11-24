# Bandwidth and Latency

[Back to Physics](../README.md)

## Overview

A connection's capacity and its delay are different properties. A wider road can carry more vehicles at once, but it does not automatically shorten the journey for one vehicle.

## 1. Latency: Delay

Latency describes delay between defined points in a communication process. It can mean **one-way delay** or **round-trip time (RTT)**, depending on the measurement.

`ping` measures an ICMP request-and-reply round trip. An application's response time can additionally include server processing and other work.

### What Contributes to Delay?

- **Propagation:** Time for the signal to travel through the medium.
- **Transmission:** Time to place the packet's bits onto a link.
- **Queueing:** Time waiting behind other traffic.
- **Processing:** Time spent handling packets or requests.
- **Retransmissions:** Additional delay when communication must be repeated.

Latency matters for gaming, voice calls, and interactive SSH sessions. Variations in delay are often called **jitter**.

## 2. Bandwidth, Throughput, and Goodput

| Term | Meaning |
| --- | --- |
| Link capacity or bandwidth | The supported or allocated data rate, often in Mbps or Gbps. |
| Throughput | The rate actually achieved during a measurement. |
| Goodput | The rate of useful application data, excluding overhead and retransmitted data. |

In signal physics, bandwidth can also mean a **frequency range**, measured in Hz. Frequency bandwidth and data rate are related but are not the same quantity.

Capacity matters when downloading large files, streaming video, or supporting several users. Streaming requirements vary with resolution, codec, frame rate, and service.

## 3. Comparison

| Property | Latency | Data-Rate Capacity |
| --- | --- | --- |
| Typical unit | Milliseconds (ms) | Megabits or gigabits per second |
| Main question | How long does communication take? | How much data can the link carry per second? |
| Common concern | Responsiveness | Transfer speed and simultaneous traffic |

Upgrading to a higher-capacity plan may reduce queueing under load, but it cannot remove the propagation delay to a distant server or fix every wireless problem.

## 4. Linux Example

```bash
ping -c 4 1.1.1.1
```

The `time=` field reports the measured round-trip time to that destination for each reply. It is a sample of that path's behavior, not an exact prediction for every application or server.

## Related Notes

- [Copper and Electrical Signals](Copper-and-Electrical-Signals.md)
- [Fiber Optics and Light](Fiber-Optics-and-Light.md)
- [Radio Waves and Wireless](Radio-Waves-and-Wireless.md)
