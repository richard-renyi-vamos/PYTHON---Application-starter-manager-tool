import os
import psutil
import subprocess
import time

class AppManager:
    def __init__(self):
        self.running_apps = {}

    def start_application(self, script_name):
        """Starts a Python application script."""
        if script_name in self.running_apps:
            print(f"{script_name} is already running!")
            return

        try:
            process = subprocess.Popen(['python', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.running_apps[script_name] = process
            print(f"Started {script_name} with PID {process.pid}")
        except Exception as e:
            print(f"Error starting {script_name}: {e}")

    def stop_application(self, script_name):
        """Stops a running Python application script."""
        if script_name not in self.running_apps:
            print(f"{script_name} is not running!")
            return

        process = self.running_apps[script_name]
        process.terminate()
        del self.running_apps[script_name]
        print(f"Stopped {script_name} with PID {process.pid}")

    def list_running_apps(self):
        """Lists all running Python application scripts."""
        if not self.running_apps:
            print("No applications are currently running.")
        else:
            for app, process in self.running_apps.items():
                print(f"{app} (PID: {process.pid})")

    def monitor_apps(self):
        """Monitors the status of running applications."""
        while True:
            for app, process in list(self.running_apps.items()):
                if process.poll() is not None:  # Process has finished
                    print(f"{app} has stopped.")
                    del self.running_apps[app]
            time.sleep(5)

def main():
    manager = AppManager()

    while True:
        print("\nApplication Manager")
        print("1. Start an application")
        print("2. Stop an application")
        print("3. List running applications")
        print("4. Monitor applications")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            script_name = input("Enter the script name to start: ")
            manager.start_application(script_name)

        elif choice == "2":
            script_name = input("Enter the script name to stop: ")
            manager.stop_application(script_name)

        elif choice == "3":
            manager.list_running_apps()

        elif choice == "4":
            manager.monitor_apps()

        elif choice == "5":
            print("Exiting Application Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
