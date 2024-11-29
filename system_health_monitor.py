import psutil
import logging
import time
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Set up logging
logging.basicConfig(
    filename="logs/system_health.log",  # Use the logs folder
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Threshold values
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 90  # in percentage
MAX_PROCESSES = 500  # Maximum number of processes

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")

    # Check memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High memory usage detected: {memory_usage}%")

    # Check disk space
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert(f"Low disk space detected: {disk_usage}% used")

    # Check number of running processes
    processes = len(psutil.pids())
    if processes > MAX_PROCESSES:
        alert(f"High number of processes running: {processes}")

def alert(message):
    """Log and print an alert message."""
    print(f"ALERT: {message}")
    logging.warning(message)

if __name__ == "__main__":
    print("Starting System Health Monitoring Script...")
    while True:
        check_system_health()
        time.sleep(10)  # Monitor every 10 seconds
