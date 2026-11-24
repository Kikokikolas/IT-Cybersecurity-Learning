# Digital Audio and PCM

[Back to Physics](../README.md)

## Overview

**PCM (pulse-code modulation)** represents an audio signal as a sequence of numerical samples. It is widely used for uncompressed digital audio, including audio handled by systems such as PipeWire.

Recording an analog signal involves **sampling** and **quantization**. Games and synthesizers can also generate samples directly in software.

## 1. Sampling: Measuring Over Time

The **sample rate** specifies how many samples are recorded each second **per channel**.

| Sample Rate | Samples per Second per Channel | Common Use |
| --- | --- | --- |
| 44.1 kHz | 44,100 | Audio CDs and music |
| 48 kHz | 48,000 | Video, games, and many audio-system configurations |

PipeWire settings can vary; 48 kHz is not a universal requirement.

For an ideally band-limited signal, the sampling rate must exceed twice its highest frequency to avoid aliasing. Real recording systems use anti-aliasing filters and leave room for their transition bands. See [NI on sampling and reconstruction](https://www.ni.com/en/shop/electronic-test-instrumentation/oscilloscopes/using-a-digitizer-for-time-domain-measurements.html).

**Sample rate is not sound frequency.** A 1 kHz tone sampled at 48 kHz has 48 samples per cycle. The speaker does not vibrate at 48 kHz merely because the sample rate is 48 kHz.

## 2. Quantization: Representing Amplitude

Quantization maps each sample to one of a finite set of values. A signed 16-bit integer sample has 65,536 possible values, from **−32,768 to +32,767**.

| Example Value | 16-Bit Binary Representation |
| --- | --- |
| 0 | `00000000 00000000` |
| +16,384 | `01000000 00000000` |
| +32,767 | `01111111 11111111` |
| −32,768 | `10000000 00000000` |

A sequence of zero-valued signed PCM samples represents digital silence. One zero-valued sample can simply be a waveform crossing zero. Other formats include 24-bit integers and floating-point samples.

## 3. How Much Data Is Needed?

For uncompressed 16-bit audio at 48 kHz:

```text
Mono:   48,000 × 16 × 1 =   768,000 bits/s
Stereo: 48,000 × 16 × 2 = 1,536,000 bits/s
```

These rates exclude file headers and transport overhead. Compressed audio uses a different bitrate; decoding produces samples for playback.

## 4. Frequency, Sound Level, and Hearing

- **Frequency**, measured in hertz (Hz), relates to pitch. Roughly 20 Hz to 20 kHz is a conventional range for young human hearing; individual limits vary.
- **Sound pressure level**, expressed in dB SPL, is a logarithmic measure relative to a reference pressure. It is related to perceived loudness but is not identical to it.
- **0 dB SPL is not complete silence.** Digital dBFS uses a different reference: 0 dBFS represents full scale.
- Hearing damage does not begin only at the pain threshold; exposure duration and level both matter. See [NIDCD on noise-induced hearing loss](https://www.nidcd.nih.gov/health/noise-induced-hearing-loss).

## Playback Path

```text
PCM samples → DAC → amplifier → speaker motion → air-pressure waves
```

## Related Notes

- [Digital-to-Analog Conversion](Digital-to-Analog-Conversion.md)
- [Sound and Air Pressure](Sound-and-Air-Pressure.md)
