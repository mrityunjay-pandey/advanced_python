class Distance:
    def __init__(self,km,m):
        self.km = km
        self.m = m
def add_distance(obj1,obj2):
    total_km = obj1.km + obj2.km
    total_m = obj1.m + obj2.m
    if (total_m > 1000):
        total_km += total_m//1000
        total_m = total_m % 1000
    return Distance(total_km,total_m)
obj1 = Distance(4,500)
obj2 = Distance(5,700)
obj = add_distance(obj1,obj2)
print(f"After addition total distance is {obj.km}km and {obj.m}m")