def searching(b,numbers):
    for i in range (len(numbers)) :
        key = 0
        if (b == numbers[i]) :
            key = i
            break
        else :
            key = "nil"
    return (key)

b = 3 
numbers = [0,1,2,4,5,6,]
print(searching(b, numbers))