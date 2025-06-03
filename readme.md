copilot_test.py
Description
copilot_test.py is a simple Python script that displays the system uptime (how long the system has been running).

On Windows, it uses the net stats srv command to determine when the system started.
On Unix/Linux/Mac, it tries to read from /proc/uptime for detailed uptime, or falls back to using the uptime -p command.
The script prints the system uptime in a human-readable format.

How to Run
Clone or download this repository.
Ensure you have Python 3 installed on your system.
Open a terminal (Command Prompt on Windows, Terminal on Unix/Linux/Mac).
Navigate to the directory containing copilot_test.py.
Run the script:
bash
python copilot_test.py
You will see the system uptime printed in the terminal.
