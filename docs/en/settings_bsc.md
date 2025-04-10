## General
There are two version of the webui. The Classic Webui and the Webui V2.
The webui V2 is shown below, which is not available so currently.

### General information on operation
**Save the settings**
Saving differs in the webui's.

Classic Webui:
The changed settings can be saved with the "S" button, which is in each line of the settings.
It should be noted that only the setting in the respective line of the "S" button is saved.

Webui V2
All changes can be stored here via the "Save" button in the headline. Not every change has to be saved individually.

### Functional principle of monitoring functions
This section explains how internal trigger can be used to monitor and control different values ​​(e.g. temperature, voltage) in order to react to potential danger.
  
**Trigger functionality**
A trigger can be configured for each value to be monitored, which becomes active when a defined limit is reached. An activated trigger initially does not trigger a direct action. However, it can be flexibly set which actions should be triggered by the trigger. For example:

  - a relay is switched (e.g. to activate a fan),
  - the inverter is instructed to reduce its charging current to 0 A.


This logic makes it possible to combine trigger (as a signal provider) and connected actions (as a signal consumer) in a flexible way. Up to 10 internal triggers are available.

**How it works for several sources**
If several sources are connected to a trigger, the following rule applies:

  - Activation (high): The trigger is activated as soon as one of the connected sources exceeds the defined limit.
  - Deactivation (low): The trigger is only deactivated when all connected sources have returned to normal.

> **A notice:** Especially when using virtual triggers (Vtrigger), make sure that they have to be specifically deactivated by automation in order to be able to use the trigger functionality again.

**Sample application**

  - Two temperature sensors (Sensor 2 and Sensor 3) monitor a border temperature of 30 ° C. As soon as one of the two sensors exceeds this value, Trigger 1 becomes active.
  - Based on Trigger 1, two actions can be configured:
      - Relays 1 is switched to activate a fan.
      - The inverter automatically reduces its charging current to minimize heat development.

**Summary**
This combination of flexible trigger sources and configurable target campaigns enables precise and versatile control. The logic ensures that dangers can be recognized early and suitable measures can be taken, while the flexibility to adapt to individual requirements is preserved.

## Dashboard
After calling the website via the integrated WLAN module (IP or BSC.info), the home board comes with a few basic information.
You can navigate to the respective functions via the side menu.

![](img/settings/settings_dashboard.png) {Width = "950"}

| Kachel | Description |
| ------------- | ------------- |
| System | As long as the "Running" tile is located, the individual tasks run without errors.   If an internal task exceeds its predetermined maximum cycle time, there is an error with the associated TASKNAUFER.  |
| MQTT | Indicates whether there is a connection to the MQTT broker |
| Free Heap | Displays the free HEAP and ever the lowest free HEAP since the system start |
| BT-Devices | Status of the connected BT devices such as a NEEY balancer; "C" means connected |
| Trigger | Status of the ten possible trigger; 0 = no trigger, 1 = trigger |

## Live data
![](img/settings/settings_livedaten.png) {Width = "950"}
"Fet State" describes the current FET loading/unloading state.

![](img/settings/settings_fet_state.png) {Width = "300"}

## system
![](img/settings/settings_system.png) {Width = "950"}

Here you can find all system internal setting options, such as user names and passwords for WLAN and MQTT logins.
Please note that the Tilde sign (~) is currently not supported as a password sign <u> </u>.

### Mqtt
![](img/settings/settings_system_mqtt.png) {Width = "300"}
As soon as MQTT is activated and the associated IP address and the port are set, the BSC cyclically sends the data to the MQTT broker.

