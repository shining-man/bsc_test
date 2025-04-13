## Fundamental
It is not recommended to use the following building instructions for productive use.
This guide represents a test platform for temporary use to view the project scope.
Third manufacturers can lead to stability problems with the boards used.
The original hardware has been tested, designed and, above all, galvanically separated, which is a very important aspect, especially with negative BMS types.

## Problems with negative BMS
There are some BMS manufacturers that separate the negative power path when triggered.
If in this error another GND branch via e.g. "BMS -> RS485 -> BSC -> Inverter", the electricity is guided over these fine wires and you are faced with a cable fire!
The inverter will not notice this at first and tries to continue to pull its electricity out of the battery!
Therefore, make sure to use galvanically separate modules for such BMS types.

## Hardware modules
All modules must be able to deal with a 3.3V level of the microcontroller and also be supplied from there.

### The heart of the whole - the ESP32 microcontroller

#### Module
An ESP32 DEV kit can be used for the first time.
Nodemcus from various manufacturers with an ESP32-DowX (e.g. ESP-Wroom-32) chipset such as "Berrybase NMCU-ESP32" are compatible.

#### Power supply
The power supply to the nodemcus is unfortunately sparsely positioned and can lead to an unstable state of the system.
There are two things to consider to help the boards:
1. Direct connection this with a high -quality 3.3V /> = 1.5A power supply to the 3.3V and GND PIN
2. In addition, different sizes between these pins are useful - e.g. Kerko: 220nf & Elkos: 22Uf, 470UF

#### Module connection criteria
It should be noted that depending on the connection of external hardware, suitable level converter can be used!
-> From an ESP32, a uart with 3.3V level - no RS485! This may destroy the controller or target hardware.

#### Gpios
The data connection of the communication modules is shown in the following table.
A seplos BMS should be connected to the Serial2.

Interface | RX | Tx
-------- | -------- | ---------
**Serial 0** | GPIO 16 | GPIO 17
**Serial 1** | GPIO 23 | GPIO 25
**Serial 2** | GPIO 35 | GPIO 33
**Can** | GPIO 5 | GPIO 4

### RS485 converter
A galvanically separate and tested RS485 adapter is, for example.
To have different sources.
Including is three -wheeled (A / B / GND).

![](img/bsc_ohne_org_hw_rs485_converter.jpg) {Width = "450"}

### CAN converter
For example, the following has been working reliably for the CAN interface in a prototype.
To have different sources.
Including is three -wheeled (Canh / Canl / GND).

![](img/bsc_ohne_org_hw_can_converter.jpg) {Width = "450"}