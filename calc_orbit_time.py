import os
import json

vehicle_data = json.load(open(
    os.path.join('config_data/vehicle_data.json')))
orbit_data = json.load(open(
    os.path.join('config_data/orbit_data.json')))


def get_orbit_time(input_data, vehicles):
    result = {
        "vehicle_name": "",
        "orbit": "",
        "time": 2147483647
    }
    traffic_speed = {
        "Orbit1": int(input_data[1]),
        "Orbit2": int(input_data[2])
    }

    for orbit, data in orbit_data.items():
        for veh in vehicles['vehicle']:
            if vehicle_data[veh]['max_speed'] < traffic_speed[orbit]:
                temp_speed = vehicle_data[veh]['max_speed']
            else:
                temp_speed = traffic_speed[orbit]

            temp = (
                (60 / temp_speed) * data['distance'] + 
                (data['craters'] * vehicles["crater_constant"]) * 
                vehicle_data[veh]["cross_crater_time"])

            if result['time'] > temp:
                result.update({
                    'vehicle_name': veh,
                    'orbit': orbit,
                    'time': temp
                })
    print(result)


