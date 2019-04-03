class TransporterTanker:
    def __init__(self, name, max_speed_without_burden, max_burden_weight, burden_weight):
        # გადამზიდი ტანკერის სახელი
        self.name = name
        # მაქსიმალური სიჩქარე ტვირთის გარეშე
        self.max_speed_without_burden = int(max_speed_without_burden)
        # მაქსიმალური ტვირთის წონა
        self.max_burden_weight = int(max_burden_weight)
        # ტვირთის წონა
        self.burden_weight = int(burden_weight)

    def calculateShipMaxSpeed(self):
        """ეს მეთოდი ითვლის ტანკერის მაქსიმალურ სიჩქარეს ტვირთის წონის შესაბამისად"""
        speed = self.max_speed_without_burden - ((self.max_speed_without_burden/3) / 100) \
                       * (self.burden_weight / self.max_burden_weight * 100)
        return speed


class TransporterTankerForFood(TransporterTanker):
    def __init__(self, name, max_speed_without_burden,
                 max_burden_weight, burden_weight):
        TransporterTanker.__init__(self, name, max_speed_without_burden,
                                   max_burden_weight, burden_weight)

        # ტანკერის ტიპი
        self.type = "სურსათის გადამზიდი"

    def getType(self):
        return self.type

    def getName(self):
        return self.name


class TransporterTankerForClothes(TransporterTanker):
    def __init__(self, name, max_speed_without_burden,
                 max_burden_weight, burden_weight):
        TransporterTanker.__init__(self, name, max_speed_without_burden,
                                   max_burden_weight, burden_weight)

        # ტანკერის ტიპი
        self.type = "ტანსაცმლის გადამზიდი"

    def getType(self):
        return self.type

    def getName(self):
        return self.name

