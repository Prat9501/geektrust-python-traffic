import os
import sys
import re
import pytest
from src.get_vehicles import get_vehicle
from src.get_orbit_time import get_orbit_time


n_files = len(os.listdir('tests/test_data/input_data'))

def open_input_file(path):
    with open(path, 'r') as f:
        input_data = (f.read()).split(' ')
    return input_data

def write_output_data(path, vehicle, orbit):
    with open(path, 'w') as f:
        f.write(f"{vehicle} {orbit}") 


def test_to_check_the_input_pattern():
    for i in range(1, n_files+1):
        with open(f"tests/test_data/input_data/input{i}.txt", 'r') as f:
            input_data = f.read()
            assert re.match(r'(RAINY|SUNNY|WINDY) \d+ \d+', input_data)


def test_to_check_output_files():
    for i in range(1, n_files+1):
        input_data = open_input_file(f"tests/test_data/input_data/input{i}.txt")

        vehicle_data = get_vehicle(input_data[0])
        res = get_orbit_time(input_data, vehicle_data)

        write_output_data(
            f'tests/test_data/output_data/output{i}.txt',
            res['vehicle_name'],
            res['orbit']
        )
    output_files = len(os.listdir('tests/test_data/input_data'))
    assert n_files == output_files


def test_to_check_climate():
    for i in range(1, n_files+1):
        input_data = open_input_file(f"tests/test_data/input_data/input{i}.txt")
        assert input_data[0] in ["SUNNY", "RAINY", "WINDY"]


def test_to_check_vehicle():
    for i in range(1, n_files+1):
        input_data = open_input_file(f"tests/test_data/input_data/input{i}.txt")
        vehicle_data = get_vehicle(input_data[0])
        if input_data[0] == 'SUNNY':
            assert vehicle_data['vehicle'] == ["CAR", "BIKE", "TUKTUK"]
        elif input_data[0] == 'RAINY':
            assert vehicle_data['vehicle'] == ["CAR", "TUKTUK"]
        else:
            assert vehicle_data['vehicle'] == ["CAR", "BIKE"]


def test_to_check_the_output_pattern():
    for i in range(1, n_files+1):
        with open(f"tests/test_data/output_data/output{i}.txt", 'r') as f:
            input_data = f.read()
            assert re.match(r'(CAR|TUKTUK|BIKE) (ORBIT1|ORBIT2)', input_data)