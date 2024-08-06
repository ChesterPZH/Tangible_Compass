Tangible Compass is a wearable device that employs real-time haptic feedback with directional guidance, which enhances the navigation capabilities of the Blind and Low Vision community or for screenless applications.

Tangible Compass is based on an open loop data transformation / control system and a one DOF kinesthetic haptic device.



Open loop control system: Smartphone app sensory data -> LAN remote data streaming -> python server API acquisition -> python to Arduino serial communication -> Hapkit board local setup.

Smartphone app sensory data: Phyphox app is used to capture smartphone sensory data, as the indication of current user status. Theoretically, the GPS data should be used; however, it does not provide effective update as commercial GPS applications. The magnetic field data was used to simulate the compass data. It is also mostly linear as the phone pointing in a half circle compass and has a quick update rate, which is great for no-moving hands on demo.

LAN remote data streaming: Simply turning on the remote data streaming function in Phyphox. Any APP has similar function would be a possible replacement of Phyphox.

python server API acquisition + Arduino serial communication: Change the url to the IP address showing on Phyphox. The example uses magnetic filed X axis data. You can post process the data (e.g., offset, amplify) before write to serial, and it is recommended to do in Python. Change the serial_port and baud_rate to match your Arduino board.





One DOF kinesthetic device: The design is based on Stanford University Hapkit. 
The basics of the system structure / mathematical model / control loop can be found on Wiki. Below is the logistic that linearly maps the serial data to the force. Users can change the values accordingly to modify the haptic environment.
