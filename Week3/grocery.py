my_dict = {
    }
while True:
    try:
        item = str(input().upper())
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    except KeyError:
        pass
    except EOFError:
        groceries = sorted(my_dict.items())
        for i in groceries:
            print(groceries[i], i)
        break
