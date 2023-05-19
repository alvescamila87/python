import datetime

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def julian_calendar(year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    
    # Cálculo do dia juliano
    base_date = datetime.datetime(year, 1, 1)
    current_date = base_date
    julian_dates = []
    
    for days in days_in_month:
        julian_dates.extend([current_date.day for _ in range(days)])
        current_date += datetime.timedelta(days=days)
    
    return julian_dates

# Exemplo de uso
year = 2023
julian_dates = julian_calendar(year)
print(f"Calendário juliano para o ano {year}:\n")
print("Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec")
for i, day in enumerate(julian_dates):
    print(f"{day:02d}   ", end="")
    if (i + 1) % 12 == 0:
        print()
