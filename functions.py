def mintohour(minutes):
    hour=minutes/60
    return hour
minutes=int(input("enter minutes:"))
print(mintohour(minutes))
def secondstohour(seconds):
     hour=(seconds/60)/60
     return hour
seconds=int(input("enter seconds:"))
print(secondstohour(seconds))