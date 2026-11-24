# Radio Waves and Wireless Networking

[Back to Physics](../README.md)

## Overview

Wi-Fi, Bluetooth, and mobile networks carry information using radio-frequency electromagnetic waves. Radio and visible light belong to the same electromagnetic spectrum but occupy different frequency ranges.

Radio waves can travel through a vacuum; air is not required. Their interaction with walls and other obstacles depends on frequency, materials, and geometry.

## 1. From Bits to Radio and Back

1. **Modulation:** The transmitter maps bits to symbols that vary properties such as amplitude and phase. Systems such as Wi-Fi can use many subcarriers.
2. **Transmission:** Changing currents in an antenna produce radiated electromagnetic fields.
3. **Reception:** The incoming field induces a small electrical signal at the receiving antenna.
4. **Demodulation and decoding:** The receiver estimates the transmitted symbols and recovers data, using synchronization and error-control mechanisms.

The recovered bits are not guaranteed to be correct under all conditions; damaged frames may be discarded or retransmitted.

## 2. Wi-Fi Bands

| Band | Typical Considerations |
| --- | --- |
| 2.4 GHz | Often useful for longer reach; shared with many other devices and limited channel space. |
| 5 GHz | More opportunities for wide channels; propagation differs from 2.4 GHz. |
| 6 GHz | Additional spectrum for compatible equipment; availability and operating rules depend on location. |

Wi-Fi 6E extends Wi-Fi 6 operation into 6 GHz. The band is not inherently free from interference, and a higher carrier frequency does not automatically guarantee a higher data rate. See [Cisco's Wi-Fi 6E band documentation](https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9166-series-access-points/220526-configure-and-verify-wi-fi-6e-band-opera.html).

Range and throughput depend on channel width, power, antennas, obstacles, client capability, and competing traffic. No band guarantees that signals pass easily through every wall.

## 3. Attenuation and Obstacles

Radiated energy spreads according to the antenna's pattern; antennas do not necessarily radiate equally in every direction.

Walls and objects can absorb, reflect, or scatter radio energy. Multiple reflected paths can combine constructively or destructively at the receiver.

## 4. Interference and Shared Airtime

Nearby networks and other devices may compete for airtime or interfere with reception. Bluetooth and leakage from microwave ovens can affect the 2.4 GHz band.

Retries and lower selected transmission rates can reduce throughput and increase latency. Channel contention also adds waiting time even when frames are received correctly.

## Related Notes

- [Frequency, Amplitude, and Wavelength](../Waves/Frequency-Amplitude-and-Wavelength.md)
- [Noise, Attenuation, and Interference](Noise-Attenuation-and-Interference.md)
- [Bandwidth and Latency](Bandwidth-and-Latency.md)
