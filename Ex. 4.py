def fiest(numbers):
    print("given list;",numbers)
    first_num=numbers[0]
    last_num=numbers[-1]

    if first_num ==last_num:
        return True
    else:
        return False
    x=[10,20,30,40,10]
    print("Result is",First(x))
    y=[50,60,70,80,30]
    print("Result is",First(y))