
def IsLeapYear(year):
    if year%4!=0:
        return False
    if year%100!=0:
        return True
    if year%400==0:
        return True
    return False

if __name__ == "__main__":
    year=int(input("check is leap year or not"))
    if IsLeapYear(year):
        print("write year is a leap year")
    else:
        print("write year isn't leap year")
    