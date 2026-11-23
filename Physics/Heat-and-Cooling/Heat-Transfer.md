# Heat Transfer

Heat transfer is the movement of thermal energy caused by a temperature difference. Spontaneous net heat transfer is from a warmer region to a cooler one. In an isolated system, this tends toward **thermal equilibrium**, where the temperatures are equal.

A running computer continuously generates heat, so its components can remain warmer than the surrounding air even while cooling works correctly.

The three main mechanisms are **conduction**, **convection**, and **radiation**. See the [OpenStax introduction to heat transfer](https://openstax.org/books/physics/pages/11-2-heat-specific-heat-and-heat-transfer).

## 1. Conduction: Transfer Through Matter

Conduction transfers thermal energy through matter without bulk movement of the material. In solids, atomic vibrations transfer energy between neighboring regions; mobile electrons also make an important contribution in metals. Conduction can also occur in liquids and gases.

**Everyday example:** A metal spoon left in hot tea gradually becomes warmer, including its handle.

**In computers:** Heat travels from the processor through its thermal interface material into the heatsink. Copper and aluminum are common heatsink materials because they conduct heat well. Air and many plastics are relatively poor thermal conductors.

```text
Processor → thermal interface material → heatsink base → heatsink fins
```

Thermal paste improves contact by filling microscopic gaps that would otherwise contain air. It is not a replacement for the heatsink.

## 2. Convection: Transfer by Moving Air or Liquid

Convection transfers heat through the movement of a fluid, such as air or a liquid coolant.

### Natural Convection

When warmer fluid becomes less dense than the surrounding fluid, buoyancy can make it rise while cooler fluid moves in to replace it. This creates circulation.

**Everyday example:** Warm air rises above a room radiator.

### Forced Convection

A fan or pump drives the fluid's movement.

**In PCs and servers:** Fans move air across heatsink fins, while pumps circulate coolant through a liquid-cooling loop. Moving cooler fluid past a warm surface generally increases heat transfer compared with leaving the fluid still.

A liquid cooler carries heat from the processor's cooling block to a radiator, where it is transferred to the surrounding air.

## 3. Radiation: Transfer by Electromagnetic Waves

Thermal radiation requires no material medium and can travel through a vacuum. Every object above absolute zero emits thermal radiation. Net radiative heat transfer depends on both emission and absorption.

**Everyday examples:** Sunlight warms the Earth across space, and a campfire can warm your face without hot air blowing toward you.

At typical computer-component temperatures, thermal emission is mainly infrared. Solar radiation also includes substantial visible light, so thermal radiation is not exclusively infrared. See [OpenStax on radiation](https://openstax.org/books/college-physics/pages/14-7-radiation).

**In computers:** Hot components, including GPUs and motherboard voltage regulator modules (VRMs), emit infrared radiation. In typical actively cooled PCs, conduction and convection carry most of the heat away. Thermal cameras detect infrared radiation from visible surfaces to estimate their temperatures.

## A PC's Cooling Cycle

| Mechanism | How Heat Travels | Example in a PC |
| --- | --- | --- |
| Conduction | Through matter without bulk movement | Processor → thermal paste → heatsink base and fins |
| Convection | Through moving air or liquid | Air flowing across fins, or coolant circulating through a cooling loop |
| Radiation | Through electromagnetic waves | Warm component surfaces emitting infrared radiation |

These mechanisms operate together: heat can conduct through a heatsink, transfer to moving air by convection, and radiate from the heatsink's surface at the same time.
