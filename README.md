
# FanControllerESP32 

### This project aims to control a fan using a Python script in conjunction with an ESP32 board.

> #### Disclaimer: This project is completely amateur; I am not a programmer.

Logic: Script to define the rotations per second (RPM) the fan should operate at;<br>
The script will provide JSON with five data points: Temperature, CPU Load, Total RAM, RAM Usage, and Target Fan RPM.

```   
    	{
    	"t": 63,	# Temperature
    	"l": 8.0,	# CPU Load
    	"tr": 19.7,	# Total RAM	
    	"ur": 11.6,	# RAM Usage
    	"r": 51		# Target RPM

    	}
```
For fan control, only the target RPM would be necessary, but I also want to include an e-paper display showing some information on the machine's case.


