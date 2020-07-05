# Geektrust Traffic Problem

[![language](https://img.shields.io/badge/language-python-yellowgreen)]()

## Lengaburu's Traffic
![](traffic.png)

## Steps
This project is solved using Python 3.7.

Project Directory

```
├── src 
│   ├── config_data         # Data about the vehicles & orbit.
│   ├── sample_input        # Sample input file params.       
│   └── geektrust.py        # `Main method file.`
│   ├── get_orbit_data.py   # function to calculate minimum time.
│   ├── get_vehicles.py     # Returns dict object of vehicles. 
├── tests 
│   ├── test_data           # Sample input & output data for test.         
│   ├── geektrust_test.py   # `Main test file`              
└── requirements.txt
```

- Setup the virtualenv for project. `virtualenv -p python3 venv`
- `cd` to project directory
- Install requirements `pip install -r requirements.txt`
- Run tests
    - `pytest tests/geektrust_test.py`
- Run solution file
    - `python -m src.geektrust src/sample_input/input1.txt`

- To see the code coverage, run
    - `coverage run -m pytest tests/geektrust_test.py`
    - `coverage report -m`