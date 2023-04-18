import math

# Motor Parameters

Continious_Motor_Torque = 0.0183 #Nm
Stall_Motor_Torque = 0.0679 #Nm


# Vehicle parameters
Vehicle_Mass = 3.5  # kg #m1
Wheel_Outer_Diameter = 64  # mm    #D1
Wheel_Mass = 0.031  # kg/pc #mD1
Number_of_Wheels = 4  #n1
Number_of_Motors = 4 
Rolling_Friction_Coefficient_Between_Wheel_and_Floor = 0.030 #mu1


# System efficiency
System_Efficiency = 75

# Floor slope
alpha = 0  # degrees

# Operating conditions
Operating_Speed_V1 = 1  # m/min
Operating_Speed_V2 = 10  # m/min
t1 = 10  # s

# Stopping accuracy
delta_l = 10  # mm

# Safety factor
SF = 1.5

# Load inertia calculations
Vehicle_Inertia = (Vehicle_Mass + 0.5 * Wheel_Mass * Number_of_Wheels) * ((Wheel_Outer_Diameter * 0.001)/ 2) ** 2
Total_Load_Inertia = Vehicle_Inertia + 0 #IF MULTIPLE VEHICLES, SHOULD BE ADDED

# Required speed calculations
Operating_Speed_V1_RPM = Operating_Speed_V1 / (3.14 * Wheel_Outer_Diameter * 0.001)  #RPM
Operating_Speed_V2_RPM = Operating_Speed_V2 / (3.14 * Wheel_Outer_Diameter * 0.001)  #RPM

# Required torque calculations
## Acceleration Torque
Acceleration_Torque = Total_Load_Inertia * Operating_Speed_V2_RPM / (9.55 * t1)   #V2_RPM is selected, beccause it's the highest

## Load Torque
Load_Force = 9.8 * ((Vehicle_Mass + Number_of_Wheels * Wheel_Mass) * (math.sin(math.radians(alpha)) + Rolling_Friction_Coefficient_Between_Wheel_and_Floor * math.cos(math.radians(alpha))))

Load_Torque = (Load_Force * Wheel_Outer_Diameter * 0.001)/ (2 * System_Efficiency * 0.01) 

#Total Required Torque
Total_Required_Torque = ((Acceleration_Torque + Load_Torque) * SF)/4 

# Required stopping accuracy calculations
delta_theta = delta_l * 360 / (3.14 * Wheel_Outer_Diameter)

##REQUIRED SYSTEM STUFF##
print(f"Load inertia: {Total_Load_Inertia:.6f} kg*m^2")
print(f"Load force: {Load_Force:.6f} kg*m^2")

print(f"Required RPM_V1: {Operating_Speed_V1_RPM:.3f} r/min")
print(f"Required RPM_V2: {Operating_Speed_V2_RPM:.3f} r/min")

print(f"Required acceleration torque: {Acceleration_Torque:.6f} N*m")
print(f"Required load torque: {Load_Torque:.6f} N*m")

print(f"Required torque: {Total_Required_Torque:.6f} N*m")
print(f"Required stopping accuracy: {delta_theta:.2f} degrees")

if(Total_Required_Torque < Continious_Motor_Torque):
    print(f"Motors can drive the vehicle safely with: {Continious_Motor_Torque/Total_Required_Torque} ratio")


