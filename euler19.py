import time
st = time.time()
# Function that returns the day of the week for a given date
# Input: year, month, day
# Output: day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
def get_weekday(year, month, day):
    if month <= 2:
        month += 12
        year -= 1
    century = year // 100
    year_of_century = year % 100
    weekday = (day + 13*(month + 1)//5 + year_of_century + year_of_century//4 + century//4 - 2*century) % 7
    return weekday

# Function that checks if a given year is a leap year
# Input: year
# Output: True if leap year, False otherwise
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Function that returns the number of days in a given month
# Input: month, year
# Output: number of days in the month
def get_num_days(month, year):
    month -= 1
    days_in_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month]

# Start and end dates for the counting of Sundays on the first of the month
start_date = [1, 1, 1901]
end_date = [31, 12, 2000]

num_sundays = 0
for year in range(start_date[2], end_date[2] + 1):
    for month in range(1, 13):
        if get_weekday(year, month, 1) == 0:
            num_sundays += 1

print(num_sundays)
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
