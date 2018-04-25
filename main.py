import datetime
from cmd_tools import write_int


months = write_int('Months number: ')
cur_year = write_int('Year from (optional): ', 1970, default=datetime.datetime.now().year)
cur_month = write_int('Month from (optional): ', min=1, max=12, default=datetime.datetime.now().month)

res = {}

for month in range(0, months):
    date = datetime.date(year=cur_year, month=cur_month, day=13)
    is_friday = date.weekday() == 4
    res[str(date)] = is_friday

    # print('X' if is_friday else '.', end='')
    print('{} {} ({})'.format('*' if is_friday else ' ', date, date.strftime("%A")))

    cur_month += 1
    if cur_month > 12:
        cur_month = 1
        cur_year += 1

# print(res)
