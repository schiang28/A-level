import xml.etree.ElementTree as ET
from sys import argv
from json import dump

data = {}

root = ET.parse(argv[1]).getroot()
for row in root.iter("DataRow"):
    name, year, reg, adno, house = [item.text for item in row]

    second, first = name.split(", ")
    tutor = reg.split("-")[1]
    house = house.split("-")[1]

    data[f"{first} {second}"] = {"adno": adno, "tutor": tutor, "house": house}
with open("Written.json", "w") as fout:
    dump(data, fout, indent=2)

