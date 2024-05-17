from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import keyboard
from time import sleep as delay

print('Program started')

# Initialize the client
client = RemoteAPIClient()

# Connect to CoppeliaSim server
sim = client.require('sim')

# Start simulation
sim.startSimulation()

print('Connected to remote API server')

# Get object handles
left_motor_handle = sim.getObject('/left_motor')
right_motor_handle = sim.getObject('/right_motor')

delay(1)

lSpeed = 0
rSpeed = 0

try:
    while True:
        # Set motor velocities
        sim.setJointTargetVelocity(left_motor_handle, lSpeed)
        sim.setJointTargetVelocity(right_motor_handle, rSpeed)

        # Handle key press events
        if keyboard.is_pressed('q'):
            break
        elif keyboard.is_pressed('w'):
            lSpeed = 4
            rSpeed = 4
        elif keyboard.is_pressed('a'):
            lSpeed = -0.4
            rSpeed = 1
        elif keyboard.is_pressed('d'):
            lSpeed = 1
            rSpeed = -0.4
        elif keyboard.is_pressed('s'):
            lSpeed = -1
            rSpeed = -1
        else:
            lSpeed = 0
            rSpeed = 0

        # Small delay to prevent excessive CPU usage
        delay(0.1)

except Exception as e:
    print(f"An error occurred: {e}")

# Stop the simulation
sim.stopSimulation()

print('Program ended')
