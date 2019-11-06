def repeatedNTimes(list):
    for i in list:
        counter = 0
        for x in list:
            if i == x:
                counter += 1
        if counter == (len(list)/2):
            return i


list1 = [5,1,5,2,5,3,5,4]
print(repeatedNTimes(list1))
