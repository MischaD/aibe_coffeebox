import time
import requests
import threading
import json
import os
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
from collections import deque

# Configuration
SHOW_PLOT = False
INTERVAL = 0.2  # Query interval in seconds
PLOT_WINDOW = 180  # Number of seconds to display in live plot
CSV_FILE = "./shelly_log/voltage_log.csv"  # File for logging data

# Ensure directory exists
os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)

# Data storage for plotting
timestamps = deque(maxlen=PLOT_WINDOW)
currents = deque(maxlen=PLOT_WINDOW)
powers = deque(maxlen=PLOT_WINDOW)

# Stop signal for the thread
stop_signal = threading.Event()

def log_voltage_main(stop_signal):
    """Function to query the voltage, update live data, and log to CSV."""
    url = "http://192.168.33.1/rpc/Shelly.GetStatus"
    payload = {
        "jsonrpc": "2.0",
        "method": "Shelly.GetStatus",
        "params": {"id": 0},
        "id": 1
    }
    headers = {"Content-Type": "application/json"}

    # Open CSV file in append mode
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if os.stat(CSV_FILE).st_size == 0:
            writer.writerow(["Timestamp", "Current (A)", "Power (W)"])  # Write header if file is empty

        while not stop_signal.is_set():
            dt = datetime.now()

            try:
                response = requests.post(url, data=json.dumps(payload), headers=headers)
                response_data = response.json()
                power = response_data["switch:0"]["apower"]
                current = response_data["switch:0"]["current"]

            except requests.exceptions.RequestException:
                power, current = -1.0, -1.0  # Indicate an error state
                print("-1 warning")

            # Update the data queues for plotting
            timestamps.append(dt)
            currents.append(current)
            powers.append(power)

            # Write data to CSV
            writer.writerow([dt.strftime("%Y-%m-%d %H:%M:%S"), current, power])
            file.flush()  # Ensure data is saved immediately

            time.sleep(INTERVAL)

def update_plot(frame):
    """Updates the plot with new data."""
    ax1.clear()
    ax2.clear()

    if timestamps:
        ax1.plot(timestamps, currents, label="Current (A)", color="blue")
        ax2.plot(timestamps, powers, label="Power (W)", color="red")

        ax1.set_ylabel("Current (A)")
        ax2.set_ylabel("Power (W)")
        ax2.set_xlabel("Time")
        ax1.legend(loc="upper left")
        ax2.legend(loc="upper right")

        plt.xticks(rotation=45)
        plt.tight_layout()

# Start the voltage logging thread
thread = threading.Thread(target=log_voltage_main, args=(stop_signal,))
thread.start()

if SHOW_PLOT:

    # Setup the matplotlib figure
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ani = animation.FuncAnimation(fig, update_plot, interval=1000)
    plt.show()
else:
    try:
        while True:
            time.sleep(1)  # Keep logging until manually stopped (Ctrl+C)
    except KeyboardInterrupt:
        print("Stopping logging...")
        stop_signal.set()


# Stop the logging when the plot is closed
stop_signal.set()
thread.join()