import os
import json


def get_vehicle(climate):
    if climate == "SUNNY":
        data = {
            "vehicle": ["car", "bike", "tuktuk"],
            "crater_constant": 0.8
        }
    elif climate == "RAINY":
        data = {
            "vehicle": ["car", "tuktuk"],
            "crater_constant": 1.2
        }
    else:
        data = {
            "vehicle": ["car", "bike"],
            "crater_constant": 1
        }
    
    return data