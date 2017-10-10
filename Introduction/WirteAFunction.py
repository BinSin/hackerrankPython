def is_leap(year):
    leap = False

    if year % 400 == 0 :
        leap = True
    elif year % 4 == 0 and year % 100 != 0 :
        leap = True

    return leap

print(is_leap(2000))
print(is_leap(2012))
print(is_leap(3000))
