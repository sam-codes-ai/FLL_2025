from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
motor_aurafarmer = Motor(Port.A)
motor_sigma = Motor(Port.E)

#The allignment: 2nd bolded spot, left side. Mission 1-2
# Initialize the drive base. In this example, the wheel diameter is 64mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=64, axle_track=112)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
# hub.display.text("AURA")

drive_base.straight(664.67)

drive_base.turn(-44.5)

drive_base.straight(300)

motor_aurafarmer.run_angle(1000,240, then=Stop.HOLD, wait=True)

drive_base.straight(-257.5)

drive_base.turn(-46)

drive_base.straight(10)

drive_base.turn(170)

drive_base.straight(100)

motor_sigma.run_angle(360, 35, then=Stop.HOLD, wait=True)

drive_base.straight(200)

motor_sigma.run_angle(360, -75, then=Stop.HOLD, wait=True)
