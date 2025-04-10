## Hardware requirements
In order to be able to use all functions of the firmware, the hardware belonging to the BSC system is required. A detailed description of this hardware, including the [Stromlaufplans](https://github.com/shining-man/bsc_hw/blob/main/circuit.pdf?raw=true), can be found in a separate [GitHub-Repository](https://github.com/shining-man/bsc_hw).

We expressly recommend the use of the original BSC hardware. This has been extensively tested and offers separate connections galvanically, which ensures more stable operation.

If the original BSC hardware is not available, you can alternatively use an ESP32 DEV kit for first tests. However, note that some functions may be restricted or not tested. You can find more information under the following [Link](BSC_ohne_orig_hardware.md).

## Connections
A tech talk about the connection options can be viewed on [Youtube](https://youtu.be/zwu_jJifkF4?si=2ktcM57JjkR39Dph).

**Correct contact of the screw terminals:**
To ensure error -free installation, please note the following information on connecting the screw terminals:

  1. **Marking of PIN 1:**
Each screw clamp is marked with a number "1" that specifies PIN 1 of the respective clamp. This marking serves as a reference for the correct connection.

  2. **Labeling the functions:**
In addition to the marking of PIN 1, there is a lettering that describes the respective function of the individual contact points. Read this carefully to make the right connections.

  3. **Important safety instructions:**
Be sure to make the connections correctly!
Incorrect connections can cause damage to the BSC or components connected to externally.

  4. **Illustrations and practical information:**
The illustrations contained in this documentation only serve to illustrate. Therefore, always check the markings and labels on your board to ensure the correct connections.

![](img/hardware/hw_stecker_9pol.png) {Width = "300"}
![](img/hardware/hw_stecker_6pol.png) {Width = "300"}

## Power supply
The pins to be used can be found as "V In1" for "+" and GND for "-" printed on your PCB. The operation of the BSC hardware is designed in the standard delivery for 5V (> = 1.5a). As a stable solution in the power supplies, Haupschienen variants from the MEAULL company have proven themselves, which can be purchased via the BSC shop.

The voltage supply should be redundant, i.e. a reliability of the care. In this case, if a power supply no longer provides a voltage, the second intervention and the circuit board will continue without interruption. Thus, the board could be connected to a DC/DC power supply directly from the battery and an AC/DC power supply connected to the EVU network. The BSC offers two separate inputs for this. To define which voltage source the primary voltage source is, this should be set about 0.2V higher. Then the power supply of the BSC takes over the power supply with the higher voltage.

**Increasing power supply:**

If necessary, it is possible to expand voltage supply to more than 5V (e.g. 12V / 24V). The following conditions must be observed (be careful, the circuit board marking has changed between different hardware visions. These are always given as follows as HWREV < 2.5 / HwRev > = 2.5):

* JP28 / R61 (supply voltage for the BSC components): is usually bridged and must be separated for higher supply voltages 5V.
The component can be found on the back of the circuit board, right next to the solemnity connections of U19.
* JP29 / R91 & JP25 (relay voltage supply):
  * When using 5V relay, no change to these jumpers is necessary
  * If a higher supply voltage> 5V is desired for the relay without loading U19
    * HW-Rev <2.5
      * When using relay higher voltage, separate the connection 2-1 and bridge 3-2 with the soldering iron
Note: With the BSC V2.3, the lettering of the jumper from JP29 is wrong! There is 1 left, but 1 is on the right.
    * HW-Rev> = 2.5
      * When using relay higher voltage, remove resistance R91 and set solder jumper JP25.
* U19 is to be equipped with a DC DC converter for a **Higher supply voltage** larger 5V
  * Suitable DCDC modules are offered in the BSC shop up to 27V.
* Otherwise, a suitable DC-DC converter depends on the input voltage
* The square soldering point at U19 is the 5V output of the DC/DC converter. Be sure to pay attention to polarity!
  * If 5V relays are used, please note that they are supplied with the U19 voltage controller, therefore use> = 1a DC-DC converter
  * Here is an example of the U19 stock:
![](img/hardware/hw_bestueckung_u19.jpg) {Width = "400"}

## Can/rs485
All interfaces are galvanically separated and can therefore be connected directly to a BMS (RS485 -> Serial0-10) or inverter (CAN) without any adapter.
The voltage level of the interfaces mentioned are "standardized".
A seplos BMS can be contacted directly via the RJ45 socket.

## OneWire
Temperware sensors can be connected to the OneWire interface without additional further hardware.
The usually necessary pullup resistors are already integrated on the BSC board.


# Temperature management
The BSC needs a light thermal to cool the top of the boards.
Please do not unnecessarily pack the board and ensure continuous ventilation.


# How do you separate solder jumper
To do this, the solder jumper set in delivery must be removed mechanically.
This is best done with a "dremel" that only removes the copper layer on the surface.
Caution! There are other copper layers within the board, which of course must not be violated.
![](img/hardware/hw_trennen_loetjumper.jpg) {Width = "600"}

# Jumper configuration

## J6 for regular operation
Opening Jumper J6 is required to program an unprogrammed board.
This must be set for normal operation.
![](img/hardware/hw_jumper_j6.png) {Width = "400"}

## J4 for programming
The setting of Jumper J4 is required to program an unprogrammed board.
This remains open to normal operation.
![](img/hardware/hw_jumper_j4.png) {Width = "400"}

## Connect funds of the relay to VIN
The medium tapes (COM) of the relay can be connected to the VIN of the board by setting the respective jumper.
![](img/hardware/hw_relais_vin.png) {Width = "600"}

## J14-J16 Activate the outputs
These relays have other functionalities that are currently not shown with the firmware.
Therefore, the jumper must be placed on the blue marked positions.
![](img/hardware/hw_relais_jumper_j14_j16.png) {Width = "600"}

# BSC display
The display for the BSC was spun into a [separates Projekt](https://github.com/shining-man/bsc_display) in which the firmware can also be found.

## Support display
Hardware version 3.3 of the display was tested.
Available, for example, via Aliexpress from various senders.
![](img/hardware/hw_display.png) {Width = "500"}

## Connection to the BSC mainboard
The connection is made via the extension port "J3":

* The data connection via the I²C bus of the PINS "SCL/SDA", which can be connected 1: 1.
* A 5V voltage supply for the display can also be taken off. This must be connected to the appropriate connection of your display together with GND.
![](img/hardware/hw_display_stecker_j3.png) {Width = "400"}
![](img/hardware/hw_display_stecker_j3_2.png) {Width = "200"}

## Pinout of the display "WT32-SC01"
![](img/hardware/hw_pinout_display_wt32sc01.png) {Width = "700"}
