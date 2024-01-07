from max30102 import MAX30102
import time

# Create MAX30102 object
mx30 = MAX30102()

try:
    # Initialize the MAX30102
    mx30.begin()

    while True:
        # Read heart rate and SpO2 values
        heart_rate, spo2 = mx30.read_sensor()

        # Display the values
        print("Heart Rate: {} bpm, SpO2: {}%".format(heart_rate, spo2))

        time.sleep(1)
        break
