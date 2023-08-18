def build_calendar(offset, days):
    weeks = (offset + days) // 7 + 1
    month_calendar = []
    for w in range(1, weeks + 1):
        week_row = []
        for d in range(1, 8):
            this_cell = (w - 1) * 7 + d
            if this_cell <= offset or this_cell - offset > days:
                this_date = 0
            else:
                this_date = this_cell - offset
            week_row.append(this_date) 
        month_calendar.append(week_row)
    return month_calendar

print(build_calendar(2, 31))
