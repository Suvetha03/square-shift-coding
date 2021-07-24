import math
def isPrime(n):
    if(n==1):
        return 0
    for i in range(2, n):
        if n%i == 0:
            return 0
    return 1


def isPowerOfTwo(n):
    return n & (n-1)


def orderSeating(seating):
    prime = []
    power_of_2 = []
    other_ids = []
    for id in seating:
        if(isPrime(id)==1):
            prime.append(id)
        elif(isPowerOfTwo(id) == 0):
            power_of_2.append(id)
        else:
            other_ids.append(id)
    new_seating = prime
    new_seating.extend(power_of_2)
    new_seating.extend(other_ids)
    print(new_seating)
    return new_seating


def fillAisleSeats(aeroplane_seating, passenger_id):
    i = j = 0
    k = -1
    index = 0
    for id in passenger_id:
        try:
            aeroplane_seating[i][j][k] = passenger_id[index]
            index=index+1
        except:
            return aeroplane_seating , index
        if k==-1:
            i=i+1
            k=0
        else:
            k=-1
            if i == len(aeroplane_seating)-1:
                i=0
                j=j+1      

    return aeroplane_seating, index


def fillWindowSeats(aeroplane_seating, passenger_id):
    i=j=k=0
    index = 0
    for id in passenger_id:
        try:
            aeroplane_seating[i][j][k] = passenger_id[index]
            index = index+1
        except:
            return aeroplane_seating, index
        if i==0:
            i=k=-1
        elif i==-1:
            i=k=0
            j=j+1

    return aeroplane_seating, index


def fillMiddleSeats(aeroplane_seating, passenger_id):
    i = j = 0
    k = 1
    index = 0
    for id in passenger_id:
        try:
            aeroplane_seating[i][j][k] = passenger_id[index]
            k=k+1
            index = index+1
        except:
            return aeroplane_seating
        if k == len(aeroplane_seating[i][j]) - 1:
            k=1
            i=i+1
        
        if i == len(aeroplane_seating[i][j]) - 1:
            i = 0
            j=j+1
        
    return aeroplane_seating