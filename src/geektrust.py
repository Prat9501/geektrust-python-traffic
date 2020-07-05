import os
import sys
from get_vehicles import get_vehicle
from get_orbit_time import get_orbit_time


def main():
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        input_data = (f.read()).split(' ')

    vehicle_data = get_vehicle(input_data[0])
    res = get_orbit_time(input_data, vehicle_data)

    with open('sample_input/output1.txt', 'w') as f:
        f.write(f"{res['vehicle_name']} {res['orbit']}") 

    # n_files = len(os.listdir('sample_input/input'))

    # for i in range(1, n_files+1):
        # with open(f"sample_input/input/input{i}.txt", 'r') as f:
        #     input_data = (f.read()).split(' ')

        # vehicle_data = get_vehicle(input_data[0])
        # res = get_orbit_time(input_data, vehicle_data)

        # with open(f'sample_input/output/output{i}.txt', 'w') as f:
        #     f.write(f"{res['vehicle_name']} {res['orbit']}") 

if __name__ == '__main__':
    main()