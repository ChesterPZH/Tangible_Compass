# import requests
# import json
# import time

# url = 'http://172.168.91.121/get?'

# what_to_get = ['magX', 'magY', 'magZ', 'mag']
# get_gyro_info = ['gyrX', 'gyrY', 'gyrZ']
# angle_info = ['anglePlane']

# def print_data():
#     response = requests.get(url + '&'.join(angle_info)).text
#     data = json.loads(response)
#     # for item in get_gyro_info :
#     #     mag_data = data['buffer'][item]['buffer'][0]
#     #     print(f'{mag_data:10.7}', end='\t')
#     live_data = data['buffer']['anglePlane']['buffer'][0]
#     print(f'{live_data}', end='\t')
#     print()

# while True:
#     print_data()
#     time.sleep(0.1)

import requests
import json
import time
import serial  # Import the serial library

url = 'http://172.20.10.14/get?'
mag_info = ['magX']
serial_port = '/dev/cu.usbserial-AQ02O6OD'  # Change this to the correct port
baud_rate = 115200

# Set up the serial connection
ser = serial.Serial(serial_port, baud_rate)

def print_data():
    response = requests.get(url + '&'.join(mag_info)).text
    data = json.loads(response)
    live_data = data['buffer']['magX']['buffer'][0]
    print(f'{live_data}', end='\t')


    #=====================================
    # cycle_time = 8  # total cycle time in seconds (0 to 10 to 0 to -10 to 0)
    # elapsed_time = time.time() % cycle_time  # get the elapsed time in the current cycle
    
    # if elapsed_time >= 0 and elapsed_time < 5:
    #     offset = 0
    # elif elapsed_time >= 5 and elapsed_time < 10:
    #     offset = 10
    # elif elapsed_time >= 10 and elapsed_time < 15:
    #     offset = 0
    # else:
    #     offset = -10

    # # Apply the offset to the live_data
    # live_data += offset
    #=====================================

    # Send data to Arduino
    ser.write(f"{live_data}\n".encode())

while True:
    print_data()
    time.sleep(0.001)

# serial_port = '/dev/cu.usbserial-AQ02O6OD'  # Change this to the correct port on your system
# baud_rate = 115200  # Set your baud rate
# dummy_data = ["123.45", "234.56", "345.67", "456.78", "567.89"]  # Example dummy data

# # Set up the serial connection
# ser = serial.Serial(serial_port, baud_rate)

# def print_data():
#     for data in dummy_data:
#         print(f'{data}', end='\t')  # Print dummy data to console for verification
#         ser.write(f"{data}\n".encode())  # Send dummy data to Arduino
#         time.sleep(0.1)  # Adjust time.sleep as needed for your testing

# while True:
#     print_data()