# Noise, Attenuation, and Interference

[Back to Physics](../README.md)

## Overview

A communication system must recover information from a signal that changes as it travels. Attenuation, noise, interference, distortion, and dispersion can all make reception harder.

## 1. Attenuation: Reduced Signal Strength

Attenuation is the reduction in signal level along a path, often expressed in decibels.

| Medium | Examples of Loss Mechanisms |
| --- | --- |
| Copper | Conductor and dielectric losses. |
| Optical fiber | Absorption, scattering, bends, and connector losses. |
| Wireless | Spreading of radiated energy and absorption by obstacles. |

Loss accumulates rather than appearing suddenly at one universal distance. A link works only while the received signal remains adequate for its receiver and signaling scheme.

## 2. Noise and Interference

**Noise** includes unwanted fluctuations generated within devices or received from the environment. **Interference** commonly refers to unwanted signals from other sources.

Examples include electrical pickup from motors, crosstalk between cable pairs, and competing radio transmissions.

Fiber does not pick up electromagnetic interference in the way copper does. However, optical systems still have receiver noise, optical noise, losses, and other impairments. See [HPE Juniper's optical-loss and dispersion explanation](https://networkingdocs.hpe.com/documentation/us/en/hardware/mx960/acx1000/topics/concept/fiber-optic-cable-signal-loss-attenuation-dispersion-understanding.html).

## 3. Signal Quality and Network Behavior

The **signal-to-noise ratio (SNR)** compares desired signal power with noise power. Interference may be included separately in a signal-to-interference-plus-noise ratio (SINR).

Poor reception can lead to errors, retransmissions, lower selected data rates, and disconnections. Retransmissions can reduce useful throughput and increase delay.

## 4. Engineering Responses

| Technique | Purpose |
| --- | --- |
| Twisted pairs and differential signaling | Reduce sensitivity to common-mode pickup. |
| Shielding and suitable routing | Reduce unwanted coupling. |
| Optical fiber | Avoid electrical pickup along the optical path. |
| Amplification or regeneration | Extend reach, with different effects on noise and signal recovery. |
| Error correction | Recover some corrupted data without retransmission. |
| Channel planning | Reduce interference and contention in wireless systems. |

These techniques do not solve every limitation. Network engineering also addresses timing, impedance, dispersion, capacity, and reliability.

## Related Notes

- [Copper and Electrical Signals](Copper-and-Electrical-Signals.md)
- [Radio Waves and Wireless](Radio-Waves-and-Wireless.md)
