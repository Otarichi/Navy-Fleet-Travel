from Transporter_tanker import *
from Fighting_ship import *
from Submarine import *

transporterTanker_01 = TransporterTankerForFood("გადამზიდი 01", 300, 100000, 80000)
transporterTanker_01_FirstSpeed = round(transporterTanker_01.calculateShipMaxSpeed())
transporterTanker_01_Type = transporterTanker_01.getType()
transporterTanker_01_Name = transporterTanker_01.getName()

transporterTanker_02 = TransporterTankerForClothes("გადამზიდი 02", 290, 90000, 75000)
transporterTanker_02_FirstSpeed = round(transporterTanker_01.calculateShipMaxSpeed())
transporterTanker_02_Type = transporterTanker_02.getType()
transporterTanker_02_Name = transporterTanker_02.getName()


fightingShip_01 = FightingShipForAircraft("გამანადგურებელი 01", 400, 120000, 100000)
fightingShip_01_FirstSpeed = round(fightingShip_01.calculateShipMaxSpeed())
fightingShip_01_Type = fightingShip_01.getType()
fightingShip_01_Name = fightingShip_01.getName()

fightingShip_02 = FightingShipForFightingShips("გამანადგურებელი 02", 410, 115000, 90000)
fightingShip_02_FirstSpeed = round(fightingShip_02.calculateShipMaxSpeed())
fightingShip_02_Type = fightingShip_02.getType()
fightingShip_02_Name = fightingShip_02.getName()


submarine_01 = SubmarineForFight("წყალქვეშა ნავი 01", 380, 115000, 115000)
submarine_01_FirstSpeed = round(submarine_01.calculateSubmarineMaxSpeed())
submarine_01_Type = submarine_01.getType()
submarine_01_Name = submarine_01.getName()

submarine_02 = SubmarineForTransport("წყალქვეშა ნავი 02", 350, 120000, 115000)
submarine_02_FirstSpeed = round(submarine_02.calculateSubmarineMaxSpeed())
submarine_02_Type = submarine_02.getType()
submarine_02_Name = submarine_02.getName()