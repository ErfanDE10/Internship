# System Health Monitoring Script

This Python-based system health monitoring script continuously tracks the performance of your system and sends alerts when critical resource usage or issues are detected. It provides real-time notifications and email alerts to keep you informed of potential bottlenecks or system slowdowns. The script is designed for automated and periodic health checks, enabling you to maintain an optimized and stable environment.

## Features

- **CPU Monitoring**: Checks the CPU usage and raises an alert if it exceeds the defined threshold (80% by default).
- **Memory Monitoring**: Monitors RAM usage, alerting when more than 80% of memory is being utilized.
- **Disk Usage Monitoring**: Tracks the usage of disk space and alerts when usage exceeds 80%.
- **Heavy Process Detection**: Identifies processes that consume more than 50% of CPU or memory, notifying the user.
- **Disk I/O Monitoring**: Ensures sufficient read and write speeds of the disk to prevent bottlenecks in I/O operations.
- **Network Monitoring**: Checks network performance to detect any slowdowns in sending or receiving data.
- **Zombie Process Detection**: Scans for zombie processes that could affect system stability.
- **Swap Memory Monitoring**: Alerts if swap memory usage exceeds 50%, preventing system slowdowns.
- **Automatic Cleanup**: Cleans up temporary files to free up system resources.
- **Logging**: All alerts and system statuses are logged to a file for later review.

## Installation

To install and run this system health monitoring script, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/system-health-monitor.git
cd system-health-monitor
```

### 2. Install Dependencies
The script requires Python and a few external libraries to function. Install the dependencies with the following command:
```bash
pip install psutil smtplib plyer
```

### 3. Configure Email Settings
Edit the script to add your email credentials. These will be used to send alert notifications.

```python
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'
```

### 4. Run the Script
Once configured, run the script using Python:
```bash
python system_health_monitor.py
```

The script will automatically check your system health every hour and send alerts when necessary.

## Usage

This script is designed to run periodically in the background, checking system resources every hour and alerting you via email and desktop notifications if any resource exceeds its threshold.

- **CPU Threshold**: Default is set to 80%.
- **Memory Threshold**: Default is 80%.
- **Disk Usage Threshold**: Default is 80%.
- **Heavy Processes**: Alerts for processes using more than 50% CPU or memory.
- **Disk I/O Speeds**: Checks if read/write speed is below 50MB/s.
- **Network**: Notifies if the sending/receiving rate is below 1MB/s.
- **Zombie Processes**: Scans for any zombie processes affecting system stability.
- **Swap Memory**: Sends an alert if swap usage exceeds 50%.

### Logging

All system health checks are logged into `system_health.log`. This file contains timestamps of each health check, allowing you to review system health history.

### Notifications

- **Email Alerts**: Sent when any critical issue is detected.
- **Desktop Notifications**: Appear on your screen when thresholds are breached.

## Customization

You can modify the script to adjust the thresholds or the frequency of checks as needed:

- **Change Check Frequency**: The script runs every hour by default. You can modify the `time.sleep(3600)` statement to change this interval.
- **Thresholds**: Modify the threshold values (e.g., CPU, memory, disk) directly in the script to match your system’s needs.

## Future Improvements

Some potential features to add in the future:
- Integration with a cloud service for remote monitoring.
- Detailed reporting (monthly or weekly) sent via email.
- Web interface for real-time monitoring.
- Auto-resolve certain issues like restarting heavy processes or clearing cache.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project by submitting pull requests. You can also report any issues or suggest new features through GitHub Issues.
