import os
import sys
import platform

def get_uptime():
    if platform.system() == "Windows":
        # Windows: use 'net stats srv' command and parse output
        try:
            output = os.popen('net stats srv').read()
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System uptime (since):", line.split("Statistics since")[1].strip())
                    return
            print("Unable to determine uptime on Windows.")
        except Exception as e:
            print("Error fetching uptime:", e)
    else:
        # Unix/Linux/Mac: use 'uptime -p' or read /proc/uptime
        try:
            if os.path.exists('/proc/uptime'):
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    hours, remainder = divmod(uptime_seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    print(f"System uptime: {int(hours)} hours, {int(minutes)} minutes")
            else:
                output = os.popen('uptime -p').read().strip()
                print("System uptime:", output)
        except Exception as e:
            print("Error fetching uptime:", e)

if __name__ == "__main__":
    get_uptime()
