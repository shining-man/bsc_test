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
```json
{
  "system": {
    "fw_version": "T0.8.0_T9", 
    "fw_add": "SERIAL_LOG", 
    "hw_version": "2", 
    "name": "bsc", 
    "time": "2025-04-03 06:10:39", 
    "boottime": "2025-04-01 21:01:46", 
    "system": 0, 
    "mqtt": 0, 
    "rssi": 23},
  "trigger": {
    "0": 0, 
    "1": 1, 
    "2": 0, 
    "3": 0},
  "inverter": {
    "current": 66.30, 
    "voltage": 55.30, 
    "soc": 14},
  "data_device": [
    {"name": "NEEY 1", "cells": 18, "totalVolt": 0.00, "totalCurr": 0.00, "soc": 0},
    {"name": "Seplos 1", "cells": 18, "totalVolt": 55.30, "totalCurr": 22.10, "soc": 85}
  ]
}
```

### 2. All Active-Nerrors [GET]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/errors/all`

**Description:**
This end point returns all possible errors of the system, including a label, whether you are currently active or not.

**Answer format:**
```json
{
  "errors": [
    {"id": 1, "state": false, "text": "Data Device 0 Error"},
    {"id": 2, "state": false, "text": "Data Device 1 Error"},
    {"id": 20, "state": false, "text": "CANBUS Error"}
  ]
}
```

### 3. Active reror [get]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/errors/active`

**Description:**
This end point only returns the system that is currently active. The format is identical to `/restapi/errors/all`, but contains only entries with `"state": true`.

**Answer format:**
```json
{
  "errors": [
    {"id": 20, "state": true, "text": "CANBUS Error"}
  ]
}
```

### 4. IO data [get]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/io`

**Description:**
This end point returns the condition of the digital inputs (DI) and relay.

**Answer format:**
```json
{
  "di": [0, 0, 0, 0],
  "relais": [0, 0, 0, 0, 0, 0]
}
```

### 5. Vtrigger [Post]
> Note: This end point is only available in the [Insider Version](insider.md).

End point: `/restapi/vTrigger`

**Description:**
This end point allows the virtual trigger to be set.

**Expected input format:**
```json
{
  "id": [Trigger Nr],
  "value": [0|1]
}
```

**Example call with `curl`**:  
Windows:  
```bash
curl -L -X POST "http://[BSC IP]/restapi/vTrigger" ^
-H "Content-Type: application/json" ^
-d "{\"id\":6,\"value\":0}"
```

Linux:  
```bash
curl -L -X POST "http://[BSC IP]/restapi/vTrigger" \
-H "Content-Type: application/json" \
-d "{\"id\":6,\"value\":0}"
```

