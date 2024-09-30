import threading
import tkinter as tk
from data_processing import process_heart_rate, detect_anomaly
from database import init_db, insert_heart_rate
from visualization import Visualizer
from gui import GUI
from sensor import Sensor
import time

sensor = Sensor()

def fetch_data():
    while True:
        heart_rate = sensor.get_heart_rate()
        spo2 = sensor.get_spo2()[1]  # We only care about SpO2 here
        if heart_rate is not None:
            heart_rate = process_heart_rate(heart_rate)
            insert_heart_rate(heart_rate)
            if detect_anomaly(heart_rate):
                print(f"Anomaly detected: {heart_rate}")
        time.sleep(1)
        return heart_rate, spo2

def heart_rate_callback():
    heart_rate, spo2 = fetch_data()
    return heart_rate

def main():
    # Initialize database
    init_db()

    # Setup the real-time visualizer
    visualizer = Visualizer()

    # Run the tkinter GUI in the main thread
    root = tk.Tk()
    gui = GUI(root, heart_rate_callback)
    root.title("Patient Monitoring App")
    
    # Create a separate thread for fetching data and updating graphs
    data_thread = threading.Thread(target=fetch_data, daemon=True)
    data_thread.start()

    root.mainloop()

    # Start real-time visualization
    visualizer.start_visualization()

if __name__ == "__main__":
    main()
