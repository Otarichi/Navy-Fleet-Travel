class FightingShip:
    def __init__(self, name, max_speed_without_burden, max_burden_weight, burden_weight):
        # საბრძოლო გემის სახელი
        self.name = name
        # მაქსიმალური სიჩქარე ტვირთის გარეშე
        self.max_speed_without_burden = max_speed_without_burden
        # მაქსიმალური ტვირთის წონა
        self.max_burden_weight = max_burden_weight
        # ტვირთის წონა
        self.burden_weight = burden_weight

    def calculateShipMaxSpeed(self):
        """ეს მეთოდი ითვლის გემის მაქსიმალურ სიჩქარეს ტვირთის ზომის შესაბამისად"""
        speed = self.max_speed_without_burden - int((self.max_speed_without_burden/3) / 100) \
                       * (self.burden_weight / self.max_burden_weight * 100)
        return speed


class FightingShipForAircraft(FightingShip):
    def __init__(self, name, max_speed_without_burden,
                 max_burden_weight, burden_weight):
        FightingShip.__init__(self, name, max_speed_without_burden,
                              max_burden_weight, burden_weight)
        # გემის ტიპი
        self.type = "საბრძოლო გემი თვითმფრინავების მოსაგერიებლად"

    def getType(self):
        return self.type

    def getName(self):
        return self.name


class FightingShipForFightingShips(FightingShip):
    def __init__(self, name, max_speed_without_burden,
                 max_burden_weight, burden_weight):
        FightingShip.__init__(self, name, max_speed_without_burden,
                              max_burden_weight, burden_weight)
        # გემის ტიპი
        self.type = "საბრძოლო გემი საბრძოლო გემების მოსაგერიებლად"

    def getType(self):
        return self.type

    def getName(self):
        return self.name
