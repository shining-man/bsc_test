# Inverter
In this section, you can define the loading and unloading trading cladding in addition to the definition of the connected inverter.
All percentage limits are applied to the values ​​set in the "Basic data" category.
![](img/settings/settings_inverter_basisdaten.png) {Width = "950"}

## general
### CAN bus
Here you can define the protocol to be used towards inverter.
The setting "Send Extended Data" can only be used for a connected Victron system. Further information can be viewed [hier](devices/wechselrichter.md#einstellungen-bsc).

### Valuehandling Multi-Bms
![](img/settings/settings_inverter_soc.png) {Width = "450"}
With the "ValueHandling Multi-BMS" you have the option of configuring the State of Charge (SOC) for the transmission to the inverter. This enables precise control, which is used, based on the various sources and calculation methods. The available options are:

- **Master source**
The SOC of the device, which was selected under the "Data Source (Master)", is transmitted to the inverter.

- **Soc average**
The average of the SOC from all devices selected under "BMS for SoC" is calculated and transmitted to the inverter.

- **SOC minimal value**
The lowest SoC value of the devices selected under "BMS for SoC" is transmitted to the inverter.

- **SOC maximum value**
The highest SoC value of the devices selected under "BMS for SoC" is transmitted to the inverter.

- **BMS**
The SOC of a single device selected under "BMS for SoC" is used. If several devices have been selected, the SOC of the first selected device is transmitted.

These settings enable flexible adaptation of the SOC data that are sent to the inverter.

### Base data
#### Absorption charging voltage
The **Absorption charging voltage** describes the voltage that is necessary to bring batteries into a (almost) fully charged condition. It should be noted that this voltage should not be permanent, as this can negatively affect the service life and performance of the battery.

A suitable point in time to switch from **Absorption charging voltage** to **Float tension** exists if the electricity remains very low over a longer period of time.

In order to automatically control this transition, the "**Charge-caused cut-off**" function is available, which is described below. Without this function, the battery remains permanently on the absorption voltage, which can lead to damage in the long term.

This setting is therefore essential to correctly end the charging process and optimally protect the battery.

#### Float charging voltage
The float charging voltage indicates the open circuit voltage (OCV), i.e. the voltage that a battery reaches when it is in an unencumbered condition and is not loaded.

Essentially, the float charging voltage corresponds to the voltage value in which the battery lies in a stable, unused state without being unloaded or charged. This condition occurs when there is no load on the battery and no energy flows into or out of the cell.

#### Batterpack settings
With this function you can avoid a loading or discharge overflow if individual battery packs are switched off in the system.

The Battery Safety Controller (BSC) ensures that the previously defined maximum loading and discharge current is transmitted to the inverter. Depending on the number of packs connected in parallel, you must specify this electricity value individually. If a Battery Management System (BMS) intervene and take the pack from the network, it is possible to take over the remaining packs to take over the full stream of the unusual pack. This could lead to an overflow.

To prevent this, you can use this function to define a maximum current per pack. The BSC reacts automatically to the failure of a pack and adapts the maximum current to the remaining packs, so that the current never exceeds the specified value.

Example: Suppose you have defined a maximum charging current of 180a and three packs, each defined a maximum current of 100a. If a pack fails, the remaining electricity of 200A would still be within the permissible framework. If another pack fails, the charging controller would automatically limit the current to 100a to protect the remaining pack from an overcurrent.

This function ensures that your system always works safely even if individual packs fail and no overcurrent situations arise.


### Trigger at SOC
With this function you can, for example, switch external device depending on the SoC value.
![](img/settings/settings_inverter_trigger_soc.png) {Width = "950"}

**Two examples of this:**
![](img/settings/settings_inverter_trigger_soc_beispiel.png) {Width = "450"}


Triggered here ...

* Rule0 a relay for an MPPT charging controller
  * <= Turn on 89%
  * > = Switch off 90%

* Rule1 a relay for a charger of an offgrid system
  * <= Switch on 10%
  * > = Switch off 25%

The charger starts at 0% until the 25% are reached and then switches off. It is only started again at 10% and smaller.
So you have a hysteresis of 15%.

## Batch
Example of a charging cycle including balancing, float and absorption voltage with the help of the BSC and a visualization via home assistant/Grafana:
![](img/settings/settings_inverter_charge_beispiel.png) {Width = "1300"}

### Charging current per pack too big
![](img/settings/settings_inverter_current_per_pack.png) {Width = "450"}
With this function, the charging current is automatically and dynamically adjusted to ensure that the maximum loading value of each battery pack is not exceeded. This intelligent regulation protects the battery from overflow.

The following graphic illustrates the streams of three battery packs during a charging process:
![](img/settings/settings_inverter_current_per_pack_example_1.png) {Width = "600"}
Green shows the current for pack 1, yellow of pack 2 and blue of Pack 3.

It can be seen in the presentation that the maximum load current for Pack 1 (green) was reduced to 50a for a short time (this is visible in the middle of the diagram). After the value has been reduced, the (BSC) regulates the charging current dynamically and holds it on the set value of 50a.


### Depending on the charging stream, throttling depending on the tension
These settings make it possible to reduce the charging current when certain cell stresses are exceeded. This helps to protect the cells from overloading.

* **On off:** Activate or deactivate the function.
* **Start greater with cell tension:** indicates the cell tension in which the throttling of the charging current begins.
* **Maximum cell voltage:** From this cell voltage, only with the minimum charging current is loaded.
* **Minimum charging current:** The lowest electricity that is used during charging.

### Reduce charging current at cell drift
This function reduces the charging current based on the cell tension difference (drift) to ensure a even load of the cells.

* **On off:** Activate or deactivate the function.
* **Start greater with cell tension:** Cell voltage from which the reduction of the charging current begins.
* **Start greater at Drift:** The voltage difference between cells, in which the reduction starts.
* **Reduction per further MV deviation:** Electricity reduction for any further MV deviation in cell voltage difference compared to the starting definition set.

### Reduce charging current - SoC
The charging current is reduced when the loading status (State of Charge, SoC) exceeds a certain value.

* **On off:** Activate or deactivate the function.
* **Reduction from SOC:** The charge status (SoC), from which the charging current is reduced.
* **Reduce per 1% by x A:** indicates how much the electricity per 1% SoC is to be reduced.
* **Minimum charging current:** The lowest electricity that is used during charging.

### Dynamic charging limit limitation (beta!)
This experimental function limits the charging voltage based on the cell tension and the tension difference between the cells.

* **On off:** Activate or deactivate the function.
* **Start cell voltage:** Cell voltage from which the limitation becomes active.
* **Tension delta min/max:** The maximum difference between the lowest and highest cell tension.

### Voltage control for charging current limitation
> These functions are only available insiders

As soon as the function is activated, the charging voltage is dynamically adjusted to keep the charging current within the configured corridor. If the charging current exceeds or fall below the defined area, the voltage control intervenes and corrects the voltage accordingly. In addition, the charging current transmitted to the inverter is set to 0 A.

The regulation comes into force only if the autobalancer is not active.

The diagrams show a Victron system with activated voltage control. It is clearly recognizable that the charging current is limited and no energy flows into the battery. Instead, the excess energy is fed into the network, while the SOC (State of Charge) remains almost constant over time.
![](img/settings/settings_inverter_SpgRegLadestrombegrenzungGrafana.png) {Width = "950"}
![](img/settings/settings_inverter_SpgRegLadestrombegrenzungVrm.png) {Width = "950"}

**Setting options:**

* **On off:** The regulation can either be activated or deactivated permanently.
Alternatively, it is only possible to activate it if a defined trigger condition is met. This allows the control to be integrated into a home automation system, for example, so that it is only active in summer and the full capacity of the battery is available in winter.
* **Active off (SoC):** Here you can determine which load status (State of Charge, SoC) comes into force. This enables targeted adaptation to different requirements.
* **Regulation corridor (±):** defines the permissible fluctuation area for charging current. There is no regulation within this corridor. Over- or falls below the charging current this area, the charging voltage is automatically adjusted.

**Areas of application:**
The function makes it possible to load the battery only up to a certain SoC in order to extend its lifespan.


### Autobalancer
The autobalance feature takes over the full balancing of your battery cells to ensure optimal performance and lifespan of the battery. The most important settings and processes are described below:
![](img/settings/settings_inverter_charge_autobalance.png) {Width = "950"}

**Autobal. Start (trigger)** *(This option is only available insiders)*
The trigger configured here makes it possible to start the autobalancer immediately if it is currently in the waiting time until the next interval. It should be noted that the trigger has to be put back on "low" after the start of the autobalancer.

**Balance interval**
With the parameter balance interval you can determine the time intervals in which the battery cells should be carried out. This value determines how often the balancing is activated to adjust the cell stresses.

**Start criteria**
The balancing process begins automatically when the defined balance interval has expired and the start cell voltage was reached in the second step.
The highest cell voltage of the configured data devices is taken for the start cell voltage.
These starting conditions ensure that the balancing is carried out under optimal conditions.

**Balance minimum time**
The parameter balance minimum time indicates how long the balancing should be carried out at least, regardless of whether the cell voltages have already been balanced. This prevents the duration of balancing that is too short and ensures that the cell tension is thoroughly adjusted.

**Balance charging voltage**
For the balancing process, the charging voltage of the system is increased to the previously defined balance charging voltage. This tension ensures that the balancing process can be carried out effectively.

**Balance cell voltage**
The parameter balance cell voltage indicates how high the voltage of the individual cells can increase as a maximum during the balancing process. This prevents an overload of the cells and protects the battery system from damage.

**Disconnecting the balancing process**
The process is ended automatically as soon as the difference between the cell tension reaches or falls below the set. This ensures that all cells are loaded evenly and there is no excessive disparity.

**Time-out**
The Timeout parameter determines the maximum time the balancing process is automatically canceled if the cell stresses could not be compensated for within the intended time frame. This protects the system from endless balancing cycles.

**Extended options**
> Note: The extended options are only available in the [Insider Version](insider.md)

- **Ballance-spg. send as soon as the start time reaches**
When this option is activated, the balance voltage is sent as soon as the set starting time is reached.
- **For start cells-to-do-it-all → Step 'Wait for Start-Zellspg.'**
If this option is active, when the defined start cell voltage is fallen below, switching again to the step *"Wait for Start-Zellspg."*. This also resets the ongoing timers.
- **Cutoff from Step 'Wait for Start-Zellspg.' deactivate**
With this option, the Cutoff function is already deactivated in the step *"Wait for Start-Zellspg."*.

**After balancing**
After completing the balancing process, the charging voltage is lowered to the floating level in order to keep the battery in the loaded condition without further loading it.

This autobalance feature offers an automated solution to balance the battery cells regularly and thus maximize the efficiency and lifespan of the battery.

**References**

* After a restart of the BSC, there is no waiting time until the first balancing. The set balance interval only starts after the first balancing.
* If the BSC was started at 10 p.m. and an interval of five days is set, it will not balance the morning of the fifth day, but only the closest when the sun goes up again!  Because the balances would only be sharpened on the evening of the fifth day
* For different BMS, e.g. the seplos, the adjustable minimum time can be used to set the SOC 100

The exact process of the balance process can be visualized with the MQTT-Topic "/Inverter/Autobalstate".
Function of the five states available:

  - 0: Autobalancing is deactivated
  - 1: BSC is waiting for the next start time
  - 2: Balancing did not finish and it will be repeated the next day
  - 3: start time reached; BSC is waiting for the start cell voltage
  - 4: Start cell voltage reached; Car blancing is now active
  - 5: Celldif. Finished was reached, but the balance charging voltage has not yet been reached
  - 6: Balance charging voltage reached; Wait until the minimum time expired

### Charge-caused cut-off
This function interrupts the charging current when it lies for a certain period of time below a set electricity value.
After this demolition, the target charging voltage used so far is placed from the absorption voltage to the float tension.

* **On off:** Activate or deactivate the function.
* **Cut-off time:** Time period in which the charging current must be below a certain value before it is set to 0 A.
* **Cut-off electricity:** The cut-off current is the overall charging current, below which the cut-off time begins. The total charging current has been calculated as a mean since the set start cell voltage (if available) has been exceeded.
If the average of the overall charging current exceeds the cut-off current again during the process, both the timer and the mean.
* **Start cell voltage:** The start cell voltage is the voltage from which the cut-off control becomes active. As soon as this has been exceeded and the cut-off current is undercut, the timer remains active.
Another falling below the start cell voltage does not lead to the termination of the timer. The timer is only reset when the cut-off current is exceeded.

### SOC when falling below the cell tension
This function controls the reloading of the cells based on the cell tension.

* **On off:** Activate or deactivate the function.
* **Cell voltage in the loading start:** Cell voltage where reloading starts.
* **Cell voltage loading:** Cell voltage in which reloading ends.
* **SOC:** Charging status that is sent to the inverter during reloading.
* **Blocking time between two discharges:** Time that has to pass between two discharges.

## Discharge
### Discharge stream of the cell voltage-dependent
![](img/settings/settings_inverter_discharge_cellvoltage.png) {Width = "450"}

This function serves to adapt the discharge current based on the cell tension in order to extend the lifespan of the battery cells and to ensure their safety.

- **On off** (Activation of the throttle)
This option enables the cell voltage-dependent throttling to be switched on or off.
When activated, the discharge current is adapted depending on the cell tension.

- **Start smaller than**
Here a threshold is determined, when the reduction of the discharge current is activated.
As soon as the lowest cell voltage falls below this value, the throttling is put into force so as not to unload the cells too much.

- **End cell tension**
This value determines the cell voltage, when the discharge flow is reduced to the "minimum exposure current".
> Note: The end cell voltage value must always be set smaller than the cell start voltage!

- **Minimum enthusiasm**
This is the minimal discharge current, which is not below the end of the cell tension.
