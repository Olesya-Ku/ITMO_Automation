def calculate_days(years, months):
    day = years * 365 + months * 29
    return day
years = int(input("Введите количество лет: "))
months = int(input("Введите количество месяцев: "))
total_day = calculate_days(years, months)
print(f"Общее количество дней за {years} лет и {months} месяцев: {total_day} дней")



