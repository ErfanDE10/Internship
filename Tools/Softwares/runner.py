import os
import subprocess
import sys

# Function to check if Python is installed
def check_python_installed():
    try:
        subprocess.check_call([sys.executable, '--version'])
        return True
    except Exception as e:
        print(f"Python is not installed. Error: {e}")
        return False

# Function to check if pip is installed
def check_pip_installed():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
        return True
    except Exception:
        print("pip not found. Installing pip...")
        try:
            subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])
            return True
        except Exception as e:
            print(f"Failed to install pip. Error: {e}")
            return False

# Function to install required packages from requirements.txt
def install_requirements():
    try:
        print("Installing required libraries...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("All dependencies installed successfully.")
    except Exception as e:
        print(f"Failed to install dependencies. Error: {e}")

# Function to run the main system health monitor script
def run_monitor_script():
    try:
        print("Running system health monitoring script...")
        subprocess.check_call([sys.executable, 'system_health_monitor.py'])
    except Exception as e:
        print(f"Failed to run the system health monitor script. Error: {e}")

# Main function to orchestrate the setup and execution
def main():
    # Step 1: Check if Python is installed
    if not check_python_installed():
        print("Please install Python 3.6 or higher and rerun this script.")
        return
    
    # Step 2: Check if pip is installed
    if not check_pip_installed():
        print("Please install pip manually and rerun this script.")
        return
    
    # Step 3: Install required libraries
    install_requirements()

    # Step 4: Run the system health monitoring script
    run_monitor_script()

if __name__ == "__main__":
    main()
