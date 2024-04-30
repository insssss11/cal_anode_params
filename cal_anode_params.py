from larmuir_function import larmuir_square
import math

print("{0:-^80}".format("Input Parameters"))
half_angle_cathode = float(input("{0:<70}{1}".format("Enter the half angle in [deg]", ": ")))
rho_cathode = float(input("{0:<70}{1}".format("Enter the cathode spherical radius in [mm]", ": ")))
current = float(input("{0:<70}{1}".format("Enter the current in [mA]", ": ")))
voltage = float(input("{0:<70}{1}".format("Enter the voltage in [kV]", ": ")))
conv_ratio = float(input("{0:<70}{1}".format("Enter the convergence ratio (r_cathode/r_anode)", ": ")))

upervence = 1e-3*current/math.pow(1e3*voltage, 1.5)

r_cathode = rho_cathode*math.sin(half_angle_cathode*math.pi/180.)

r_anode = r_cathode/conv_ratio
rho_anode = rho_cathode/conv_ratio

focal_length = -4*conv_ratio/(rho_cathode - rho_anode)

half_angle_anode = half_angle_cathode*(1 - rho_cathode/(4*(rho_cathode - rho_anode)))
position_beamwaist = rho_anode/(1 - rho_cathode/(4*(rho_cathode - rho_anode)))
r_min = math.exp(-3.3*1e-5*half_angle_anode**2/(upervence))

print_list = {"Pervence" : (1e6*upervence, "uper"),\
            "Cathode Radius" : (r_cathode, "mm"), "Cathode Spherical Radius" : (rho_cathode, "mm"),\
            "Anode Radius" : (r_anode, "mm"), "Anode Spherical Radius" : (rho_anode, "mm"),\
            "Anode Half Angle" : (half_angle_anode, "deg"), "Anode Focal Length" : (focal_length, "mm"),\
            "Beam Waist Position" : (position_beamwaist, "mm"), "Beam Waist Radius" : (r_min, "mm")}

print("{0:-^80}".format("Output Parameters"))
for key, value in print_list.items():
    print("{0:<70} : {1:3.4f} {2}".format(key, *value))