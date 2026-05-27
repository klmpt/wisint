import os
import datetime

def log_action(message):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    filename = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    filepath = os.path.join('logs', filename)
    
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {message}\n")