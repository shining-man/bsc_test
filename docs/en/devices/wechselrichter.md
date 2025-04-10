

## Victron MP2 48/5000/70
**Other types of the inverter can probably be connected in the same style.**

### Physical connection of the components

* Victron internal cabling
MP2 <-> MK3-USB adapter <-> VENUSOS (e.g. Cerbogx, Raspberrypi + Can-Shield)

* Connection of the BSC
BSC (CAN connection) <-> Cerbogx / Raspberrypi + Can-Shield

### CAN connection

Please make sure that the RJ45 final resistance included in Victron is set at the end of the connection, mostly the Cerbo.

* H on h
* L on l
* GND on GND

| Can | [Victron VE.Can Port](https://www.victronenergy.com/live/battery_compatibility:can-bus_bms-cable) |
| --- | --- |
| CAN-GND | PIN 3 |
| CAN-L | PIN 8 |
| CAN-H | PIN 7 |

### Settings BSC
Settings -> inverter & loading (inverter) -> General
![image](../img/devices/devices_inverter_canbus.png)

The "Send Extended Data" option only has a function in conjunction with the [dbus-bsc-can](https://github.com/shining-man/dbus-bsc-can).

In conjunction with a Cerbogx, the option **unspecific** is because this hardware has too little performance and problems can result.
The problems may be that in rare cases, a SoC of 0% for approx. 30s is transmitted in rare cases!

### Venusos settings
Menu -> Settings -> Services -> Can [0.1.2,3, ...] -> Can bus profiles
![image](../img/devices/devices_inverter_venus_canbus.png)

Network status if everything works
![image](../img/devices/devices_inverter_venus_canbus2.png)

Everything is recognized
![image](../img/devices/devices_inverter_venus_canbus_devicelist.png)

### BSC Log edition when Inverter has been recognized
![image](../img/devices/devices_inverter_can_log.png)

### Known special features
#### The battery is unloaded into the network
The SoC reaches 100% and is discharged again when switching to the Float voltage.
Reason: This is one of the **BSC independent behavior**. If the option "DC PV feed-in from excess" is activated in the Victron settings with ESS, the Victron System tries to lower the voltage by unloading to the Float voltage.
~~ Remedy: For example, lower the voltage difference between float and absorption volume to 0.4V. In order to prevent constant charging and unloading over the day, the setting for "float charging voltage SoC" should not be set too high in the BSC, otherwise the absorption will change excitement and the process begins from the front. ~~

#### The charging current limit (CCL) is ignored
If the BSC changes from absorption to Float-Voltage, the charging current limit is set to 0A. The Victron System ignores this setting under certain circumstances.
Reason: If the option "DC PV feed-in from excess" is activated with ESS, the DVCC system does not apply the DVCC charging current limit from the PV system to the battery. This behavior is necessary to enable export. There are still limit values ​​for charging voltage.
Source: [Victron](https://www.victronenergy.com/media/pg/CCGX/de/dvcc---distributed-voltage-and-current-control.html#UUID-0cda63b2-c80b-e81b-e174-f6a91ca5f848)


## Growatt SPF5000es
Connection is via CAN bus.
As a CAN protocol in the BSC, the Pylontech protocol must be defined (Deye ...).
The "Send extend data" checkbox does not have to be activated.

Protocol setting on Inverter via PRG 005: "Li".
Then confirm and define in the following PRG 36: "L52".

Now the SOC etc. should be available.

![Growatt](../img/devices/devices_inverter_growatt_spf5000es.jpg)


##  Goodwe GW5048es
Connection BSC <> Inverter via CAN bus

Canbus Inverter protocol in the BSC: "Deye"

Battery setting on the inverter: "Goodwe 3x Secu-A5.4l"
A protocol setting on the inverter is not necessary.

BMS:
2x seplos V2 configured on pylontech protocol.
Connected to BSC via Serial2 interface.


## Solis S5-EH1P & RHI 5G

#### CAN connection
* H on h
* L on l
* GND does not exist in solos

Occupation CAN connection Solis

| Signal | Connection | Ader color RJ45 (T568A) |
| ------------- | ------------- | ------------- |
| CAN-L | PIN 5 | Blue/white |
| CAN-H | PIN 4 | Blue |
| CAN-GND | ?  | ? |

#### Settings BSC
Settings -> inverter & loading (inverter) -> General
Canbus -> Select Solis Rhi -> Save
BMS CANBUS ENABLE -> Active -> Save

#### Solis settings
Advanced Settings -> Storage Energy Set -> Battery Select -> Battery Module -> Select Pylon

## Deye Sun-12k-SG04LP3-EU

#### CAN connection
The connection BSC <> inverter (CAN bus) takes place via the "BMS Port" of the inverter (see Manual page 10).
This port is connected to a commercially available network cable. Three individual veins of this cable must be connected to the CAN interface, to be found on the screw terminals of the BSC.

* CAN-H on CAN-H
* CAN-L on CAN-L
* GND on GND

| Signal | RJ45 connection | Ader color RJ45 (T568A) |
| ------------- | ------------- | ------------- |
| CAN-H | PIN 4 | Blue |
| CAN-L | PIN 5 | White/blue |
| CAN-GND | PIN 6 | Orange |


![](../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu.png) {Width = "450"}

#### Setting on the inverter
"Bat Set 1: Batt Mode" Lithium ", asked Set 3:" Lithium Mode 00 "
![SystemSetup](../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings1.png)
![BatterySettings](../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings2.png)
![BatterySettings3](../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings3.png)

#### Settings in the BSC
Settings -> inverter & loading -> General
BMS Canbus Enable
Canbus Protocol: "Pylontech"
Data source (Master): "Serial 2"
