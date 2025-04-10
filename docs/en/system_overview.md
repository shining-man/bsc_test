## System overview
The BSC is a freely configurable controller that realizes an interface between the different components of a DIY battery system. It can take on a variety of control and monitoring tasks, including the central charging control of the storage system or the implementation of a second security level next to the BMS.

`` `Mermaid
%% {init: {
'Theme': 'Base',
'Themevariables': {'fontsize': '16px', 'fontfamily': 'Arial', 'Edelabelbackground': 'White'}
}} %%


Flowchart TD
BMS [BMS]-"RS485"-> BSC [Serial 0-2]
TEMP_SSESOR [Temperature <br> Sensors] -OneWire -> BSC
Neey [Neey <br> Balancer] <-- Bluetooth --> BSC [Bluetooth]
VICTRON _Shunt [Victron <br> Smartshunt] -> Victron_ Shunt_conv [RS485 <br> Converter] -RS485 -> BSC
BSC -Can -> Can [inverter]
BSC [MQTT] <-- MQTT --> MQTT_BROKER [MQTT Broker]
BSC [REST API] -REST -> REST [REST Client]

BSC [Extension <br> Interface] -.- E1 [<a href='hardware.md#bsc-display'> DISPLAY </a>]
Se ["serial <br> extension [MDPROTECT1](Serial 3-10)"] -.- BSC <br>
BMS -RS485 -> SE

BSC [Battery Safety Controller] ::: Wide
    
Subgraph Battery
BMS
Temp_ensor
Nice
Victron_shunt
end

Classdef Wide Padding: 200px
Style BSC Fill: #FFDBAA
`` `

## Components
* **BSC:** The device consists of a board and the software running on it. It has a wide variety of interfaces to be able to communicate with the external components (WLAN, Bluetooth, RS485, CAN-BUS, OneWire, digital inputs and outputs, as well as an analog input)
* **Display:** Optionally, a display can be connected to the BSC, which communicates with the BSC via an I2C bus. Further information can be found [hier im Wiki](hardware.md#bsc-display). It is advisable to operate BSC and display in [diesem Gehäuse](https://bsc-shop.com/produkt-kategorie/gehaeuse/).
* **Serial extension:** The BSC has 3 RS485 interfaces for the connection of BMS. If more are required, the Serial Extension Board can be connected to the BSC to get 8 more RS485 interfaces. See [das entsprechende Github-Repo](https://github.com/shining-man/bsc_extension_serial)
* **BMS:** Different BMS can be connected via RS485, CAN or Bluetooth. Current state information from the batteries, such as cell stresses, SoC or temperatures, are then called up of these. See [hier im Wiki](devices/bms.md)
* **Temperature sensors:** Additional temperature sensors can be connected via OneWire or digital or analog inputs that complement the information of the connected BMS.
* **Balancer:** Balancer from NEEY can be controlled by the BSC, including calling up the current state information and control of the balancer.
* **Shunt:** The BSC can call up the SoC of a battery from an external shunt. A Victron Smartshunt is currently supported. Since this only communicates via Uart, an additional RS485/UART KONVERTER is required.
See [hier im Wiki](devices/externer_shunt.md)
* **Inverter:** The BSC communicates with various inverters via CAN bus, such as Victron, Solis or Deye. The current battery status can also be reported and configuration parameters, such as the charging control, can also be set.
See [hier im Wiki](devices/wechselrichter.md)
* **MQTT Broker:** All condition data can also be sent to a MQTT broker via WLAN to save and visualize it in the long term (e.g. via Grafana).
See [hier im Wiki](mqtt.md)
* **Rest client:** Condition data via the monitored batteries or via the BSC can be called up via an HTTP REST API.
See [hier im Wiki](settings_bsc.md#derzeit-aktive-inverter-drosselung)

## Available interfaces
* **WLAN:** Access to the BSC web interface, transmission of MQTT data
* **Bluetooth:** ~~ Communication with Neyy-Balancer ~~
* **RS485:** Reference of BMS data
* **Can bus:** Reference of BMS data, communication with inverters
* **Http rest:** Reference of battery and BSC status information
* **OneWire:** Reference of sensor data, such as temperature sensors
* **Digital inputs:** Reception of digital sensor data via a galvanically separate entrance
* **Analog entrance:** Receiving analog sensi -data via a galvanian entrance
* **Digital outputs:** Control of external devices via relay
