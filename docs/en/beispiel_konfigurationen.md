## Important NOTE! Read first!
The settings and configuration suggestions listed here are based on experience of users and are specially developed for LIFEPO4-based cells. They only serve as a guide and represent a **Initial design** for a possible configuration with the devices described.

Please note that we cannot guarantee or guarantee the correctness, completeness or applicability of the information provided. The correct adaptation of these settings to your specific system requires well -founded technical knowledge. It is your responsibility to carefully check, understand and adapt the information provided before implementing it in your system.

We strongly advise against taking over the attitudes shown without reflection. Take the necessary time to understand the proposed configurations as a whole and ensure that you are suitable for your individual requirements and systems. Improper use can lead to damage to the devices, the batteries or even endanger your security.

**A notice:** The information listed here is at your own risk. We assume no liability for direct or indirect damage that could arise from the application of the available settings.

## Configuration examples
### 5x JK-InverterBMS 200A (16S); 2x Victron Multiplus 5000

#### BSC - Settings Serial interface

![](img/beispielconfig/beispielcfg_serial.png) {Width = "450"}


#### BSC settings inverter
##### Generally
Serial 6 was set here as a data source (Master) BMS, since the highest temperatures occur through the highest position in the stack.
This temperature is used to transfer the "battery temperature" to Venus OS. Sensor number 1 usually had the highest temperature in this environment.
![](img/beispielconfig/beispielcfg_inverter_general_1.png) {Width = "450"}
  
![](img/beispielconfig/beispielcfg_inverter_general_2.png) {Width = "450"}

##### Load
![](img/beispielconfig/beispielcfg_inverter_charge_1.png) {Width = "450"}
![](img/beispielconfig/beispielcfg_inverter_charge_2.png) {Width = "450"}

##### Unload
![](img/beispielconfig/beispielcfg_inverter_discharge_1.png) {Width = "450"}

#### BMS
##### Settings
![](img/beispielconfig/beispielcfg_bms_settings_jk_1.png) {Width = "350"}
![](img/beispielconfig/beispielcfg_bms_settings_jk_2.png) {Width = "350"}
![](img/beispielconfig/beispielcfg_bms_settings_jk_3.png) {Width = "350"}
![](img/beispielconfig/beispielcfg_bms_settings_jk_4.png) {Width = "350"}

##### Control
![](img/beispielconfig/beispielcfg_bms_settings_jk_5.png) {Width = "350"}


### 1x seplos 10e 200a (16S); 3x Growatt SPF5000es

#### BSC settings inverter
##### Generally
![](img/beispielconfig/beispielcfg_inverter_general_seplos.png) {Width = "1050"}

##### Load
![](img/beispielconfig/beispielcfg_inverter_charge_seplos.png) {Width = "1050"}

##### Unload
![](img/beispielconfig/beispielcfg_inverter_discharge_seplos.png) {Width = "350"}

#### BMS
##### parameter
![](img/beispielconfig/beispielcfg_bms_seplos_parameter.png) {Width = "1050"}

##### Switch
![](img/beispielconfig/beispielcfg_bms_switches.png) {Width = "1050"}