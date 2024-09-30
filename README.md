# Real-Time Patient Monitoring App (Raspberry Pi)

## OVerview 
This project is a real-time patient monitoring system that runs on a Raspberry Pi, using sensors like a heart rate sensor and a pulse oximeter connected to the Pi’s GPIO pins. The Raspberry Pi collects vital signs data (e.g., heart rate, oxygen saturation), processes it, and visualizes it in real time. It also features anomaly detection (e.g., abnormal heart rate) and data logging.

## Features
* **Sensor Integration**: Collects real-time data from health sensors such as a heart rate monitor and pulse oximeter.
* **Direct GPIO Communication**: Interfaces directly with the Raspberry Pi's GPIO, I2C, and SPI pins to read sensor data.
* **Real-Time Data Visualization**: Displays real-time graphs of heart rate and SpO2 using matplotlib.
* **Anomaly Detection**: Detects abnormal readings (e.g., high/low heart rate) and triggers alerts.
* **Data Logging**: Stores sensor data in an SQLite database for historical analysis.

## Hardware requirements
* **Raspberry P**i: Any Raspberry Pi model with GPIO pins (Raspberry Pi 3, 4, Zero W, etc.).
* **Pulse Oximeter Sensor**: MAX30100, MAX30102, or MAX30105.
* **Heart Rate Sensor**: Pulse Sensor (or equivalent).
* **MCP3008 ADC**: To read analog signals from the Pulse Sensor (since Raspberry Pi lacks analog inputs).
* **Wires and Breadboard**: To connect the sensors and ADC to the Raspberry Pi.

## Software requirements
* Raspberry Pi OS: Make sure you have Raspberry Pi OS installed.
* Python 3.x: Installed on your Raspberry Pi.
* Python Libraries:
    * RPi.GPIO: For GPIO pin control.
    * spidev: For SPI communication with the MCP3008.
    * Adafruit-Blinka: For I2C and SPI device support.
    * adafruit-circuitpython-max30100: For interfacing with the MAX30100 pulse oximeter.
    * matplotlib: For real-time data visualization.
    * sqlite3: For data storage in a local SQLite database.
    * tkinter: For creating a graphical user interface (GUI).

Install Required Python Libraries:
* Run the following commands to install the necessary dependencies:
```
sudo apt-get update
sudo apt-get install python3-smbus python3-dev i2c-tools
pip3 install RPi.GPIO spidev Adafruit-Blinka Adafruit-MCP3008 adafruit-circuitpython-max30100 matplotlib sqlite3 tkinter
```

## Wiring Guide
1. Pulse Oximeter (MAX30100/MAX30102) to Raspberry Pi (I2C):
    * VCC → 3.3V or 5V on Raspberry Pi.
    * GND → Ground on Raspberry Pi.
    * SCL → GPIO 3 (SCL, Pin 5).
    * SDA → GPIO 2 (SDA, Pin 3).

2. Heart Rate Sensor (Pulse Sensor) to Raspberry Pi (Analog via MCP3008):
    - Since the Raspberry Pi does not have analog pins, you need to use an MCP3008 ADC to read the analog signal from the heart rate sensor.

    * Pulse Sensor:
       * VCC → 3.3V (or 5V) on Raspberry Pi.
       * GND → Ground on Raspberry Pi.
       * Signal → Connect to MCP3008 channel (CH0).
    
    * MCP3008 to Raspberry Pi:
      * VDD → 3.3V.
      * VREF → 3.3V.
      * AGND → Ground.
      * DGND → Ground.
      * CLK → GPIO 11 (SCLK, Pin 23).
      * DOUT → GPIO 9 (MISO, Pin 21).
      * DIN → GPIO 10 (MOSI, Pin 19).
      * CS/SHDN → GPIO 8 (CE0, Pin 24).
     
## Installation & Setup
### 1. Enable I2C and SPI on Raspberry Pi:
1. Run sudo raspi-config to open the Raspberry Pi configuration tool.
2. Navigate to Interfacing Options and enable I2C and SPI.
3. Reboot the Raspberry Pi to apply the changes:
```
sudo reboot
```

### 2. Python application setup
1. Clone or Download this repository on your Raspberry Pi
```
git clone https://github.com/Karolkalex/monitoring_app-raspberry.git
cd patient_monitoring_app
```
2. Run the Application: Execute the Python application to start reading and visualizing data from the sensors:
```
python3 app.py
```

## Project Structure
- patient_monitoring_app/
- │
- ├── app.py              # Main application entry point
- ├── sensor.py           # Raspberry Pi sensor communication (I2C, SPI)
- ├── data_processing.py  # Data processing and anomaly detection
- ├── visualization.py    # Real-time data visualization with matplotlib
- ├── database.py         # Database interaction (SQLite)
- └── gui.py              # Graphical User Interface (Tkinter)

### File Descriptions:
* **app.py**: Coordinates sensor reading, data processing, visualization, and GUI.
* **sensor.py**: Reads data from the Pulse Oximeter (MAX30100) via I2C and the Heart Rate Sensor via SPI (using MCP3008 ADC).
* **data_processing.py**: Processes the sensor data and detects anomalies (e.g., abnormal heart rate).
* **visualization.py**: Real-time visualization of heart rate and SpO2 data using matplotlib.
* **database.py**: Logs sensor data into an SQLite database for historical analysis.
* **gui.py**: Manages the user interface (Tkinter) to display real-time data and alerts.

## How It Works
* Raspberry Pi:
  - The Raspberry Pi collects heart rate and SpO2 data from the sensors connected via I2C and SPI (MCP3008).
* Python Application:
  - Sensor Data Collection: The Pi reads the sensor data using Python libraries like RPi.GPIO, spidev, and adafruit-circuitpython-max30100.
  - Data Processing: The data is processed and checked for anomalies (e.g., heart rate below or above safe thresholds).
  - Real-Time Visualization: The heart rate and SpO2 data is plotted in real-time using matplotlib.
  - Alerts: Alerts are triggered if any anomalies are detected in the sensor readings.
  - Data Logging: All sensor data is logged into an SQLite database for historical review.
 
## Usage
1. Connect the sensors to your Raspberry Pi according to the wiring guide.
2. Enable I2C and SPI on your Raspberry Pi if you haven't done so already.
3. Run the Python application to monitor heart rate and SpO2 data in real time.
```
python3 app.py
```
4. View Real-Time Graphs: The data will be displayed in real-time using a Tkinter GUI, and alerts will appear if any abnormalities are detected.
5. Analyze Historical Data: All data is saved in an SQLite database for further analysis.

## Troubleshooting
* No Data from Sensors: Double-check the wiring of your sensors and ensure I2C and SPI are enabled on your Raspberry Pi.
* Invalid Sensor Readings: Ensure the correct libraries are installed, and the sensors are properly connected. Use i2cdetect -y 1 to verify if the I2C sensor (MAX30100) is recognized by the Raspberry Pi.
* SPI Issues with MCP3008: Ensure that the SPI connections (MOSI, MISO, CLK, and CE) are correctly wired between the MCP3008 and the Raspberry Pi.

## Future Improvements
* Additional Sensors: Add support for other health monitoring sensors, such as temperature sensors (DHT11, DHT22) or ECG sensors.
* Remote Monitoring: Add a web server or cloud integration to remotely access real-time data.
* Mobile Application: Create a mobile app to receive and display the data being collected by the Raspberry Pi.

## License
This project is licensed under the MIT License.

## Contributors
[Carolina Guinart](https://github.com/Karolkalex)
