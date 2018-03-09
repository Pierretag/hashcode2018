import sys
import json
from vehicule import Vehicule
import copy

def main(fileName):
    data = openFile(fileName)
    vehicules = simulateSteps(data)
    writeAnswer(vehicules)


def openFile(file):
    data = {"header": {}, "list": []}
    identifiant = 0
    with open(file, 'rU') as f:
        token = f.readline().split()
        data["header"] = {"rows": token[0], "columns": token[1], "nbVehicules": token[2], "nbRides": token[3],
                          "bonus": token[4], "nbStep": token[5]}
        for line in f:
            token = line.split()
            data["list"].append({"id": identifiant, "startCord": {"x": token[0], "y": token[1]},
                                 "endCoord": {"x": token[2], "y": token[3]}, "startTime": token[4],
                                 "endTime": token[5]})
            identifiant = identifiant + 1
    return data


def simulateSteps(data) -> list():
    vehicules = list()
    nbVehicule = int(data["header"]["nbVehicules"])
    for i in range(nbVehicule):
        vehicules.append(Vehicule())

    rideInProgress = copy.deepcopy(data["list"])
    steps = int(data["header"]["nbStep"])
    for step in range(steps):
        for vehiculeCourant in vehicules:
            if (vehiculeCourant.tempsIndispo > 1):
                vehiculeCourant.tempsIndispo = vehiculeCourant.tempsIndispo - 1
            else :
                if(vehiculeCourant.currentRide != 0):
                    vehiculeCourant.endOfRide()
                vehiculeCourant.bookRide(step, rideInProgress)


    return vehicules


def writeAnswer(vehicules):
    outputFile = open("result.out", "w")
    for vehicule in vehicules:
        line = str(len(vehicule.listRides))
        rides = vehicule.listRides
        for ride in rides:
            line = line + ' ' + str(ride["id"])
        outputFile.write(line + '\n')


if __name__ == '__main__':

    if (len(sys.argv) > 1):
        inputfileName = sys.argv[1]
    else:
        inputfileName = "c_no_hurry.in"

    main(inputfileName)
