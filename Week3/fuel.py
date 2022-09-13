def main():
    x, y = get_frac()
    perc = int(x)*100/int(y)
    if perc <= 1:
        print("E")
    elif perc >= 99:
        print("F")
    else:
        print(round(perc, 1), "%")

def get_frac():
    while True:
        try:
            num, den = input("Give me a fraction as x/y: ").split('/')
            if int(num) < int(den):
                return int(num), int(den)
        except (ValueError, ZeroDivisionError):
            pass
        
main()
