# External shunts

## Victron Smartshunt

### Hardware connection

In order for the connection to be established from the Smartshunt to the BSC, a corresponding 3.3V compatible converter must be used between the VE.Direct port (UART 3,3V) and the BSC (RS485).
A galvanically separate type is not necessary, since this separation is available at the BSC anyway. The connection takes place via A/B/GND.

#### The plug to be used
Manufacturer: JST
Series: PH
Pole number: 4
Raster size: 2.0mm
Order no.: JST PHR-4

![](../img/devices/devices_shunt_smartshunt_vedirect_stecker.png) {Width = "550"}

#### Certer colors of an original ve.direct cable. (Without guaranteeing information on your cable)

|  Pinnr | Certer color |
| : ------------- | : ------------- |
| 1 | red |
| 2 |  Green |
|  3 |  white |
|  4 | Black |

#### Example of a UART/RS485 converter to be used
![](../img/devices/devices_shunt_smartshunt_rs485_converter.png) {Width = "300"}

It turned out that the Smartshunt cannot supply all types of UART/RS485 converter with electricity.
The converter should no longer absorb like 10mA (pulse max. 20ma/5ms).
Otherwise, an external power supply must be used for the converter!

#### Connecting table

| Smartshunt | Adapter Uart page | Adapter RS485 Page | BSC (Serial 0) |
| ------------ | ------------ | ------------ | ------------ |
| PIN1 (GND) | GND | GND | S0 GND |
| PIN2 (RX) | TXD | A+ | S0 RX/A |
| PIN3 (TX) | RXD | B- | S0 TX/B |
| PIN4 (3V3) | VCC |  |  |

Various, preferably Chinese converter, have the wrong TXD/RXD printing. With these, the two signals must then be connected inverted.

### Settings BSC

#### Definition of the serial interface
Settings -> Interfaces -> Serial -> Selection of the Victron Smartshunt

#### Needed value trading
![](../img/devices/devices_shunt_smartshunt_bsc_settings.png) {Width = "400"}

Settings can be found as follows
- Settings -> Inverter & loading -> General -> ValueHandling Multi -BMS -> SoC
Selection: BMS

- Settings -> Inverter & loading -> General -> Valuehandling Multi -BMS -> BMS for SoC
Selection: Selection of the interface where the Smartshunt is connected.

This only uses the SOC of the Smartshunt and forwarded to the inverter.