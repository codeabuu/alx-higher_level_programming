#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            print(item, end=" ")
            count += 1
            if count >= x:
                break
            print()
            return (count)
    except:
            print("An error occurred.")
            return (count)

