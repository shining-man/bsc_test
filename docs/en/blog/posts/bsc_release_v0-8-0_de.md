---
date: 2025-04-06
authors: [Shiningman]
categories:
  - Release Notes (insider)
---

[IMG _Dashboard]: Release_ V0-8-0_de/Dashboard.png
[IMG _Charging current limitation grapha]: Release_ V0-8-0_de/charging current limitation grafana.png
[IMG _Charging current limit of_ V0-8-0_DE/charging current limitation vrm.png

# Version 0.8.0 (DE)
This version brings with it some improvements and extensions, especially the new **Dashboard**. Below is an overview of all changes since the last stable version:

## 🌐 dashboard
One of the biggest changes is the new dashboard. At a glance, it shows all system -relevant information and live data.

<!-- more -->

! [IMG_Dashboard]

## ✨ new functions

- **Plausibility test for text input fields in the webui**
This function increases input safety and reduces configuration errors.

- **Immediate start of the autobalancer per trigger**
The autobalancer can now also be started directly via a trigger, which makes the process more flexible.

- **Additional options for the autobalancer**
The autobalancer now offers additional options to better adapt it to specific requirements.
    - **Ballance-spg. send as soon as the start time reaches**
With this option, the balance voltage is sent as soon as the set starting time is reached.
    - **For start cells-to-do-it-all → Step 'Wait for Start-Zellspg.'**
With this option, when the defined start cell voltage is fallen below, the step is "Wait for Start-Zellspg." changed. This also resets the ongoing timers.
    - **Cutoff from Step 'Wait for Start-Zellspg.' deactivate**
With this option, the Cutoff function is already in the step "Wait for Start-ZellSPG." Deactivated.


- **Dynamic voltage control to limit the charging current**
With this function, the charging voltage is dynamically adjusted to keep the charging current within the configured corridor. If the charging current exceeds or below the defined area, the voltage is automatically corrected.  <br> <br>
This function makes it possible to load the battery only up to a certain SOC (State of Charge) in order to extend its lifespan.  <br> <br>
The diagrams show a Victron system with activated voltage control. It is clearly recognizable that the charging current is limited and no energy flows into the battery. Instead, the excess energy is fed into the network, while the SoC remains almost constant over time. <br>
! [IMG_LADESTROM LITTION GRAFANA]
! [IMG_LADESTROM LITTION VRM] <br>

- **Support of the Pace PC200 via RS232**
The device can now also be read out via the serial interface (RS232).

## 🔌 Rest API extensions

- **New Rest-Endpoint: `/restapi/io`**
From now on, digital inputs and relay status can be queried via this new REST Endpoint.

- **Set `vTrigger` via the rest of the API**
This extends the control options via external systems and enables more flexible integration.

## 🛠️ Adjustments & bug fixes

- **Adjustment of the temperature range for alarm rules**
The temperature range for the alarm rules has been optimized.

- **Removal of data syrups in "Reduce charging current - SoC"**
A problem with the data types in connection with the SOC loader regulation has been fixed.

- **Troubleshoot when reading out the PIC data at SeplosV3**
A problem when reading the PIC data was fixed for the SeplosV3 platform.
