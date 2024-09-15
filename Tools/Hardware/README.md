# **ESP32 Portable Multimeter with Email Alerts**

## **Overview**

This project is a portable multimeter designed using the ESP32 microcontroller. The primary goal of this multimeter is to monitor voltage outputs from an ATX power supply with three different voltage channels—12V, 5V, and 3.3V. It displays real-time voltage readings on an OLED display and sends email alerts when voltage levels go beyond the standard ATX voltage ranges. The multimeter is compact and capable of sending notifications via email, ensuring timely responses in case of voltage irregularities.

## **Key Features**

- **Three Voltage Channels**: Monitors three voltage outputs: 12V, 5V, and 3.3V, which are standard in ATX power supplies.
- **Real-Time OLED Display**: Displays voltage values on an OLED screen for live monitoring.
- **Email Alerts**: Sends email notifications if the voltage on any of the channels falls outside the defined ATX voltage ranges.
- **Portable and Compact**: Designed to be small and portable, making it easy to integrate into different setups.
- **ATX Power Supply Standards**: Follows the ATX power supply voltage standards for accurate monitoring and alerting.

## **Voltage Standards**

The multimeter monitors the following ATX voltage standards:
- **+12V**: For high-power components like the CPU and GPU.
  - Minimum: 11.4V
  - Maximum: 12.6V
- **+5V**: For I/O devices and storage components.
  - Minimum: 4.75V
  - Maximum: 5.25V
- **+3.3V**: For low-power circuits.
  - Minimum: 3.14V
  - Maximum: 3.47V

## **How It Works**

1. **Voltage Monitoring**:
   - The ESP32 reads the voltage from three separate analog inputs, each connected to a different voltage output of the ATX power supply (12V, 5V, 3.3V).
   - The input voltage is stepped down using a voltage divider circuit before being read by the ESP32 to ensure the input is within its 3.3V range.

2. **OLED Display**:
   - The current voltage values are displayed on a small OLED screen, allowing you to monitor the values in real time.

3. **Email Alerts**:
   - If any of the monitored voltages fall outside the specified ATX range, an alert is immediately sent via email to the specified recipient. This ensures the user is informed of any abnormal voltage behavior.

## **Hardware Requirements**

- **ESP32 Development Board**: Acts as the core controller for reading voltages and sending alerts.
- **OLED Display (128x64)**: Used for displaying real-time voltage values.
- **Resistors (Voltage Divider)**: Used to scale down the voltage readings so that the ESP32 can safely measure them.
- **ATX Power Supply**: Source of the voltages being monitored.
- **Jumper Wires**: For connecting components.
- **Breadboard**: For prototyping connections.

## **Software Requirements**

- **Arduino IDE**: For programming the ESP32.
- **ESP32 Board Package**: To enable ESP32 functionality in the Arduino IDE.
- **Adafruit SSD1306 Library**: For OLED display control.
- **ESP32 MailClient Library**: To send email notifications.
  
## **Installation**

### 1. **Set Up Arduino IDE for ESP32**
   - Install the [ESP32 board package](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/) in Arduino IDE.
   
### 2. **Install Required Libraries**
   - Install the following libraries using the Arduino IDE Library Manager:
     - **Adafruit GFX Library**
     - **Adafruit SSD1306 Library**
     - **ESP32 MailClient Library**

### 3. **Configure Email Settings**
   - Replace the following placeholders in the code with your actual email and WiFi credentials:
     - `your-SSID`: Your WiFi SSID.
     - `your-PASSWORD`: Your WiFi password.
     - `your-email@gmail.com`: The email address sending the alert.
     - `your-email-password`: The password for the sender's email.
     - `recipient-email@gmail.com`: The email address that will receive the alerts.

### 4. **Circuit Setup**
   - Use resistors to create a voltage divider circuit for each of the three input channels (12V, 5V, 3.3V). Connect the divided outputs to the ESP32’s analog input pins.
   - Connect the OLED display to the ESP32 as per its pin configuration (SCL, SDA).

## **Code Explanation**

- **Voltage Reading**: The ESP32 reads the analog voltage values from the three input pins and converts them to actual voltage values using the voltage divider formula.
  
  ```cpp
  float readVoltage(int pin) {
    int analogValue = analogRead(pin);
    return (analogValue / 4095.0) * 3.3 * ((R1 + R2) / R2);
  }
  ```

- **OLED Display**: The OLED screen displays the voltage values in real-time.
  
  ```cpp
  display.setCursor(0, 0);
  display.print("12V: ");
  display.print(voltage12V);
  display.println(" V");
  ```

- **Email Alerts**: If any of the voltage readings fall outside the defined range, an email is triggered.
  
  ```cpp
  if (voltage12V < ATX_12V_MIN || voltage12V > ATX_12V_MAX) {
    sendEmail("12V", voltage12V);
  }
  ```

## **Usage**

1. Power on the ESP32 and ensure it is connected to your WiFi network.
2. Connect the ATX power supply to the voltage divider circuits.
3. Monitor the voltages displayed on the OLED screen.
4. If a voltage falls outside the standard ATX range, an email alert will be sent automatically.

## **Contributing**

Contributions are welcome! If you encounter any bugs or have ideas for improvement, feel free to open an issue or submit a pull request.

## **License**

This project is licensed under the MIT License.
