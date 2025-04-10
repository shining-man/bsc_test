## Info videos
[www.youtube.com/@shining-man](http://www.youtube.com/@shining-man)
** Please note: Due to the further development of the BSC, there is no longer everything in the video!
The "New Webui" mentioned in the video is currently not available. Not even for sponsors! **

## Further information
For initial information and the commissioning first read the following further chapters:
[Hardware](hardware.md)
[Konfiguration des BSC](settings_bsc.md)

If you want to test the BSC software without original hardware, you should have the chapter
[Test ohne orig. Hardware](BSC_ohne_orig_hardware.md) Read.

High armor or frequent problems are described in the chapter [Troubleshooting](troubleshooting.md).

## Installation of the firmware
### Flashes of a Lilygo circuit board
The current circuit breaker sends this with a special firmware that must be brought to the current release at the customer.
To do this, first download the current release (BSC_Firmware.zip) from [hier](https://github.com/shining-man/bsc_fw/releases) to unzip it.  Now you will find a file called "firmware.bin" that represents the firmware to be flashed.

Upgrading the firmware happens as follows:

1. When the firmware starts for the first time, the BSC provides a WLAN access point with the name "ESP*" (without WLAN pass phrase). Please connect to this WLAN now.
2. Now call the web address "http://192.168.4.1/update". Pay attention to the exact entry of the URL.
If a smartphone is used, the web address could not be dissolved. If this problem should occur, please switch off the mobile data of the smartphone for the process.
3. Now upload the previously unpacked file "firmware.bin". Other files, such as the file system, are not required.
4. Now it takes a few seconds for the device to restart.
5. If the process was successful, an LED flashes on the board. You can now connect to the BSC, as described [MDPROTET0], to carry out your configurations.

### Flashes of an unprogrammed board
* The four downloadable files must be flashed manually for the initial commissioning of an unprocessed board.
The current releases can be found [hier](https://github.com/shining-man/bsc_fw/releases).
For this purpose, a USB-serial converter with **3.3V level** must be connected to the BSC hardware on the three-pole pen strip J2 (labeled with "prog").
A 5V converter can damage the controller.

A USB port is usually available directly with the ESP32 DEV boards. Later updates can be made via the web interface.

* Before flashing the firmware, the board must be transferred to download mode. To do this, separate the power supply, put jumper J4 and switch on the power supply. After successful flashes, the jumper J4 must be removed again so that the board runs normally.
* PCB version> = V2.3: The jumper J6 may not be stuck during flashen, but must then be put back.
* You can use 921600Baud as a baud rate. If this leads to problems, it can also be down on 230400Baud
* Please delete the current memory of the module before programming using the following tools.

### Flash opportunities
#### Use of the manufacturer download tool (Only Windows)
The software for flash (flash download tools) can be obtained from the manufacturer's website of the ESP32 via [diesen Link](https://www.espressif.com/en/support/download/other-tools).
In this software, the settings, as shown in the following screenshots, must be made:

![bsc](img/download_tool_mode.png)

The firmware files must be stored in the following screen and a few settings must be made.
Make sure that the ticks are set next to the individual files and the respective line was stored green.
![bsc](img/download_tool.png)

➔ Now you can start the upload process with a click on "Start".

#### Flashes with the ESPOOL (Linux, Windows) including the previous deletion
`esptool.py  --port /dev/ttyUSB0 --chip auto write_flash -e -ff 80m -fm dio 0x01000 bootloader.bin 0x08000 partitions.bin  0x0e000 boot_app0.bin 0x10000 firmware.bin`

#### Flash over the browser
When using a Chrome browser, the [Online-Tool](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/) provided by Adafruit can also be used for flash.

After a successful connection to the controller, the 4 files of the current firmware can be flashed with the appropriate target addresses:

* bootloader.bin - 0x1000
* partition.bin - 0x8000
* boot_app0.bin - 0xE000
* firmware.bin - 0x10000

##### Beta versions flash
There are two options for flashing beta versions:

1. You can flash the individual beta-firmware "firmware.bin" directly via the web browser and the OTA functionality within the BSC weaving front end.
You can find this in the menu /settings /update.
2. Otherwise you can use the respective "firmware.bin" together with the three other files from the release.
The overall flash procedure described above remains unchanged.

## Connect to the BSC
The prerequisite is that the board is programmed!

*When the firmware starts for the first time, the BSC sets an AccessPoint with the name "BSC_* ".
* After connecting to the AccessSpoint, this can be reached under the IP address 192.168.4.1 or BSC.info and can be configured.
* Access data:
    - Username: BSC
    - Password: admin
