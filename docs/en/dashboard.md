# Dashboard
> Note: The dashboard shown here is only available in the [Insider Version](insider.md)

## Overview

The dashboard of the **Battery Safety Controller (BSC)** offers a quick overview of the entire system.
In individual tiles, relevant data on system status, inputs and outputs, loading and discharge regulations as well as the connected data devices are displayed.

![](img/dashboard/dashboard_1.png) {Width = "950"}

## Tile
The individual tiles and their content are described in detail below.

### system
This tile shows the current state of the system.

**Buttons:**
![](img/dashboard/button_menue.png) **Menu:** opens the main menu

![](img/dashboard/button_livedata.png) **Live data:** leads to the menu for live data

![](img/dashboard/button_settings.png) **Settings:** Direct access to the system menu


### Active errors
This tile shows active errors of the system.

**A notice:** Not every error in the log file is displayed as "Active Error".

**Possible active nor:**
- Data Device X Error
- Plausibility Check Error
- Canbus error

**Buttons:**
![](img/dashboard/button_errors.png) **Log:** opens the log file


### Trigger
This tile shows the status of the configured triggers with the respective descriptions.
As soon as the trigger is active, the light gray stored trigger number is shown dark gray.

**Buttons:**
![](img/dashboard/button_trigger.png) **Trigger overview:** leads to a detailed view of all triggers used and their functions.


### Relays and digital inputs
These tiles show the current status of the relays and digital inputs.
As soon as a relay or digital input is active, the exhaustive light gray stored entrance/output is shown in dark gray.


### Inverter
This tile shows the data sent to the inverter.

**Displayed values:**
- Tension (V)
- Electricity (a)
- Soc (%)
- Max. Charging and unloading values ​​(V, A)

In addition, the current loading phase is displayed (*Float, absorption*).


### Load - limits
This tile indicates a bar for each activated loading regulation, which represents the maximum permitted charging current.

**Design regulations and their names in the dashboard:**

| Designation | Description in the dashboard |
| -----------------------------------------------------------------
| Discharge of charging stream cell voltage-dependent | **Cell Volt** |
| Reduce charging current - SoC | **Soc** |
| Reduce charging current at cell drift | **Cell Drift** |
| Charge Current Cut-Off | **Cut off** |
| Charging current per pack too big | **Pack high** |
| Reduce charging current - temperature | **Tempo** |
| Voltage control for charging current limitation | **zero** |


### Discharge - limits
This tile indicates a bar for each activated discharge regulation, which represents the maximum permitted discharge current.

**Discharge regulations and their names in the dashboard:**

| Discharge | Description in the dashboard |
| ---------------------------------------------------------------
| Discharge current of the cell voltage-dependent throttling | **Cell Volt** |


### Data devices
This tile shows the live data of the connected data devices.

**Buttons:**
![](img/dashboard/button_datadevice.png) via the button (in the header) can be switched to displaying the cell tension.