# Power and Energy in Computers

[Back to Physics](../README.md)

## 1. Power: The Rate of Energy Transfer

**Power**, measured in **watts (W)**, describes how quickly energy is transferred or consumed. A computer's power draw changes with its workload: an idle desktop usually draws less power than one rendering a 3D scene.

### Power Supply Unit (PSU)

A desktop PSU has a rated output capacity, such as **650 W**, **850 W**, or **1,000 W**. It needs to support the components' combined demand, including brief transient loads.

A 750 W rating does not mean that the computer constantly consumes 750 W. Power drawn from the wall also includes conversion losses in the PSU.

### Thermal Design Power (TDP)

TDP is a thermal-design reference expressed in watts. Its definition depends on the manufacturer and product; it should not automatically be treated as an absolute maximum power draw.

For example, Intel distinguishes processor base power from maximum power dissipation in its [thermal and power specifications](https://edc.intel.com/content/www/tw/zh/design/products/platforms/details/raptor-lake-s/13th-generation-core-processors-datasheet-volume-1-of-2/015/processor-line-thermal-and-power-specifications/).

### Power Delivery and Limits

Laptops are constrained by their chargers, batteries, internal power circuits, and cooling systems. USB Power Delivery supports up to **240 W** with compatible equipment; the actual power depends on the charger, cable, and device. See the [USB-IF specification announcement](https://www.usb.org/node/2252).

Desktop components also have electrical and thermal limits, even though the system is connected to a wall outlet.

## 2. Energy: Consumption Over Time

**Energy** measures the total amount transferred or stored. For constant or average power:

```text
Energy = power × time
E = P × t

1 kWh = 1,000 Wh
```

### Battery Capacity and Runtime

Battery capacity is commonly expressed in **watt-hours (Wh)**.

For an idealized 60 Wh battery:

| Average Power Draw | Estimated Runtime |
| --- | --- |
| 10 W | 60 Wh ÷ 10 W = 6 hours |
| 60 W | 60 Wh ÷ 60 W = 1 hour |

Actual runtime depends on usable capacity, battery condition, conversion losses, and changing workloads.

For air travel, 100 Wh is not a universal hard limit. Under FAA guidance, batteries above 100 Wh and up to 160 Wh may be permitted with airline approval, subject to applicable conditions. See the [FAA battery guidance](https://www.faa.gov/hazmat/packsafe/airline-passengers-and-batteries).

### Electricity Consumption and Cost

| Example | Calculation | Energy Used |
| --- | --- | --- |
| Gaming PC averaging 400 W for 5 hours | 0.4 kW × 5 h | 2 kWh |
| Idle PC averaging 40 W for 24 hours | 0.04 kW × 24 h | 0.96 kWh |

Multiply energy use in kWh by the price per kWh to estimate the energy charge, excluding fixed charges and other billing items.

### Data Centers

Data centers track both instantaneous demand and energy consumption over time. Useful measures include energy per completed task and performance per watt. Cooling and power-conversion equipment also contribute to total consumption.

## 3. Charging and Discharging

### Charging: Storing Energy

A charger supplies power. Part of that power can run the laptop, while the remainder can charge its battery, which stores energy chemically.

A higher-rated charger does not automatically charge a battery faster. The laptop's supported input, charging controls, temperature, and battery state also affect the charging rate.

### Discharging: Using Stored Energy

When unplugged, the screen, processor, fans, and other components draw energy from the battery. A light workload usually drains it more slowly than a demanding game.

### When the Charger Cannot Meet Demand

If a laptop needs 60 W but receives only 45 W from its charger, it may draw the shortfall from its battery. Some laptops instead reduce performance or otherwise limit consumption. Behavior depends on the device.

## Comparison

| Metric | Power | Energy |
| --- | --- | --- |
| Meaning | Rate of energy transfer | Total amount transferred or stored |
| Common units | W, kW | Wh, kWh |
| Hardware examples | PSU or charger output rating | Battery capacity |
| Practical use | Assess demand and supply capability | Estimate runtime and consumption |

## Related Notes

- [Voltage, Current, and Resistance](Voltage-Current-and-Resistance.md)
- [Heat Transfer](../Heat-and-Cooling/Heat-Transfer.md)
