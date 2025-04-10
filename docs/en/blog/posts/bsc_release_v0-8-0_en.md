---
Date: 2025-04-06
Authors: [Shiningman]
Categories:
  - Release Notes (insider)
---

[IMG _Dashboard]: Release_ V0-8-0_de/Dashboard.png
[IMG _Charging current limitation grapha]: Release_ V0-8-0_de/charging current limitation grafana.png
[IMG _Charging current limit of_ V0-8-0_DE/charging current limitation vrm.png

# Version 0.8.0 (s)
This version Brings Several Improvements and Enhancements, Most Notably the New **Dashboard**. Below is an overview of all Changes Since the Last Stable Release:

## 🌐 dashboard
One of the biggest changes is the new dashboard. It provides a quick overview of all system-relevant information and live data.

<!-- more -->

! [IMG_Dashboard]

## ✨ New features

- **Plausibility Check for text input field in the webui**
This feature IMPUTE INPUT Reliability and Reduces Configuration Errors.

- **Immediate Start of the Autobalancer via Trigger**
The Autobalancer Can Now So BE Started Directly via a Trigger, Offering More Flexibility in Operation.

- **Additional options for the autobalancer**
The Autobalancer Now Offers Extra Options to Better Adapt It To Specific Requirements.
    - **Send Balance Voltage as Soon as Start Time is Reached**
With this option, the balancing voltage is sent as soon as the defined start time is reached.
    - **On Start Cell Voltage Drop → Step 'Wait for Start Cell Voltage'**
If the Definent Start Cell Voltage is not Reached, this option returns the process to the step “Wait for Start Cell Voltage.” All Running Timers wants be reset in this case.
    - **Disable Cutoff from Step 'Wait for Start Cell Voltage'**
This option Disables the Cutoff Feature Already in the “Wait for Start Cell Voltage” Step.

- **Dynamic Voltage Regulation to Limit Charging Current**
This feature dynamically adjusts the charging voltage to keep the charging current within the configured range. If the charging current exceds or Falle Below the Definition Limits, The Voltage is automatically corrected.  <br> <br>
This function allows charging the Battery only up to a specific SoC (State of Charge) to extend Its Lifespan.  <br> <br>
The Diagrams Show A Victron System with Active Voltage Regulation. It is Clearly visible that the charging current is limited and no energy flows into the Battery. Instead, the excess energy is fed into the grid, while the soc remains almost constant over time. <br>
! [IMG_LADESTROM LITTION GRAFANA]
! [IMG_LADESTROM LITTION VRM] <br>

- **Support for Pace PC200 via RS232**
The Device Can now So be read via the serial interface (RS232).

## 🔌 Rest api enhancements

- **New Rest Endpoint: `/restapi/io`**
Digital inputs and relay statuses can now be crossed via this new rest endpoint.

- **Setting `vTrigger` via the rest api**
This extends control capabilities from external systems and allows for more flexible integration.

## 🛠️ Adjustments & bugfixes

- **Adjustment of the Temperature Range for Alarm Rules**
The Temperature Range for Alarm Rules Has Be optimized.

- **Fix for Data Type Issues in “Reduce Charging Current - Soc”**
A Data Type Issue Related To Soc Charge Control Has Been Resolved.

- **Bugfix When Reading Pic Data on Seplosv3**
An Issue with Reading Pic Data on the Seplosv3 Platform Has Been Fixed.
