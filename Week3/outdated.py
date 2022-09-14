months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        m, d, y = date.split('/')
        if int(m) <= 12 and int(m) >= 1 and int(d) <= 31 and int(d) >= 1:
            print(f"{int(y):04}", "-", f"{int(m):02}", "-", f"{int(d):02}")
            break
    except:
        pass
    try:
        m2, d2, y2 = date.split(' ')
        if m2 in months:
            month = months.index(m2) + 1
            print(f"{int(y2):04}", "-", f"{int(month):02}", "-", f"{int(d2):02}")
            break
    except:
        pass
