## Virtual trigger

There are 10 virtual triggers (Vtrigger) that can be controlled by MQTT. The virtual trigger data passes 1: 1 to the normal trigger.

In order to obtain a Vtrigger "saved", i.e. beyond a reboot of the BSC, it can be sent to the BSC as "retain". As soon as the BSC has been registered again on the broker, the trigger state is updated directly with the BSC.

In addition, it can be determined for each Vtrigger whether it should be saved. These settings are under "System" on the [MQTT-Optionen](settings_bsc.md/#mqtt).

## Example
If the Vtrigger 1 is activated, trigger 1 also becomes active.

`{Device Name}/input/vtrigger/{Trigger Nummer}`

{Device name}: The device name from the system settings
{Trigger number}: trigger number from 1 to 10

Payoad:
0 -> Trigger low
1 -> trigger high

## Integrate MQTT into home assistant
In order to protect the clarity of the configuration.yaml, separate MQTT-Config files can be used.
For example, it makes sense to generate a file for each hardware connected.

The following program line must be stored in the "Config/Configuration.yaml":

`` `Yaml
MQTT:
  - Sensor :! Include _you_ Merge_list MQtts/
`` `
The individual MQTT configurations are then stored in a subdirectory called "MQTTS".
This must be created manually.

![](img/mqtt/mqtt_files.png)

Now the .yaml files have to be stored at this point.
Home assistant will read and evaluate each of the files during the boat.

### Example configurations
Below you will find sample configurations for various hardware:

* BSC internally
* BMS
* Inverter
* Neey-Balancer

#### Adjust configuration
The files must be renamed for integration instead of ".txt" into ".yaml".
Unfortunately, Github .yaml does not support.

##### Datadevices
Depending on the BSC configuration, the datadevicename must be correctly ordered in the files depending on the BSC configuration.
The area for this is marked with the abbreviation "{datadevicename}".
{Datadevicename} = Defined Clar Text Name in Data Device mapping.

##### Uniquid
Within the files there is a uniqueid per sensor value which must be defined by everyone.
You can generate this, for example, with "version 1" https://www.uuidgenerator.net/version1.

Alternatively, you can change all UUIDS to be replaced at once via the Addon called "Visual Studio Code Server" within Home Assistant.
The same procedure works via visual studio code with the Addon "Uuid Generator of Netcorext".

- Mark the temporary string "XXXXX-XX-XX-XXX-XXXXX"
- Right click -> "Change All Occurrences"
![](img/mqtt/mqtt_uuid_generator.jpg)
- Right click -> "Generates Uuid at Cursor"
![](img/mqtt/mqtt_uuid_generator_2.jpg)
![](img/mqtt/mqtt_uuid_generator_3.jpg)
=> Save

#### Files

[BSC-Internal.txt](files/mqtt_internal.txt)
[BSC-Inverter.txt](files/mqtt_inverter.txt)
[BSC-BMS-DataDevice.txt](files/bsc_bms_datadevice.txt)
[BSC-Neey1_BLE.txt](files/mqtt_neey1_ble.txt)

### Integrate existing MQTT configuration in a new directory
If a dedicated MQTT.YAML was used in advance in the configal directory, it can simply be copied and used in the directory just created.
It should be noted that the command "Sensor:" may no longer be available in the outsourced configuration files.
Furthermore, the definitions must now be moved to the left.
`` `Yaml
#### BSC inverter

    - State_topic: BSC/Inverter/Charge Current Soll
Name: DC charging current should
Unique_ID: XXXXX-XXX-XXX-XXXXXXX
State_Class: Measurement
Device_Class: Current
ICON: MDI: Current-DC
Unit _of_ Measurement: "A"
Device:
{
Identifiers: ["BSC-Inverter"],
Manufacturer: "BSC",
Model: "BSC",
Name: "BSC-Inverter",
}

    - State_topic: BSC/Inverter/Discharge Current Soll
Name: DC enthus to
Unique_ID: XXXXX-XXX-XXX-XXXXXXX
State_Class: Measurement
Device_Class: Current
ICON: MDI: Current-DC
Unit _of_ Measurement: "A"
Device:
{
Identifiers: ["BSC-Inverter"],
Manufacturer: "BSC",
Model: "BSC",
Name: "BSC-Inverter",
}
`` `

### Useful tools
Automatic creation of the BSC in HA: <a href="https://github.com/dominikfe/ha_bsc_discovery_automation" target="_blank"> https://github.com/dominikfe/ha_bsc_discovery_automation[MDPROTECT1] </a>