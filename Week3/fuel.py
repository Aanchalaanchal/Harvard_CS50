def main():
    perc = get_frac()
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
            new_num = int(num)
            new_den = int(den)
            if new_num < new_den:
                return new_num*100/new_den
        except (ValueError, ZeroDivisionError):
            pass
        
main()
