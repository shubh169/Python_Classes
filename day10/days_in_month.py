def is_leap_year(new_year):
    if new_year%4==0 and new_year!=100 or new_year%400==0:
        return True
    else:
        False
        
def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and is_leap_year(year)==True:
        return 29
    else:
        return month_days[month-1]
    
year=int(input("enter your year:"))
month=int(input("enter your month:"))
days=days_in_month(year,month)
print(days)