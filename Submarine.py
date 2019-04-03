class Submarine:
    def __init__(self, name, max_speed_without_burden, max_burden_weight, burden_weight):
        # წყალქვეშა ნავის სახელი
        self.name = name
        # მაქსიმალური სიჩქარე ტვირთის გარეშე
        self.max_speed_without_burden = max_speed_without_burden
        # მაქსიმალური ტვირთის წონა
        self.burden_weight = max_burden_weight
        # ტვირთის წონა
        self.burden_weight = burden_weight

    def calculateSubmarineMaxSpeed(self):
        """ეს მეთოდი ითვლის წყალქვეშა ნავის მაქსიმალურ სიჩქარეს ტვირთის ზომის შესაბამისად"""
        speed = self.max_speed_without_burden - ((self.max_speed_without_burden/3) / 100) \
                * (self.burden_weight / self.burden_weight * 100)
        return speed


class SubmarineForFight(Submarine):
    def __init__(self, name, max_speed_without_burden,
                 max_burden_weight, burden_weight):
        Submarine.__init__(self, name, max_speed_without_burden,
                           max_burden_weight, burden_weight)
        # წყალქვეშა ნავის ტიპი
        self.type = "საბრძოლო წყალქვეშა ნავი"

    def getType(self):
        return self.type

    def getName(self):
        return self.name


class SubmarineForTransport(Submarine):
    def __init__(self, tanker_name, tanker_max_speed_without_burden,
                 tanker_max_burden_weight, tanker_burden_weight):
        Submarine.__init__(self, tanker_name, tanker_max_speed_without_burden,
                           tanker_max_burden_weight, tanker_burden_weight)
        # წყალქვეშა ნავის ტიპი
        self.type = "სატრანსპორტო წყალქვეშა ნავი"

    def getType(self):
        return self.type

    def getName(self):
        return self.name
