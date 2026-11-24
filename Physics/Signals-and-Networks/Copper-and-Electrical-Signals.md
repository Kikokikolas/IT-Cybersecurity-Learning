# Copper and Electrical Signals

[Back to Physics](../README.md)

## Overview

Copper carries electrical signals in Ethernet cables, USB cables, and circuit-board traces. Its mobile charge carriers make it a useful conductor.

The signal propagates as an electromagnetic disturbance associated with the conductors and their surroundings. Individual electrons do not race from sender to receiver at the signal's propagation speed.

## 1. Encoding Bits

A transmitter varies electrical signals according to a defined encoding or modulation scheme.

- A simple digital interface might use two voltage ranges for binary values.
- Some encodings use transitions to carry data or timing information.
- Modern Ethernet can use multiple signal levels and complex coding; it is not universally “high voltage = 1, low voltage = 0.”

The receiver measures the arriving signal and recovers the transmitted symbols and bits.

## 2. Physical Limits

| Property | Effect |
| --- | --- |
| Propagation speed | Sets part of the minimum delay over distance; depends on cable construction. |
| Frequency response | Limits which signal components can be carried reliably. |
| Attenuation | Reduces signal strength through conductor and dielectric losses. |
| Crosstalk | Couples unwanted energy between circuits or pairs. |
| Impedance discontinuities | Cause reflections that can distort the signal. |

For many common twisted-pair Ethernet standards, the specified channel length is **100 m**. This is a system-design limit, not a point where all electrical signals suddenly disappear. Other copper technologies have different limits.

Cable frequency ratings in MHz are not the same as Ethernet data rates in Mbps or Gbps.

## 3. Why Twisted Pairs Help

A common four-pair Ethernet cable has eight conductors arranged into four twisted pairs.

### Differential Signaling

The receiver responds mainly to the **voltage difference** between the two conductors in a pair.

### Noise Rejection

Twisting helps both conductors experience similar external interference. A differential receiver rejects much of this common-mode noise, although rejection is not perfect. Pair balance, termination quality, and installation matter.

## 4. Copper and Fiber

Copper uses electrical signaling; fiber guides optical signals. Fiber avoids electromagnetic pickup along the glass, but both media have losses and practical operating limits.

## Related Notes

- [Fiber Optics and Light](Fiber-Optics-and-Light.md)
- [Noise, Attenuation, and Interference](Noise-Attenuation-and-Interference.md)
