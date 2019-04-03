from Navy_fleet import *
import random
import time


class TravelNavyFleet:
    def __init__(self, name, transporterTanker_01_FirstSpeed, transporterTanker_01_Type, transporterTanker_01_Name,
                 transporterTanker_02_FirstSpeed, transporterTanker_02_Type, transporterTanker_02_Name, fightingShip_01_FirstSpeed,
                 fightingShip_01_Type, fightingShip_01_Name, fightingShip_02_FirstSpeed, fightingShip_02_Type, fightingShip_02_Name,
                 submarine_01_FirstSpeed, submarine_01_Type, submarine_01_Name, submarine_02_FirstSpeed, submarine_02_Type, submarine_02_Name):

        self.transporterTanker_01_FirstSpeed = transporterTanker_01_FirstSpeed
        self.transporterTanker_01_Type = transporterTanker_01_Type
        self.transporterTanker_01_Name = transporterTanker_01_Name
        self.transporterTanker_02_FirstSpeed = transporterTanker_02_FirstSpeed
        self.transporterTanker_02_Type = transporterTanker_02_Type
        self.transporterTanker_02_Name = transporterTanker_02_Name
        self.fightingShip_01_FirstSpeed = fightingShip_01_FirstSpeed
        self.fightingShip_01_Type = fightingShip_01_Type
        self.fightingShip_01_Name = fightingShip_01_Name
        self.fightingShip_02_FirstSpeed = fightingShip_02_FirstSpeed
        self.fightingShip_02_Type = fightingShip_02_Type
        self.fightingShip_02_Name = fightingShip_02_Name
        self.submarine_01_FirstSpeed = submarine_01_FirstSpeed
        self.submarine_01_Type = submarine_01_Type
        self.submarine_01_Name = submarine_01_Name
        self.submarine_02_FirstSpeed = submarine_02_FirstSpeed
        self.submarine_02_Type = submarine_02_Type
        self.submarine_02_Name = submarine_02_Name
        self.name = name


    def inputTravelInformation(self):
        self.A = input("შეიყვანეთ A პუნქტი:\n")
        self.B = input("შეიყვანეთ B პუნქტი:\n")
        try:
            self.distance = int(input("შეიყვანეთ მანძილი:\n"))
        except:
            print('გთხოვთ შეიყვანოთ მხოლოდ რიცხვითი მნიშვნელობა!')

    def speedDecorate(func):
        """სიჩქარის ცვლილება გარემოების შესაბამისად"""
        def wrapper(self):
            speed = func(self)
            firstSpeed = func(self)

            weather = [["მზე",0], ["წვიმა",5], ["ქარიშხალი", 30]]
            directionOfFlow = [["არასაწინააღმდეგო",0], ["საწინააღმდეგო",15]]

            weather = random.choice(weather)
            directionOfFlow = random.choice(directionOfFlow)

            directionString = directionOfFlow[0]
            directionDecrease = int(directionOfFlow[1])

            weatherString = weather[0]
            weatherSpeedDecrease = int(weather[1])

            speed = speed - ((speed/100)*directionDecrease)
            speed = speed - ((speed/100)*weatherSpeedDecrease)

            self.navyFleetSpeed = speed
            self.firstSpeedOfNavyFleet = firstSpeed
            self.directionString = directionString
            self.weatherString = weatherString
        return wrapper


    @speedDecorate
    def GetNavyFleetSpeed(self):
        """მაქსიმალური სიჩქარის დადგენა ობიექტებს შორის,
        იმისათვის რომ საზღვაო ფლოტის წვერებმა ერთად მოახდინონ გადაადგილება"""

        navyFleetSpeed = min(self.transporterTanker_01_FirstSpeed, self.transporterTanker_02_FirstSpeed,
                             self.fightingShip_01_FirstSpeed, self.fightingShip_02_FirstSpeed,
                             self.submarine_01_FirstSpeed, self.submarine_02_FirstSpeed)
        return navyFleetSpeed

    def travel(self):
        line = "---------------------------------------------------------------------------------------------"
        print(line)
        print("საზღვაო ფლოტი " + self.name + ": {}".format(('\n'
                                                + line
                                                + '\n'
                                                + self.transporterTanker_01_Name
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.transporterTanker_01_Type
                                                + '\n'
                                                + self.transporterTanker_02_Name
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.transporterTanker_02_Type
                                                + '\n'
                                                + self.fightingShip_01_Name
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.fightingShip_01_Type
                                                + '\n'
                                                + self.fightingShip_02_Name
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.fightingShip_02_Type
                                                + '\n'
                                                + self.submarine_01_Name
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.submarine_01_Type
                                                + '\n'
                                                + self.submarine_02_Name)
                                                + ' -> '
                                                + 'ტიპი: '
                                                + self.submarine_02_Type
                                                + '\n'
                                                + line))

        time.sleep(1)
        print("საზღვაო ფლოტი '{}', {} -იდან მიემართება {} -ში".format(self.name, self.A, self.B))
        print(line)
        print("გასავლელი მანძილი უდრის {}-ს".format(self.distance))
        print(line)
        time.sleep(1)
        print("საზღვაო ფლოტის თავდაპირველი სიჩქარე უდრიდა {}-ს, მაგრამ გარემოებისა და ამინდის მხრივ, \n \tრადგან გემი მიემართებa {} მიმართულებით და არის {} ფლოტის სიჩქარე გახდა {} "
              .format(self.firstSpeedOfNavyFleet, self.directionString, self.weatherString, self.navyFleetSpeed))
        print(line)
        time.sleep(1)
        print("საზღვაო ფლოტი '{}' მიემართება დანიშნულების ადგილისაკენ".format(self.name))
        exceededdistance = 0
        distance = self.distance
        while self.distance > 0:
            print("ფლოტის მიერ განვლილი მანძილია {}".format(exceededdistance))
            print("დარჩა {}".format(distance))
            distance -= self.navyFleetSpeed
            exceededdistance += self.navyFleetSpeed
            time.sleep(1)

        print("საზღვაო ფლოტი '{}' წარმატებით ჩავიდა დანიშნულების ადგილას!".format(self.name))


NavyFleet_01 = TravelNavyFleet("შეუდარებელნი", transporterTanker_01_FirstSpeed, transporterTanker_01_Type, transporterTanker_01_Name,
                 transporterTanker_02_FirstSpeed, transporterTanker_02_Type, transporterTanker_02_Name, fightingShip_01_FirstSpeed,
                 fightingShip_01_Type, fightingShip_01_Name, fightingShip_02_FirstSpeed, fightingShip_02_Type, fightingShip_02_Name,
                 submarine_01_FirstSpeed, submarine_01_Type, submarine_01_Name, submarine_02_FirstSpeed, submarine_02_Type, submarine_02_Name)


NavyFleet_01.inputTravelInformation()
NavyFleet_01.GetNavyFleetSpeed()
NavyFleet_01.travel()