# Frequency, Amplitude, and Wavelength

[Back to Physics](../README.md)

## Overview

Amplitude, frequency, and wavelength describe important properties of periodic waves, including sound, light, and radio signals.

## 1. Amplitude: Size of the Variation

Amplitude is the maximum departure from an equilibrium or reference value. The unit depends on the quantity being measured.

| Signal | Example Amplitude Unit | Meaning |
| --- | --- | --- |
| Sound pressure | Pascal (Pa) | Pressure variation around ambient pressure |
| Electrical signal | Volt (V) | Voltage variation around a reference |
| Electromagnetic wave | Volt per meter (V/m) | Electric-field strength |

Decibels describe a logarithmic ratio or level relative to a reference; watts measure power. Neither is a universal amplitude unit. Under fixed conditions, wave intensity often scales with the square of amplitude.

## 2. Frequency: Cycles per Second

**Frequency (f)** is measured in **hertz (Hz)**. It describes how often a periodic pattern repeats, not how quickly the wave travels through space.

- For a pure sound tone, frequency is closely related to pitch.
- Radio systems use carrier frequencies and occupy a band of frequencies.
- Carrier frequency alone does not determine data rate. Channel bandwidth, signal quality, modulation, and coding also matter.

## 3. Wavelength: Distance per Cycle

**Wavelength (λ)** is the distance between matching points on successive cycles, such as adjacent crests of a sinusoidal wave.

```text
Wave speed = wavelength × frequency
v = λ × f
λ = v / f
```

At a fixed wave speed, increasing frequency decreases wavelength. In dispersive media, wave speed can depend on frequency, so the medium must also be considered.

## 4. Examples

| Wave | Frequency | Approximate Wavelength | Assumed Speed |
| --- | --- | --- | --- |
| Bass tone in air | 20 Hz | 17.2 m | 343 m/s |
| High-frequency tone in air | 20 kHz | 1.72 cm | 343 m/s |
| Radio wave in air | 2.4 GHz | 12.5 cm | 300,000,000 m/s |
| Radio wave in air | 5 GHz | 6 cm | 300,000,000 m/s |

For visible light in vacuum, red light has a longer wavelength than blue or violet light.

## 5. Connections to Networks

Changing amplitude, phase, or frequency can encode information. A symbol can represent more than one bit, depending on the modulation scheme.

Higher-frequency radio bands often provide different propagation characteristics and available channel widths. However, statements such as “higher frequency always carries more data” or “lower frequency passes through every obstacle” are too broad. Materials, antennas, power, interference, and system design matter.

Increasing signal amplitude can improve reception in some conditions, but it does not guarantee more range or eliminate interference.

## Summary

| Property | Question It Answers |
| --- | --- |
| Amplitude | How large is the variation? |
| Frequency | How often does the pattern repeat? |
| Wavelength | How far apart are matching points in space? |

## Related Notes

- [Radio Waves and Wireless](../Signals-and-Networks/Radio-Waves-and-Wireless.md)
- [Sound and Air Pressure](../Audio/Sound-and-Air-Pressure.md)
