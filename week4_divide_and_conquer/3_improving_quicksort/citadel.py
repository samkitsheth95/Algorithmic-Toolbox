def consecutive(number):
    count = 0
    length = 1
    while( length * (length + 1) < 2 * number): 
        x = (1.0 * number - (length * (length + 1) ) / 2) / (length + 1) 
        if (x - int(x) == 0.0): 
            count += 1
        length += 1
    return count

print(consecutive(21))