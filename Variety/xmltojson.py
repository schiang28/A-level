from xmltodict import parse
from sys import argv
from json import dumps

infile = argv[1]
outfile = infile.replace("xml","json")

with open(infile,"r",encoding="utf-16") as x:
    with open(outfile,"w") as j:
        j.write(dumps(parse(x.read()),indent=2))
