# Fiber Optics and Light

[Back to Physics](../README.md)

## Overview

Optical fiber guides light through a thin glass or plastic core. A transmitter modulates light, and a receiver converts the arriving optical signal into an electrical signal.

Turning light on and off is one simple signaling model. More advanced systems can encode information using multiple amplitude levels, phase, polarization, or wavelengths.

## 1. How Light Is Guided

| Layer | Purpose |
| --- | --- |
| Core | Guides the optical field. |
| Cladding | Has a lower refractive index than the core, supporting confinement. |
| Coating, buffer, and jacket | Protect the fiber mechanically; construction varies by cable. |

Total internal reflection provides a useful ray-model explanation when the necessary refractive-index and angle conditions are met. Sharp bends can still cause loss; the fiber is not a perfect mirror under every condition.

## 2. Multimode and Single-Mode Fiber

| Type | Characteristics | Common Applications |
| --- | --- | --- |
| Multimode | Common core diameters include 50 and 62.5 µm; multiple propagation modes can broaden pulses. | Building and data-center links. |
| Single-mode | A much smaller core supports one spatial mode at its operating wavelengths. | Long-distance and high-capacity links. |

Modern high-speed multimode links commonly use VCSEL lasers, not only LEDs. Single-mode fiber avoids modal dispersion but still has attenuation and other forms of dispersion. Reach depends on the fiber, wavelength, transmitter, receiver, and link budget. See [the Fiber Optic Association's fiber reference](https://www.foa.org/tech/ref/basic/fiber.html).

## 3. Comparison with Copper

| Property | Copper | Optical Fiber |
| --- | --- | --- |
| Signal | Electrical | Optical |
| Electromagnetic pickup | Can affect the signal | Glass transmission path does not pick up electrical interference |
| Reach | Depends on the interface and cable | Can support long links with suitable optics |
| Loss | Conductor and dielectric losses | Absorption, scattering, bends, and connection losses |
| Confidentiality | Requires appropriate protection | Also requires appropriate protection |

Fiber is **not impossible to tap**. Physical access can allow interception, so optical transmission is not a substitute for encryption. See [research on optical-fiber tapping](https://www.mdpi.com/2304-6732/13/10/964).

## 4. Speed and Capacity

Light travels at roughly **200,000 km/s in typical glass fiber**, compared with about 300,000 km/s in vacuum. Cable signal speeds depend on the medium and construction.

Fiber's advantages include low attenuation and high achievable capacity. Long-haul and submarine systems may use optical amplifiers or repeaters; they are not lossless paths across an ocean.

## Related Notes

- [Bandwidth and Latency](Bandwidth-and-Latency.md)
- [Noise, Attenuation, and Interference](Noise-Attenuation-and-Interference.md)
