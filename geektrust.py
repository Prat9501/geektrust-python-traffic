import os
import json
from get_vehicles import get_vehicle
from get_orbit_time import get_orbit_time


orbit_data = json.load(open(
    os.path.join('config_data/orbit_data.json')))
vehicle_data = json.load(open(
    os.path.join('config_data/vehicle_data.json')))

with open("sample_input/input2.txt", 'r') as f:
    input_data = (f.read()).split(' ')
data = get_vehicle(input_data[0])

get_orbit_time(input_data, data)