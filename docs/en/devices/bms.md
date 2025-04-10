# Supported BMS
In this section you will find an overview of the supported Battery Management Systems (BMS). The table contains important information about the addresses required for the configuration.
For a correct configuration, the addresses of the BMS and DDM (Data Device mapping) are given in the corresponding fields. These addresses are by one / separated.

- **Address Singlepack**: Diese Adresse ist diejenige, die sowohl am BMS als auch im Device-Data-Mapping eingestellt werden muss. Sie repräsentiert die spezifische Adresse für ein einzelnes BMS in einem System.

- **Address Multipack**: This address is the start address, which is configured on the BMS and in Device-Data mapping. It indicates the address of the first BMS in a multipack system. Other BMS in the chain automatically receive continuous addresses based on this start address.

## Serial BMS
| Type | HW version | SW version | Address Singlepack <br> BMS / BSC | Address Multipack <br> BMS / BSC | Connection BMS |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| **Jiabaida/JBD** |
| JBD-DP24S002 |  |  | - | - |
| **JK Smart BMS** |
| JK-B2A20S20P | V11.XW | 11.25h | - | - |
| JK-B2A24S20P | V10.XW | V10.09 | - | - |
| **JK inverter-BMS** |
| [JK-PB1A16S15P](#jk-inverter) | V14 | V14.20 | 1/1 | 1/1 |
| [JK-PB1A16S15P](#jk-inverter) | V15 | V15.17 | 1/1 | 1/1 |
| [JK-PB2A16S20P](#jk-inverter) | V15 | V15.17 | 1/1 | 1/1 |
| **Seplos** |
| [Seplos](#seplos) | 10c |  | 0/0 | 1/1 |
| [Seplos](#seplos) | 10e | 16.4 | 0/0 | 1/1 |
| Seplos V3 |  |  | ? | ? |
| **Sylcin (e.g. Taico Akku)** |
| [Sylcin](#sylcin) |  |  | 0/1 | 0/1 |
| **Gobel** |
| GP-SR1-RN150 |  | | ? | ? |
| [GP-SR1-PC200](#pace-pc200) |  | |  2/2 | 2/2 | RS485B |

## Bluetooth devices
| Type | HW version | SW version |
| ------------ | ------------ | ------------ |
| Neey |
| Neey Balancer 4a | 2.8.0 | 1.2.1 |
| Neey Balancer 4a | 2.8.0 | 1.2.3 |

Here is the dissolution of the status reports of the NEEY:

![](../img/devices/devices_neey_status.png) {Width = "520"}


## Conclusion examples

### Seplos

The BSC supports the integration of a single SEPLOS BMS and several SEPLOS BMS, which can be switched in parallel in a Daisy Chain configuration. In both cases, only a single serial connection to the BSC is required.

#### Conditions / tips for a multipack daisy-chain network:
* In the seplos software, the automatic addressing is deactivated (upload parameter -> on the right side all down)
* The DIP Switch are to be switched to RS485 configuration
* Connecting the BMS to any serial port of the BSC
Note: [JP6](../hardware.md#j6-fur-den-regularen-betrieb) must be closed.
* If there is a problem in a network with suddenly no longer answering Seplos-BMS, the firmware can help 16.06.04 (or possibly more recent). With the partially occurring problem, the BMS no longer allow a serial connection, which can only be remedied with a BMS reboot.

#### Connection options shown graphically

**When contacting via the RJ45 connection, [dieser](../hardware.md#j6-fur-den-regularen-betrieb) jumper must be set.**

![](../img/devices/devices_seplos_config_single.png)

![](../img/devices/devices_seplos_config_multi.png)

#### Special features

##### Assignment of the temperature sensors in MQTT

| Datentopic | Sensorname |
| : ------------- | : ------------- |
| 0-3 | External cable sensors |
| 4 | Mosfet |
| 5 | Environment |

##### Error handling
- A BSC warning is a "warning" or an "alarm" in the Seplos BMS
- A BSC alarm is a "Protection" in the Seplos BMS

#### Further information
[Anleitung Firmware Update](../files/SEPLOS_BatteryMonitor_Firmware_updating_Guide.pdf)
[FAQ Sammlung](https://akkudoktor.net/t/seplos-bms-faq-sammlung/8843) (battery doctor)

### Sylcin

Connection of several batteries via Serial 2 from the BSC is possible.

* Adjust the addressing 1 up (without gaps) via the dip switches. Please note that 0000 = address 1, 0001 = address 2 is!
* Connect BSC to the RS485-1 (not RS485-2) interface.
* Each additional battery must also be clamped in parallel to the respective RS485-1.
* PIN 4 and 5 is always used in the RS485-1.
* At the RS485 at the beginning and end of the bus, schedule resistance with a 120Ohm.
* If you contact the RJ45 connection, [dieser](../hardware.md#j6-fur-den-regularen-betrieb) Jumper must be set
* Setting the Sylcin BMS under Serial 2
* Define the number of packs in the settings (see images Seplos BMS)

After that, every pack can be found in the BSC. Battery 1 -> BMS (2), battery 2 -> BMS (3), ...

### JK inverter

The JK Inverter BMS can be connected to the BSC with a commercially available RJ45 patch cable.
This BSC port is named "Serial 2" in the software. JP6 must be closed to use this interface.
Individual BMS, as well as a multipack configuration via Daisychain, is possible.

#### Setting for Daisychain in the JK app
* In the case of a daisychain network, the UART protocol must be converted to protocol 1 (JK BMS RS485 Modbus V1.0) on all BMsen.

#### addressing
The BSC takes on the role of the master, so the DIP address 0 must no longer be assigned to a BMS.
Each pack gets its own ID, which can be defined via the DIP switches. No address may be awarded twice.

#### Physical connection

![grafik](../img/devices/devices_sylcin_config_multi.png)

##### Single pack configuration
* The JK BMS is connected to the BSC with a patch cable by a right RJ45 connection.

##### Multipack configuration as a series connected in series
* Connect all battery packs via the right RJ45 sockets in series
* Connect the BSC with a patch cable to one of the free right RJ45 connections of the JK-BMS

#### Configure RS485 data transmission (BMS) in the BSC software
* For direct connection via Serial2: In the BSC under Settings -> Interfaces -> Serial2 Select the "JK inverter BMS", since only one interface for several packs has to be used in the Daisychain network.
* The device mapping configuration of the connected devices is explained [hier](../settings_bsc.md/#data-device-mapping)
* After that, each pack in the BSC should be found under the live data -> BMS data.

#### CAN data transmission (inverter) configure
For the transfer of the data via CAN to e.g. a Victron Cerbogx, you must make the following settings under "Settings -> Inverter & Dadge Regulation -> General":
 1. Select BMS Canbus Enable
 2. Select CAN protocol e.g. Victron
 3. Now define the "data source (master)" to Serial 2
 4. Under "ValueHandling Multi-BMS" determine how the SoC is to be transferred / calculated. "Average", for example, hands the average over all connected BMS.
 5. Select data source (Master) (for example, the temperature refers to Victron under the point "Battery Temperature", the max and min temperatures across all packs, remain unaffected) and select another serial interface for each additional BMS under "+data source".

![](../img/settings/settings_inverter_datquelle.png) {Width = "550"}

#### Special features
##### Assignment of the temperature sensors

The JK-Inverter BMS has four connectable temperature sensors. These are assigned to the BSC software as follows:

| BSC ID | BMS
| ------------ | ------------ |
| 0 | T1 |
| 1 | T2 |
| 2 | MOS |
| 3 | T4 |
| 4 | T5 |

From V0.7.2_T4:

| BSC ID | BMS
| ------------ | ------------ |
| 0 | MOS |
| 1 | T1 |
| 2 | T2 |
| 3 | T4 |
| 4 | T5 |

### Pace PC200

The Pace PC200 BMS is installed in the GP-SR1-PC200 battery packs sold by Gobel Power, for example.
The BSC supports the individual pack here, as well as the connection of several packs than Daisychain network. In both cases, only a single serial connection to the BSC is required.
A commercially available RJ45 cable can be used as cabling to the BSC. The port on the battery pack can be seen in the following pictures and marked with RS485-B on the pack.
The respective interface is to be defined under the serial port settings, as well as in deviceapping.

#### Single pack configuration

In the case of a single-pack configuration, the BSC acts as a master (address 1), so the connected battery pack is assigned to the address 2 via Dipswitch.

![](../img/devices/devices_Pace_PC200-Singlepack.png)

#### Multi-pack configuration

Even with a multi-pack configuration, the BSC acts as a master (address 1).
The other connected packs receive the addresses 2 and the following.

![](../img/devices/devices_Pace_PC200-Multipack.png)
