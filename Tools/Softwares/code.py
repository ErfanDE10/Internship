import psutil
import smtplib
import time
import os
import logging
from plyer import notification

# Email configuration
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_EMAIL = 'recipient@example.com'

# Logging configuration
logging.basicConfig(filename='system_health.log', level=logging.INFO)

class SystemMonitor:
    def __init__(self):
        # Initialize any required attributes
        pass

    # Send email alerts
    def send_email(self, subject, body):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg)
        except Exception as e:
            print(f"Error sending email: {e}")

    # Send desktop notifications
    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

    # Log system alerts
    def log_health(self, message):
        logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

    # Clean temporary files
    def clean_temp_files(self):
        temp_dir = "/path/to/temp"
        try:
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            return "Temporary files cleaned."
        except Exception as e:
            return f"Error cleaning temporary files: {e}"

class ResourceCheck(SystemMonitor):
    # Check CPU usage
    def check_cpu(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > 80:
            return f"High CPU usage: {cpu_usage}%"
        return None

    # Check Memory usage
    def check_memory(self):
        memory = psutil.virtual_memory()
        if memory.percent > 80:
            return f"High memory usage: {memory.percent}%"
        return None

    # Check Disk usage
    def check_disk(self):
        disk = psutil.disk_usage('/')
        if disk.percent > 80:
            return f"High disk usage: {disk.percent}%"
        return None

    # Check for heavy processes
    def check_heavy_processes(self):
        heavy_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            if proc.info['cpu_percent'] > 50 or proc.info['memory_percent'] > 50:
                heavy_processes.append(
                    f"Process {proc.info['name']} (PID: {proc.info['pid']}) using CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%")
        if heavy_processes:
            return "\n".join(heavy_processes)
        return None

    # Check Disk I/O
    def check_disk_io(self):
        io_counters = psutil.disk_io_counters()
        if io_counters.read_bytes < 50000000:
            return "Disk read speed is too slow"
        if io_counters.write_bytes < 50000000:
            return "Disk write speed is too slow"
        return None

    # Check Network usage
    def check_network(self):
        net_io = psutil.net_io_counters()
        if net_io.bytes_sent < 1000000:
            return "Network sending is too slow"
        if net_io.bytes_recv < 1000000:
            return "Network receiving is too slow"
        return None

    # Check for zombie processes
    def check_zombie_processes(self):
        zombie_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            if proc.info['status'] == psutil.STATUS_ZOMBIE:
                zombie_processes.append(f"Zombie process: {proc.info['name']} (PID: {proc.info['pid']})")
        if zombie_processes:
            return "\n".join(zombie_processes)
        return None

    # Check Swap memory usage
    def check_swap_memory(self):
        swap = psutil.swap_memory()
        if swap.percent > 50:
            return f"Swap memory usage is high: {swap.percent}%"
        return None

# Main Monitoring Class
class SystemHealthMonitor(ResourceCheck):
    def __init__(self):
        super().__init__()

    # Check all system resources and alert if needed
    def check_system_health(self):
        alerts = []
        checks = [
            self.check_cpu, self.check_memory, self.check_disk, 
            self.check_heavy_processes, self.check_disk_io,
            self.check_network, self.check_zombie_processes,
            self.check_swap_memory
        ]
        
        for check in checks:
            alert = check()
            if alert:
                alerts.append(alert)

        if alerts:
            message = "\n".join(alerts)
            self.send_email("System Health Alert", message)
            self.send_notification("System Health Alert", message)
            self.log_health(message)

        clean_message = self.clean_temp_files()
        self.log_health(clean_message)

# Run the monitoring system
if __name__ == "__main__":
    monitor = SystemHealthMonitor()
    while True:
        monitor.check_system_health()
        time.sleep(3600)  # Run the checks every 1 hour
