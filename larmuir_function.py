import numpy as np
from scipy.interpolate import CubicSpline

def larmuir_square(x):
    xpoints = [0.002, 0.0025, 0.0029, 0.0033, 0.004, 0.005, 0.0056, 0.0063, 0.0071, 0.0083, 0.01, 0.0111, 0.0125, 0.0143, 0.0167, 0.02, 0.025, 0.0333, 0.05, 0.0556, 0.0625, 0.0714, 0.0833, 0.1, 0.1053, 0.1111, 0.1176, 0.125, 0.1333, 0.1429, 0.1538, 0.1667, 0.1724, 0.1786, 0.1852, 0.1923, 0.2, 0.2083, 0.2174, 0.2273, 0.2381, 0.25, 0.2632, 0.2778, 0.2941, 0.3125, 0.3333, 0.3448, 0.3571, 0.3704, 0.3846, 0.4, 0.4167, 0.4348, 0.4545, 0.4762, 0.5, 0.5556, 0.5623, 0.5882, 0.625, 0.6667, 0.6897, 0.7143, 0.7407, 0.7692, 0.8, 0.8333, 0.8696, 0.9091, 0.9524, 1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 800.0, 1000.0, 1500.0, 2000.0, 5000.0, 10000.0, 30000.0, 100000.0]
    ypoints = [13015.0, 9303.0, 7610.0, 6031.0, 4582.0, 3270.0, 2790.0, 2333.0, 1907.0, 1509.0, 1144.0, 974.1, 813.7, 663.3, 523.6, 395.3, 279.6, 178.2, 93.24, 78.56, 64.74, 51.86, 39.98, 29.19, 26.68, 24.25, 21.89, 19.62, 17.44, 15.35, 13.35, 11.46, 10.73, 10.01, 9.135, 8.636, 7.976, 7.334, 6.712, 6.109, 5.528, 4.968, 4.429, 3.913, 3.421, 2.954, 2.512, 2.302, 2.098, 1.901, 1.712, 1.531, 1.358, 1.193, 1.036, 0.888, 0.75, 0.502, 0.621, 0.394, 0.2968, 0.2118, 0.174, 0.1396, 0.1084, 0.0809, 0.0571, 0.0372, 0.0213, 0.0096, 0.0024, 0.0, 0.0023, 0.0086, 0.018, 0.0299, 0.0437, 0.0591, 0.0756, 0.0931, 0.1114, 0.1302, 0.1688, 0.208, 0.248, 0.287, 0.326, 0.364, 0.402, 0.438, 0.474, 0.509, 0.543, 0.576, 0.608, 0.639, 0.669, 0.727, 0.783, 0.836, 0.886, 0.934, 0.979, 1.022, 1.063, 1.103, 1.141, 1.178, 1.213, 1.247, 1.28, 1.453, 1.516, 1.575, 1.63, 1.682, 1.731, 1.777, 1.938, 2.073, 2.189, 2.289, 2.378, 2.713, 2.944, 3.12, 3.261, 3.38, 3.482, 3.572, 3.652, 3.788, 3.903, 4.002, 4.089, 4.166, 4.329, 4.462, 4.573, 4.669, 4.829, 4.96, 5.165, 5.324, 5.61, 5.812, 6.453, 6.933, 7.693, 8.523]
    interpolator = CubicSpline(xpoints, ypoints)
    return interpolator(x)