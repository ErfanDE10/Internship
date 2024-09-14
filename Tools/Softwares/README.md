# System Health Monitoring Service

This project is a Python-based system health monitoring tool designed to track key system performance metrics and send alerts via email and desktop notifications if any resource usage exceeds predefined thresholds. It also logs system status and can perform routine cleanup tasks like removing temporary files.

## Features

- **CPU Usage Monitoring**: Sends an alert if CPU usage exceeds 80%.
- **Memory Usage Monitoring**: Alerts when memory usage exceeds 80%.
- **Disk Usage Monitoring**: Monitors disk space and sends notifications if usage crosses 80%.
- **Heavy Processes Detection**: Identifies and reports processes using more than 50% of CPU or memory.
- **Disk I/O Monitoring**: Checks if disk read/write speeds are too slow.
- **Network Usage Monitoring**: Monitors the network's sending/receiving speed.
- **Zombie Processes Detection**: Detects zombie processes running in the system.
- **Swap Memory Usage**: Alerts if swap memory usage exceeds 50%.
- **Temporary File Cleanup**: Automatically cleans up temporary files.

## Setup

### Prerequisites

- **Python 3.6 or higher**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Steps to Run

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/system-health-monitor.git
   cd system-health-monitor
   ```

2. **Install Required Dependencies**:
   This project comes with a `runner.py` script that automatically installs the required dependencies and runs the health monitoring script. You don't need to worry about manually installing packages.
   
   Run the following command to start the setup:
   ```bash
   python runner.py
   ```

   The `runner.py` script will:
   - Check if Python is installed.
   - Check if `pip` is installed (and install it if necessary).
   - Install all required libraries listed in `requirements.txt`.
   - Run the system health monitor automatically.

3. **Run the System Health Monitoring Script**:
   Once everything is set up, the script will automatically start monitoring your system resources and send alerts when necessary.

### Email Configuration

For email alerts to work, you need to configure the email settings in the `system_health_monitor.py` file:
- Replace the placeholder `your_email@gmail.com` and `your_password` with your own email credentials in the following section:
  ```python
  EMAIL_ADDRESS = 'your_email@gmail.com'
  EMAIL_PASSWORD = 'your_password'
  RECIPIENT_EMAIL = 'recipient@example.com'
  ```

**Note**: If you're using Gmail, you might need to allow "Less secure apps" from your Google account settings for SMTP to work.

## Project Structure

```
system-health-monitor/
│
├── runner.py                # Script to install dependencies and run the monitor
├── system_health_monitor.py  # Main system monitoring script
├── requirements.txt          # Lists required Python libraries
├── system_health.log         # Log file (generated after running)
└── README.md                 # This documentation
```

## How It Works

- **Monitoring**: The system runs every hour by default, checking CPU, memory, disk, network, and more.
- **Notifications**: If any threshold is crossed, the system will send an email and show a desktop notification to alert the user.
- **Logging**: All system checks are logged in `system_health.log` for review.
- **Automatic Cleanup**: Temporary files are automatically cleaned up at regular intervals.

## Customization

You can modify the alert thresholds or add additional system checks by editing the functions in `system_health_monitor.py`.

## License

This project is licensed under the MIT License.
