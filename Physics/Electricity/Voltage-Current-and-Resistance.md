# Voltage, Current, and Resistance

[Back to Physics](../README.md)

## 1. The Water-Pipe Analogy

Voltage, current, and resistance describe different electrical quantities. Water flowing through a pipe provides a useful analogy, although it does not explain every aspect of a circuit.

| Quantity | Unit | Meaning | Water Analogy |
| --- | --- | --- | --- |
| Voltage | Volt (V) | Electrical potential difference: energy transferred per unit charge. | Pressure difference. |
| Current | Ampere (A) | Rate of flow of electric charge. | Water flow rate. |
| Resistance | Ohm (Ω) | Opposition to current flow. | A restriction in the pipe. |

### Voltage

A small battery might provide **1.5 V**. A typical European household outlet supplies approximately **230 V AC**, expressed as an RMS value. These are different kinds of supply; voltage alone does not describe their behavior.

### Current

Current measures charge passing a point per second. In a metal wire, electrons carry that charge.

A wire's current-carrying capacity depends on its material, thickness, insulation, and cooling conditions. Excessive current can overheat it.

### Resistance

Resistance relates the voltage across a component to the current through it. For a fixed voltage, increasing resistance reduces current in an ohmic circuit.

## 2. Ohm's Law

For an ohmic component under conditions where resistance remains constant:

```text
V = I × R

V = voltage in volts
I = current in amperes
R = resistance in ohms
```

- Increase voltage while keeping resistance constant → current increases.
- Increase resistance while keeping voltage constant → current decreases.

Not every component has a constant resistance; semiconductor devices can behave differently.

## 3. Electrical Power

For a DC supply:

```text
P = V × I
```

A charger supplying **20 V at 5 A** delivers **100 W**. This is an output operating point, not necessarily its actual output at every moment.

For AC circuits, average real power also depends on the relationship between voltage and current over time.

## 4. Heat and Short Circuits

Electrical resistance converts electrical energy into thermal energy through interactions within the material. This is called **Joule heating**, rather than mechanical friction.

For a resistor:

```text
P = I² × R
```

A short circuit creates an unintended low-resistance path. The resulting current can be very high, limited by the source and the remaining circuit resistance. It can cause overheating or activate a fuse, circuit breaker, or electronic protection.

Computer chips also dissipate energy as their transistors switch and through leakage, which contributes to their cooling requirements.

## Related Notes

- [Power and Energy](Power-and-Energy.md)
- [Heat Transfer](../Heat-and-Cooling/Heat-Transfer.md)
