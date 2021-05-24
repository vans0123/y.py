def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 ==0)
        return true
    else:
        return false
a = int(input('請輸入年:'))
print(is_leap_year(a))
