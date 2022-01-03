#!/usr/bin/env python3

from solarsystem import *

import json


solar_system = SolarSystem(1920, 1080)

with open("solar_system.json", "r", encoding="utf8") as f:
    data = json.loads(f.read())
    solar_system_objects = []

    for object in data:
        mass = data[object]["mass"]
        position = (data[object]["perihelion"] + 0.4, 0)
        velocity = (0, data[object]["max_speed"])

        if object == "Sun":
            solar_system_objects.append(Sun(solar_system, mass))
        else:
            solar_system_objects.append(Planet(
                solar_system, mass, data[object]["pic_path"], position, (0, data[object]["max_speed"])))

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
