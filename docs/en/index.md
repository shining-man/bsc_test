# Battery Safety Controller (BSC)-<br> The flexible controller for DIY batteries
<img src="img/bsc_display.png" width="600">

The **Battery Safety Controller (BSC)** is a freely configurable controller that can be used for a variety of control and monitoring tasks in DIY battery systems. The BSC takes over the central control of the energy-orange system and can act as an additional security level next to the BMS.

## The BSC consists of two components:
1. **BSC hardware** - It acts as middleware between the BMS and the inverter. One advantage of the BSC hardware is your safe operation: all physical interfaces are galvanically isolated.
2. **BSC software**-This makes the BSC hardware a freely configurable controller that can be used for a variety of control and monitoring tasks in DIY battery systems.

## Possibilities of the BSC

### 1. Monitoring of connected devices (serial, bluetooth)
The BSC can send the data of connected devices (BMS, balancers, temperature sensors) to a broker via MQTT to graphically present them (e.g. in Grafana) or continue to process it, e.g. in an automation system such as **Iobroker**, **Nodered** or **Home Assistant**.

### 2. Charging control
The BSC uses the data of the connected devices to control the inverter (Victron, Solis, Deye, etc.) connected via the CAN bus. There are several functions available to adapt the loading control to your own DIY battery system:

- Cell voltage -dependent throttling of the charging current
- Reduction of the charging current in cell deviations
- SOC-dependent reduction in the charging current
- Load shutdown: prevents continuous reloading when the battery is full
- Merging of the data from the individual physical battery packages into a virtual overall battery package, taking into account numerous parameters, e.g. whether the battery package loads or discharges at all.
- And more ...

### 3. Second security level next to the BMS
The BSC can monitor various configurable parameters on the connected devices to create an additional security level. Superior parameters include:

- Regular answer of the connected BMS
- Cell voltages (min/max)
- Entire voltage (min/max)
- Temperatures

This data can be used to control relay outputs, for example, and to trigger a leak can be triggered.

### 4. Temperature monitoring
Up to **64 OneWire temperature sensors** (DS18B20) can be connected and monitored. Different regulations are possible:

- Monitoring of the maximum value
- Monitoring of the minimum value
- Monitoring the maximum value with a sensor as a reference value
- Monitoring of the difference values

All settings can be parameterized flexibly via a web interface.

The **Battery Safety Controller** offers a versatile and customizable solution for monitoring and controlling DIY battery systems. Ideal for demanding applications that require an additional security level and extensive control options.
