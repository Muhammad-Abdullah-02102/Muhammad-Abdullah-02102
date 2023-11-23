def multiply_sum(a,b):
    product = a*b
    
    if product <=1000:
        return product
  
    else:
        sum = a+b
        return sum
result =multiply_sum(20,30)
print(result)
result = multiply_sum(30,40)
print(result)