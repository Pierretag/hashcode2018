class Vehicule(object):
    def __init__(self):
        """
        Constructeur
        """
        self.posX=0
        self.posY=0
        self.listRides= []
        self.currentRide =0
        self.tempsIndispo = 0

    def evaluateRide(self,time,ride):
        """
        Ressort la rentabilité d'un Ride
        {"id":id "startCord":{"x":X,"y":Y}, "endCoord":{"x":X,"y":Y}, "startTime":st, "endTime":ed }
        """
        "Nombre de point = distance "
        nbpoint = abs(int(ride["endCoord"]["x"]) - int(ride["startCord"]["x"])) + abs(int(ride["endCoord"]["y"]) - int(ride["startCord"]["y"]))
        distanceToStartCoord = abs(int(ride["startCord"]["x"]) - int(self.posX)) + abs(int(ride["startCord"]["y"]) - int(self.posY))
        if distanceToStartCoord < (int(ride["startTime"])-time):
             nbpoint = nbpoint + 2
        tempsIndispo = self.calculTempsIndispo(time,ride)
        return nbpoint/tempsIndispo


    def calculTempsIndispo(self,time,ride):
        distance = abs(int(ride["endCoord"]["x"]) - int(ride["startCord"]["x"])) + abs(
            int(ride["endCoord"]["y"]) - int(ride["startCord"]["y"]))
        distanceToStartCoord = abs(int(ride["startCord"]["x"]) - int(self.posX)) + abs(
            int(ride["startCord"]["y"]) - int(self.posY))
        "calcul du temps d'indispo"
        return max(distanceToStartCoord,int(ride["startTime"])) + distance

    def bookRide(self,time,listRides):
        evaluation = list()
        maximum = 0
        for ride in listRides:
            renta = self.evaluateRide(time,ride)
            if renta > maximum:
                maximum = renta
                self.currentRide = ride

        self.tempsIndispo = self.calculTempsIndispo(time, self.currentRide)

        if self.currentRide in listRides :
            listRides.remove(self.currentRide)

    def endOfRide(self):
        self.posX = self.currentRide["endCoord"]["x"]
        self.posY = self.currentRide["endCoord"]["y"]
        self.listRides.append(self.currentRide)
