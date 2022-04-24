from json import load
from sys import argv

with open("Example.json") as f:
    data = load(f)

with open("Example.csv","w") as fout:
    for sublist in data['report']['StudentList']['List']:
        for row in sublist['StudentData']['DataRow']:
            name,year,reg,adno,house = [i["#text"] for i in row['CellData']]

            second,first = name.split(", ")
            tutor = reg.split("-")[1]
            house = house.split("-")[1]

            print(adno,first,second,tutor,house,sep=",",file=fout)
