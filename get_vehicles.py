def get_vehicle(climate):
    if climate == "SUNNY":
        data = {
            "vehicle": ["CAR", "BIKE", "TUKTUK"],
            "crater_constant": 0.8
        }
    elif climate == "RAINY":
        data = {
            "vehicle": ["CAR", "TUKTUK"],
            "crater_constant": 1.2
        }
    else:
        data = {
            "vehicle": ["CAR", "BIKE"],
            "crater_constant": 1
        }
    
    return data