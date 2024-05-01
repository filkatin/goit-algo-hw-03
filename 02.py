import random

def get_numbers_ticket(min, max, quantity):
    if max not in range(1, 1000+1):
        print("Maximum number is not between 1 and 1000")
    elif min not in range(1, max+1):
        print("Minimum number is not between 1 and Maximum number")
    elif type(quantity) is not int:
        print("Quantity number is not integer")
    elif quantity>(max-min+1):
        print("Quantity number is too large")
    else:
        numbers_list = []
        while len(numbers_list) < quantity:
            numbers_list.append(random.randrange(min, max+1))
            numbers_list = list(set(numbers_list))
        
        return sorted(numbers_list)


print("Result: ", get_numbers_ticket(1, 49, 6))