**Vtrigger**
With "Remanenger Vtrigger" it can be determined which Vtrigger should be defined as saved. A saving Vtrigger ensures that its values ​​are automatically restored even after a restart (reboot) or a voltage failure.
More on the subject of Vtrigger under [MQTT](mqtt.md#virtual-trigger).

### Timer
If you use an external NTP server and have problems with time synchronization, you can also use the router of your network - this often works more stable.
Using the example of an AVM Fritzbox, you can activate the time server in the menu under home network/network/network settings.
As time servers, for example, you can define the following: "ntp1.t-online.de; 2.Europe.pool.ntp.org".
The IP address must then be specified in the BSC.

## Interfaces
In the Settings interfaces, what is connected to which interface is set. Here **not** is set what should happen with the data from a BMS or balancer, or when the relay output should switch. This is then done in the settings for the alarm rules or the inverter.

### Serial
![](img/settings/settings_serial.png) {Width = "950"}
In this section you determine which hardware is connected to which serial port. In addition, it is necessary to configure the "Data Device mapping" section which serial interface is assigned which internal data device.

You can find detailed information on the establishment of the Data Device mapping in the chapter [Data device mapping](#data-device-mapping)

This configuration ensures that the connected hardware is correctly recognized and linked to the corresponding internal data devices.

**Assignment (software => hardware):**

* Serial 0 => U1
* Serial 1 => U2
* Serial 2 => U3

All other interfaces shown can only be used with a connected serial extension.

**Support hardware**
![](img/settings/settings_unterstuetze_bms.png) {Width = "400"}
The list of available hardware is continuously expanded in order to meet the requirements and needs of our users. The picture shown only serves as an illustration and represents an example.

#### filter
![](img/settings/settings_schnittstelle_filter.png) {Width = "400"}
This filter serves to identify jumps in the cell tension and to filter out. The response threshold of the filter is set as a percentage compared to the previous valid value. As soon as the cell voltage exceeds the specified percentage, the new value is not adopted, but also not rated as a mistake.

The "Number of RX errors" function enables the threshold to be determined from when a cell voltage deviation is regarded as an error. As soon as the set number of errors is exceeded, the timeline is no longer updated for the last valid package in the system.

These functions ensure more precise and stable data processing by filtering temporary voltage jumps and preventing faulty packages.

#### Plausibility Check
![](img/settings/settings_schnittstelle_plausibility_check.png) {Width = "500"}
The "plausibility check" is an important function that continuously monitors the current flow and the cell tension of the data devices connected to the system.

If the values ​​for electricity and cell voltages no longer change regularly over a longer period of time, this indicates that the BMS no longer sends any valid data. In this case, it can be assumed that there is a problem in the BMS.

The "Plausibility Check" offers early warning in the event of irregularities and supports the reliable function and safety of the entire system.

**How the plausibility check**:
`` `Mermaid
Flowchart TD
n1 ["plausibility check"] -> n7 ["is electricity <'electricity threshold'"]
N7 -> N8 ["Cell voltages change 'ZEIT 2' not"]
N8 -> N4 ["Trigger becomes active"]
n1 -> n6 ["is electricity> = 'electricity threshold'"]
N6 -> N10 ["Cell voltages change 'time 1' not"]
N10 -> N4
`` `

#### Value Adjustment for SOC transmission to the inverter
![](img/settings/settings_value_adjustment_soc.png) {Width = "500"}
The "Value Adjustment" enables the inverter to transmit an adapted state of charge (SoC) depending on the cell tension. There are two operating modes available that cover different requirements and behaviors.

##### Operating mode 1: Fixed SOC transmission when the cell tension is defined
In this mode, the cell voltage is defined, in which the inverter should receive a SOC of 100%. When the cell voltage reaches or exceeds the set value, the SOC of 100% is transmitted to the inverter. As soon as the cell voltage falls below the set value, the SOC is returned to the inverter by the battery management system (BMS).

**A notice:** For this mode, the "Cell Voltage for SOC 0%" field must remain empty. This ensures that only the upper threshold (for 100% SoC) is taken into account and that the SOC is calculated solely by the BMS if the cell tension drops under the defined threshold.

**Example:**

- Cell voltage for SOC 100%: 3.5 V
  - With a cell voltage of 3.5 V or higher, the inverter is transmitted 100% of the inverter.
  - If the cell voltage falls below 3.5 V, the SOC transmission takes place regularly through the BMS.

##### Operating mode 2: Linear SOC calculation between two cell voltage thresholds
In this mode, two cell tension thresholds are defined: an upper threshold for 100% SoC and a lower threshold for 0% SoC. When the cell voltage reaches or exceeds the upper threshold, the inverter is transmitted 100% of the inverter. If or falls below the cell tension, the lower threshold is transmitted, a SoC of 0% is transmitted. For cell stresses between these two values, the SOC is calculated linearly and sent to the inverter accordingly.

**Example:**

- Cell voltage for SOC 100%: 3.5 V
- Cell voltage for SoC 0%: 2.9 V
  - With a cell voltage of 3.5 V or higher, the inverter is transmitted 100% of the inverter.
  - With a cell voltage of 2.9 V or lower, the inverter is transmitted a SOC of 0%.
  - In the case of cell voltages between 2.9 V and 3.5 V, the SOC is calculated linearly and transmitted to the inverter.

This mode is particularly useful for BMS systems that do not report its own SOC, since the SOC is automatically determined depending on the cell stresses.

**Important NOTE:** Make sure that the entered cell voltages meet the specifications of the battery system used to ensure optimal function and safety.

### Data Device mapping
![](img/settings/settings_data_device_mapping.png) {Width = "950"}

The Data Device Mappings serve to assign the serial interface or the Bluetooth device to the internal data device used in the BSC (Battery System Controller).

The following parameters must be set here:

  - Interface: the serial interface or the Bluetooth device that is used.
  - Address of the Data Device: The clear address that is assigned to the specific device.
  - Name (optional): A custom name that is displayed in the further settings of the parameter. This name is also used for the MQTT-Topic of the respective devices.

If several devices are connected to a serial interface and the BMS (Battery Management System) supports the connection in Daisy Chain mode, it is necessary to define the correct address for each device. This is the only way to ensure a clear assignment and error -free communication between the BMS and the devices.

> **A notice:** The correct configuration of the Data Device Mappings is essential to ensure trouble -free functionality. Note the addressing rules of your BMS system.

### Relay outputs
![](img/settings/settings_relais.png) {Width = "950"}
Here the basic settings for the relay outputs can be made.

* **Triggering at**
Here it is stated in which upcoming trigger the relay is to be switched
* **Tripping behavior**
    * Permanent: The relay remains attracted as long as the trigger is due
    * Impulse: The relay switches for a duration of X MS. The impulse duration is discontinued under "Impulse duration".
* **Impulse duration**
The impulse duration is set here when "impulse" has been set in the trigger behavior.
* **delay**
Indicate how many seconds the switching of the relay should be delayed at an upcoming trigger.
* **Invert**
The option enables the relay output to be flexibly switched between the operating modes NO (Normally Open) and NC (Normally Closed). By activating this option, the logic of the relay output is reversed, so that the alternative state is used when the switching process is carried out. This function is particularly useful to ensure compatibility with various control requirements or circuit design.

The logic with the triggers runs through the entire system. There are triggers, e.g. the digital inputs and there are trigger customers, e.g. the relay outputs.

### Digital inputs
![](img/settings/settings_di.png) {Width = "950"}
The basic settings for the digital inputs can be made here.

* **Invertic receipt**
Here the entrance can be inverted
* **Forward**
Here the trigger can be set to which the entrance goes.   When the entrance becomes high, the trigger set here becomes active.  If the entrance is inverted, then the trigger is active at the entrance.
 
### OneWire
![](img/settings/settings_onewire1_1.png) {Width = "950"}
Here the addresses of the OneWire temperature sensors are determined.

As soon as this one-time configuration page is called, the controller scans the bus to OneWire-Devices and displays it at the bottom of the page.
The devices shown in bold are new devices that are not yet stored in the OneWire configuration page.
This makes it easier to identify newly connected sensors.

![](img/settings/settings_onewire1_2.png) {Width = "950"}

### OneWire II
![](img/settings/settings_onewire2_1.png) {Width = "950"}
An offset for the respective OneWire temperature sensors can be set here.

### Bluetooth
**Bluetooth is currently not available!**
![](img/settings/settings_onewire2_2.png) {Width = "950"}
Here, up to 7 Bluetooth devices can be determined from which the controller gets data.
To do this, the device type and the MAC address (in small letters) must be set.

As soon as this configuration page is called, the controller scans cyclically according to new BT devices
And indicate the last 5 found at the bottom of the page.

**Supported hardware**
![](img/settings/settings_unterstuetze_bms_bt.png) {Width = "400"}

## Alarm rules
In the alarm rules you can set which data should be monitored by which devices.

### BMS
![](img/settings/settings_alarmrules_bms.png) {Width = "950"}
The BMS alarm rules enable the monitoring of the configured data devices. Various parameters of the Data device can be monitored to configure alarms and trigger automatic actions when certain threshold values ​​are reached.
  
The voltage trigger is triggered when the voltage falls under the "min" value set or the "Max" value exceeds. In order to avoid unnecessary alarms due to small fluctuations, an adjustable hysteresis can be added, which "calms down" the trigger and is only activated in significant changes.

The following monitoring functions are available:

| Monitoring function | Option | Description |
| : ------------- | : ------------- | : ------------- |
| **No data from the BMS** |  |  |
|  | Trigger no data | Activate/disable the monitoring function |
|  | Action at Trigger | Gives where trigger should be triggered |
|  | Trigger no data | If no data comes x seconds, then trigger is triggered |
| **Voltage monitoring cell min/max** |  |  |
|  | SPG. Surveillance | Activate/disable the monitoring function |
|  | Action at Trigger | Gives where trigger should be triggered |
|  | Number of cells monitoring | Number of cells that are to be monitored.  The first cell is always started. |
|  | Cell voltage min | Supporting the surveillance |
|  | Cell voltage max | Monitoring upper limit |
| **Voltage monitoring Total Min/Max** |  |  |
|  | Action at Trigger | Gives where trigger should be triggered |
|  | Voltage min | Supporting the surveillance |
|  | Tension max | Monitoring upper limit |

### temperature
![](img/settings/settings_alarmrules_temperatur.png) {Width = "950"}
At this point, the settings for monitoring the temperature values ​​of the Data devices and OneWire temperature sensors can be configured.

| Option | Description |
| : ------------- | : ------------- |
| Source | Here it can be determined whether the temperature data is obtained from a data device or the OneWire sensors.
| Sensor number from <br> Sensor number up to | Here the OneWire sensors to be monitored can be determined by specifying an area (from/to). The sensor numbers refer to the numbers of the OneWire sensors.  |
| Monitoring | A surveillance function can be set here.  Depending on the monitoring function, the fields value 1+2 have a different function |
| Reference sensor <br> Value 1 <br> Value 2 | Specific function, depending on the monitored monitoring |
| Triggering | Gives where trigger should be triggered.  The foremost is that a surveillance function has been selected |

**Monitoring functions:**

* **unadorned**
The monitoring is deactivated

* **Maximum value crossing**
It is monitored whether one of the sensors exceeds the maximum permitted temperature value.
The maximum permitted temperature is determined with the "value 1".
  * Reference sensor: -
  * Value 1: maximum permitted temperature
  * Value 2: -

* **Minimal value sub-man**
It is monitored whether one of the sensors falls below the minimally permitted temperature value.
The minimally permitted temperature is determined with the "value 1".
  * Reference sensor: -
  * Value 1: minimally permitted temperature
  * Value 2: -

* **Maximum value crossing (reference)**
It is monitored whether one of the sensors exceeds the maximum permitted temperature value.
The maximum permitted temperature specifies the sensor defined under "reference sensor".
  * Reference sensor: sensor number of the OneWire temperature sensor
  * Value 1: maximum permitted temperature difference
  * Value 2: -

* **Different value monitoring**
The maximum temperature deviation of the sensors is monitored.
If the difference between the lowest and highest value is too great, the trigger is triggered.
  * Reference sensor: -
  * Value 1: maximum permitted temperature difference
  * Value 2: -



### Currently active inverter throttling
You can view the set throttling with the help of the Restapi.
Add to the IP address of the BSC "/Restapi" (e.g. 192.168.1.100/restapi).

The "CC _"-values ​​and" dcc_" values ​​shown represent the electricity limited by the respective loading regulation.

![](img/settings/settings_restapi_aktive_drosselung.png) {Width = "250"}

If it is not possible to display the data directly during a throttle event, it is possible to have it temporarily recorded using an alternative platform such as Home Assistant. It should be noted that each query of the rest-API includes all available data.

For the transfer of the data, a duration of around 0.5 to 1 second per package can be expected. This period serves as an orientation.

Below you will find an example of a Yaml code that can be used to create a sensor to display the value of "Setpoint_CC" in Home Assistant:

`` `Yaml
Platform: rest
Name: Bscapi _setpoint_ CC
Resource: http://192.x.x.x/restapi
Value _template: "{{value_ JSON ['inverter'] ['Setpoint_cc']} "
Unit _of_ Measurement: "A"
State_Class: "Measurement"
ICON: "MDI: API"
`` `

## Firmware update
A firmware update can be initiated directly via the menu.
Information on the current release stand, as well as the suitable description of the changes is displayed live.
Correctly set network gateway is required for live information.

![](img/settings/settings_ota_update.png) {Width = "400"}
