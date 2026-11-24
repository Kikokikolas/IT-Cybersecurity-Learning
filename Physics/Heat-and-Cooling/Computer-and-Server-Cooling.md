# Computer and Server Cooling

[Back to Physics](../README.md)

## Overview

Computers must transfer heat away from their components. Much of the electrical energy consumed by chips becomes heat through switching activity, leakage, and other losses.

Temperature limits vary by component. A system may reduce performance through **thermal throttling** or shut down if its protection thresholds are reached; there is no universal 95–105 °C limit for every chip.

## 1. Cooling Personal Computers

### Thermal Interface Material

Thermal paste or another interface material fills microscopic gaps between a component and its cooler. It improves thermal contact compared with trapped air.

### Heat Pipes and Vapor Chambers

These sealed devices use evaporation and condensation to move heat. Liquid evaporates near a hot region, vapor moves toward a cooler region, and condensed liquid returns, often through a wick.

Their operation includes phase change and fluid movement, so describing them as ordinary solid conduction is incomplete. Performance depends on design and operating conditions.

### Air and Liquid Cooling

| Method | Heat Path |
| --- | --- |
| Air cooler | Component → heatsink → moving air |
| Liquid cooler | Component → cold plate → coolant → radiator → surrounding air |

A liquid loop's thermal mass can moderate short temperature changes, but sustained heat must still leave the system. Fan size, noise, space, and airflow requirements vary between desktops and laptops.

## 2. Cooling Servers and Data Centers

### Rack Dimensions and Airflow

One rack unit (**1U**) is **44.45 mm** high; **2U** is **88.9 mm**. Thin servers often use compact, fast fans to move air through restrictive passages, but fan sizes and speeds vary by model.

### Hot and Cold Aisles

Racks can be arranged so that fronts face cold aisles and backs face hot aisles. Containment helps reduce mixing between supply and exhaust air.

Supply air may come from raised floors, overhead systems, or other arrangements. Raised-floor cooling is not universal. See [ENERGY STAR on airflow management](https://www.energystar.gov/products/data_center_equipment/optimize-airflow-hvac).

### Direct-to-Chip and Immersion Cooling

- **Direct-to-chip cooling:** Liquid flows through cold plates attached to heat-producing components.
- **Immersion cooling:** Suitable equipment operates in a compatible dielectric fluid.

Liquid cooling can support high heat densities. The appropriate solution depends on the equipment and facility rather than one universal GPU wattage threshold. See the [DOE data-center design guide](https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design_0.pdf).

## 3. Comparison

| Consideration | Personal Computer | Server or Data Center |
| --- | --- | --- |
| Priorities | Comfort, noise, performance, and available space | Reliability, capacity, maintainability, and efficiency |
| Air management | Device enclosure and room conditions | Equipment airflow plus facility-wide heat removal |
| Cooling options | Air coolers, heat pipes, and liquid loops | Air cooling, cold plates, or immersion where appropriate |
| Energy overhead | Fans, pumps, and room cooling where used | Fans, pumps, heat rejection, and facility cooling equipment |

Cooling's share of total energy use varies with design, climate, and workload; it is not a fixed percentage for all facilities.

## Related Notes

- [Heat Transfer](Heat-Transfer.md)
- [Power and Energy](../Electricity/Power-and-Energy.md)
