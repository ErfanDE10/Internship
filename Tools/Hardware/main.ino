#include <WiFi.h>
#include <ESP32_MailClient.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// WiFi settings
const char* ssid = "your-SSID";
const char* password = "your-PASSWORD";

// Email settings
#define SMTP_HOST "smtp.gmail.com"
#define SMTP_PORT 465
#define EMAIL_SENDER "your-email@gmail.com"
#define EMAIL_PASSWORD "your-email-password"
#define EMAIL_RECIPIENT "recipient-email@gmail.com"

// OLED display settings
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// ESP32 pins for voltage input
const int analogPin12V = 34; // Analog pin for 12V channel
const int analogPin5V = 35;  // Analog pin for 5V channel
const int analogPin3V = 32;  // Analog pin for 3.3V channel

// Voltage divider parameters
const float R1 = 30000; // Resistor R1 (ohms)
const float R2 = 7500;  // Resistor R2 (ohms)

// Standard ATX voltage ranges
const float ATX_12V_MIN = 11.4;
const float ATX_12V_MAX = 12.6;
const float ATX_5V_MIN = 4.75;
const float ATX_5V_MAX = 5.25;
const float ATX_3V_MIN = 3.14;
const float ATX_3V_MAX = 3.47;

SMTPData smtpData;

void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("OLED allocation failed"));
    for (;;);
  }
  display.display();
  delay(2000);
  display.clearDisplay();
}

void loop() {
  // Read voltages from the three channels
  float voltage12V = readVoltage(analogPin12V);
  float voltage5V = readVoltage(analogPin5V);
  float voltage3V = readVoltage(analogPin3V);

  // Display voltages on OLED
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  
  display.setCursor(0, 0);
  display.print("12V: ");
  display.print(voltage12V);
  display.println(" V");

  display.setCursor(0, 20);
  display.print("5V: ");
  display.print(voltage5V);
  display.println(" V");

  display.setCursor(0, 40);
  display.print("3.3V: ");
  display.print(voltage3V);
  display.println(" V");
  
  display.display();

  // Check voltage ranges and send email if necessary
  if (voltage12V < ATX_12V_MIN || voltage12V > ATX_12V_MAX) {
    sendEmail("12V", voltage12V);
  }
  
  if (voltage5V < ATX_5V_MIN || voltage5V > ATX_5V_MAX) {
    sendEmail("5V", voltage5V);
  }
  
  if (voltage3V < ATX_3V_MIN || voltage3V > ATX_3V_MAX) {
    sendEmail("3.3V", voltage3V);
  }

  delay(5000); // Check voltage every 5 seconds
}

float readVoltage(int pin) {
  int analogValue = analogRead(pin);
  return (analogValue / 4095.0) * 3.3 * ((R1 + R2) / R2); // Calculate voltage using voltage divider
}

void sendEmail(String channel, float voltage) {
  smtpData.setLogin(SMTP_HOST, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD);
  smtpData.setSender("ESP32 Voltage Monitor", EMAIL_SENDER);
  smtpData.setPriority("High");
  smtpData.setSubject("Voltage Alert - " + channel);
  smtpData.setMessage("Warning! " + channel + " Voltage out of range: " + String(voltage) + " V", false);
  smtpData.addRecipient(EMAIL_RECIPIENT);

  if (!MailClient.sendMail(smtpData)) {
    Serial.println("Error sending Email, " + MailClient.smtpErrorReason());
  } else {
    Serial.println("Email sent successfully for " + channel + "!");
  }

  smtpData.empty(); // Clear data after sending
}
