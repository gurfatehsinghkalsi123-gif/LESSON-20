from datetime import date , time , datetime

datet = date.today()
print("Today's date is :", datet)
timest = datetime.now()
print("the current timestamp is: ", timest)
print("\nThe current year is:", datet.year,"the current month is:", datet.month,"and the current date is", datet.day)