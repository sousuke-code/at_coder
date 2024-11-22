s = input()
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for week in weeks:
    if week == s:
        print(weeks.index('Saturday') - weeks.index(week))
        break