# Digital-to-Analog Conversion

[Back to Physics](../README.md)

## Overview

A **digital-to-analog converter (DAC)** turns digital sample values into an analog electrical signal. The DAC may be part of a motherboard audio codec, USB audio device, or wireless headphones.

## 1. From Numbers to an Electrical Output

The DAC interprets each sample according to its digital format and output scale. The relationship between a sample value and a voltage depends on the hardware, reference voltage, gain, and output arrangement.

For an illustrative signed 16-bit system with an approximately ±2 V output range:

| Sample Value | Approximate Signal Voltage |
| --- | --- |
| −32,768 | −2 V |
| 0 | 0 V |
| +16,384 | +1 V |
| +32,767 | Just below +2 V |

These are example signal voltages relative to a reference, not universal voltages at every DAC pin. Some circuits use a DC bias or differential outputs.

Different DAC architectures exist, including resistor-ladder and delta-sigma designs. A bit does not universally correspond to one switch that directly produces the final output voltage. An electrically open switch interrupts a path; a closed switch conducts.

## 2. Reconstructing the Waveform

A simple sample-and-hold model produces a staircase-shaped output. Reconstruction filtering suppresses unwanted high-frequency spectral images while retaining the intended signal band.

Real audio DACs may use interpolation, oversampling, and other internal processing, so their internal switching rate can be much higher than the input sample rate.

The result approximates the intended analog waveform. Quantization, noise, distortion, and filter behavior prevent a blanket claim of perfect reproduction. See [NI's sampling and reconstruction material](https://education.ni.com/teach/resources/1226/sampling-and-reconstruction).

## 3. Amplification and Volume

An amplifier provides the voltage and current needed by the load. A line-level DAC output is not generally designed to drive a large passive speaker directly.

Volume can be adjusted by changing sample values digitally, changing analog gain, or combining both methods. Keyboard volume controls do not necessarily operate only an analog amplifier.

## 4. Where Conversion Happens

| Connection | Typical Playback Path |
| --- | --- |
| Analog headphone jack | Computer's DAC and amplifier → analog cable → headphones |
| USB headphones or USB audio interface | Digital USB data → DAC and amplifier in the connected device |
| Bluetooth headphones | Encoded digital audio over radio → decoding → DAC and amplifier in the headphones |

Bluetooth audio commonly uses a codec; it is not necessarily raw PCM transmitted over the air. Exact hardware and formats depend on the devices.

## 5. From Voltage to Motion

The amplifier drives current through a dynamic speaker's voice coil. The current interacts with the permanent magnet's field, producing force on the coil and diaphragm.

The diaphragm's motion creates pressure variations in the air. It follows the reconstructed audio signal, not a separate push for every bit or sample. Zero voltage at one instant does not imply immediate mechanical rest.

```text
Sample values → reconstructed signal → amplifier
              → voice-coil current → diaphragm motion → sound
```

## Related Notes

- [Digital Audio and PCM](Digital-Audio-and-PCM.md)
- [Speakers and Electromagnetism](Speakers-and-Electromagnetism.md)
- [Voltage, Current, and Resistance](../Electricity/Voltage-Current-and-Resistance.md)
