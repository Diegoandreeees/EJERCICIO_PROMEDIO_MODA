"""
Diego Diaz
27.352.609

"""

import csv
import statistics

edades = []
with open('datos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        edades.append(int(row['edad']))

def getPromedio(datos):
    return statistics.mean(datos)

def getModa(datos):
    return statistics.mode(datos)

if __name__ == "__main__":
    print(getPromedio(edades))
    print(getModa(edades))

