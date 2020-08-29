def sumOfFirsts(numbers):
    result = 0
    temp = 0
    while(True):
        x = -1
        found = False
        for j in range(temp,len(numbers)):
            if numbers[j] != 0 or found:
                if x == -1:
                    x = numbers[j]
                    found = True
                if numbers[j]-x > 0:
                    numbers[j] = numbers[j] - x
                elif numbers[j]-x == 0:
                    numbers[j] = 0
                    temp = j;
                else:                    
                    break
            #print(numbers)
        if x!=-1:
            #print(x)
            result+=x;
        if temp == len(numbers)-1:
            break;
    return result


a = [4,7,5,0,0,2,8,9]
print(sumOfFirsts(a))