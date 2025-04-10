# Rest API documentation

## References
- All endpoints deliver JSON data.
- The API does not need authentication.

## Endpoints

### 1. System data [get]
End point: `/restapi`

**Description:**
This end point enables the controller to be called up by various system data. The answer contains information about the system state, data sent to the inverter, as well as data from the connected data devices.

**Answer format:**
This is just an extract from the answer and not complete!
`` `Json
{
"System": {
"FW _Version ":" T0.8.0_ T9",
"FW _add ":" serial_ Log",
"HW_Version": "2",
"Name": "BSC",
"Time": "2025-04-03 06:10:39",
"Boottime": "2025-04-01 21:01:46",
"System": 0,
"MQTT": 0,
"RSSI": 23},
"Trigger": {
"0": 0,
"1": 1,
"2": 0,
"3": 0},
"Inverter": {
"Current": 66.30,
"Voltage": 55.30,
"SOC": 14},
"Data_Device": [
{"Name": "Neey 1", "Cells": 18, "Total Volt": 0.00, "Total Curr": 0.00, "Soc": 0},
{"Name": "Seplos 1", "Cells": 18, "Total Volt": 55.30, "Total Curr": 22.10, "SoC": 85}
]
}
`` `

### 2. All Active-Nerrors [GET]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/errors/all`

**Description:**
This end point returns all possible errors of the system, including a label, whether you are currently active or not.

**Answer format:**
`` `Json
{
"Errors": [
{"ID": 1, "State": False, "Text": "Data Device 0 Error"},
{"ID": 2, "State": False, "Text": "Data Device 1 Error"},
{"id": 20, "state": false, "text": "canbus error"}
]
}
`` `

### 3. Active reror [get]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/errors/active`

**Description:**
This end point only returns the system that is currently active. The format is identical to `/restapi/errors/all`, but contains only entries with `"state": true`.

**Answer format:**
`` `Json
{
"Errors": [
{"ID": 20, "State": True, "Text": "Canbus Error"}
]
}
`` `

### 4. IO data [get]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/io`

**Description:**
This end point returns the condition of the digital inputs (DI) and relay.

**Answer format:**
`` `Json
{
"Di": [0, 0, 0, 0],
"Relay": [0, 0, 0, 0, 0, 0]
}
`` `

### 5. Vtrigger [Post]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/vTrigger`

**Description:**
This end point allows the virtual trigger to be set.

**Expected input format:**
`` `Json
{
"ID": [Trigger NR],
"Value": [0 | 1]
}
`` `

**Example call with `curl`**:
Windows:
`` Bash
CURL -L -X Post "http://[BSC IP]/RESTAPI/Vtrigger" ^
-H "Content-Type: Application/Json" ^
-d "{\" id \ ": 6, \" value \ ": 0}"
`` `

Linux:
`` Bash
CURL -L -X Post "http://[BSC IP]/RESTAPI/Vtrigger" \
-H "Content-Type: Application/Json" \
-d "{\" id \ ": 6, \" value \ ": 0}"
`` `

