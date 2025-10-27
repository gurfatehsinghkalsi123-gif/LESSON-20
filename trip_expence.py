def hotel_cost(days):
    return 5000 * days

def plane_cost(destination):
    if destination == 'bali':
        return 15000
    if destination == "canada":
        return 23000
    if destination == "thailand":
        return 10000
    if destination == "andaman and nicobar":
        return 7000
def car_rent(days):
    if days> 10:
        return 500 * days - 700
    else:
        return 500 * days
def total_trip_cost(days, destination, extraexpence):
    return hotel_cost(days)+plane_cost(destination)+car_rent(days)+extraexpence
days = int(input("how much days you would travel: "))
destination = input("where you want ot travel")
extra = int(input("any extra expence? : "))
print("hotel amount = ", hotel_cost(days))
print("car rental amount = ", car_rent(days))
print("plane ride amount = ", plane_cost(destination))
print("total amount = ", total_trip_cost(days, destination, extra))
        