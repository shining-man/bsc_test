## Important Note! Read First!
The Settings and Configuration Suggestions Listed Here Are Based On Experience of Users and Are Specialy Developed for Lifepo4-Based Cells. They only serve as a guide and represent a **Initial design** for a possible configuration with the devices described.

Please note that we cannot guarantee or guarantee the correctness, Completeness or Applicability of the Information Provided. The correct adaptation of these settings to your specific system requires well -founded technical knowledge. It is your responsibility to carefully check, understand and adapt the information proved before Implementing IT in your system.

We Strongly Advise Against Taking Over The Attitudes Shown Without Reflection. Take the Necessary Time to Understand the Proposed Configurations as a Whole and Ensure That You Are Suitable for Your Individual Requirements and Systems. IMPROOPER use can lead to damage to the devices, The Batteries or Even Endanger Your Security.

**A notice:** The information Listed here is at your own risk. We assume no liability for direct or indirect damage that could arise from the application of the Available settings.

## Configuration Examples
### 5x JK-InverterBMS 200A (16S); 2x Victron Multiplus 5000

#### BSC - Settings Serial Interface

![](img/beispielconfig/beispielcfg_serial.png) {Width = "450"}


#### BSC settings inverter
##### General
Serial 6 was set here as a data source (master) BMS, Since the Highest Temperature Occur Through the Highest Position in the stack.
This temperature is used to transfer the "Battery Temperature" to Venus OS. Sensor number 1 Usually had the highest temperatures in this Environment.
![](img/beispielconfig/beispielcfg_inverter_general_1.png) {Width = "450"}
  
![](img/beispielconfig/beispielcfg_inverter_general_2.png) {Width = "450"}

##### Load
![](img/beispielconfig/beispielcfg_inverter_charge_1.png) {Width = "450"}
![](img/beispielconfig/beispielcfg_inverter_charge_2.png) {Width = "450"}

##### Unclear
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
##### General
![](img/beispielconfig/beispielcfg_inverter_general_seplos.png) {Width = "1050"}

##### Load
![](img/beispielconfig/beispielcfg_inverter_charge_seplos.png) {Width = "1050"}

##### Unclear
![](img/beispielconfig/beispielcfg_inverter_discharge_seplos.png) {Width = "350"}

#### BMS
##### parameter
![](img/beispielconfig/beispielcfg_bms_seplos_parameter.png) {Width = "1050"}

##### Switch
![](img/beispielconfig/beispielcfg_bms_switches.png) {Width = "1050"}