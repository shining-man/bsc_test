## software

### The SOC value of the BMS and the value transferred to the inverter do not match
There are three options here that can "cause" this.

1) The setting of the SOC source is defined incorrectly.
![](img/troubleshooting/troubleshooting_soc_quelle.png) {Width = "400"}

2) If the master source 5S has failed, the SOC is adopted by a device that is still available. As soon as the master's source is available again, it is switched back to it.

3) The operating mode 2 of the SOC-Value Adjusted is activated and linearizes the SoC between the set voltage values.
Please switch to/Settings/interfaces/serial and scrolls to the "Value Adjustments" in the menu.
There should be no two values ​​per interface here if a BMS with SOC calculation is used.
Further information can be found [hier](settings_bsc.md#serial) under "Operating mode 2: Linear SOC calculation between two cell voltage thresholds".

### Log entry: "MQtt Queue is full"
This problem can occur if the broker cannot access all data from the cue within a certain time.

**Possible cause:**
A user reported difficulties in an environment with a Docker container that contained several integrated applications.

**Solution:**
The division into several Docker containers eliminated the problem. It can therefore be helpful to distribute the load through such an architectural change.

### Serial debugging
In the event of difficult-to-understand errors, special firmware versions can be made available for troubleshooting.
These versions issue extended information on error limitation via the programming interface installed on the BSC.
For this purpose, the serial0 is used to which no external device may be connected to the process via RS485.
The internal log that can be reached in webui is deactivated in these versions and only shows the previous events of the old version.

In order to record this data stream, a UART/USB converter with <u> 3.3V level </u> and a PC program is required.
A wide variety of manufacturers can be used as a converter, adapter has proven to be well functioning with an FT232R chip. Adapter with a CP340G chip often also works.
Adapter that are not designed for 3.3V can irreparably damage the controller!

The converter is to be connected via the three -pole pen strip "J2" next to the processor.
The respective signal designation of the pins is printed on the top left corner of the board.

- TX comes to RX
- RX to TX
- GND to GND

![](img/troubleshooting/troubleshooting_serial_debug_j2.png) {Width = "400"}

"Putty", "Yat" and "Hterm" has proven itself as a PC program under Windows.
The serial interface is referred to as the "COM port". You can find the right number of those in the Windows device manager under "Connections (Com & LPT)".
The data connection parameters are 115200baud, 8bit, no parity, a stopbit.
To test the connection, the BSC can be switched on again and again. Information is sent to the PC.


A short **video** can also be found [hier](mov/serial_debugging.mp4).

## Hardware

### Communication with external hardware does not work
Please check all connected connections again.
Each plug has a **printed on the circuit board** pin1 marking.
This must be correct with the printed signal information and the connected line!

#### Check CAN contact
**1)**
In the event of a CAN connection, a resistance of 120ohm should be measured between the two data lines (l / h) per connected side.
This can be checked in which you switch the devices on both sides without a power and measure the resistance between CAN _L and can_ H per side without a connected connection with a multimeter.

From time to time there are devices without this built-in resistance, then only measure 120Ohm on the BSC page.
Here, however, you should be listening and the pin assignment should be meticulously checked again, as this is atypical.

If there are 120 ohm on both sides, you can connect both devices together and measure the resistance on the signal lines again in the electricity.
Now 60ohm should be displayed on the multimeter.

**2)**
At a CAN interface, "CAN _H with the opposite side can_ H" and "Can _L with the opposite side can_ L" must always be connected.
This must be checked.
Furthermore, the GND signal must be contacted on both sides.

#### Serial 2 without function / no data connection possible (only timeouts in the log)
Please see if the jumper J6 was set on the board.
Further information [hier](hardware.md#j6-fur-den-regularen-betrieb).

### Sporadic CRC errors at the serial interfaces (HW2.3 and HW2.4)
Due to the lack of sweater on the RX signals of the serial interfaces, there may be a float of the signal. This creates the insertion of 10kOhm pullup resistors.
  
Regarding the sizes of usable resistors, it is very important to solve your own skills.
- For example, 0603 is suitable between the pins. 0805 is also possible
- Vertical to the soldering pad would work very well in 1206, but 0805 is also possible
- 0805 works just like 1206 between the THT pins from J3

#### HW2.3
**Serial 0+1+2**
With Serial 0, 1, 2, the 10 co -cock resistance to U4, U5 and U6 must be solved between PIN 7 and 8.
For easier soldering, contacting can be used a little further up above.

Board view from below:
![](img/troubleshooting/troubleshooting_hw_23.png) {Width = "800"}

#### HW2.4
**Serial 0+1**
With Serial 0 and 1, the 10 co -cock resistance to U4 and U6 must be soldered into between PIN 7 and 8.
With U4 it may be easier to contact this as in the picture.

**Serial 2**
In Serial 2, the 10kOhm resistance between PIN 6 and PIN 7 of the J3 connector must be used.
This can also be done quite well with a wound resistance (THT).

Board view from below:
![](img/troubleshooting/troubleshooting_hw_24.png) {Width = "800"}

### Can_gnd contact (hw2.3)
CAN _L & can_ H can be contacted via the screw terminals of the hardware.
The associated CAN_GND is missing here and must therefore be tapped on the underside of the circuit board via the pins of the voltage controller.

Board view from below:
![](img/troubleshooting/troubleshooting_hw_23_cangnd.png) {Width = "800"}