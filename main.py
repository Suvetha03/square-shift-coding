from helper_functions import orderSeating
from aeroplaneSeating import AeroplaneSeating
import re

# Inputs
seating_arrangement = input()
passenger_id = input()

# converting inputs in string format to list of integers
seating_arrangement = re.split('[,\[\]]', seating_arrangement)

seating_arrangement_list = []
for x in seating_arrangement:
    try:
        seating_arrangement_list.append(int(x))
    except:
        continue
passenger_id = re.split(',', passenger_id[1:-1])
passenger_id = [int(x) for x in passenger_id]
seating_arrangement = seating_arrangement_list

# Converting list of Input-1 into 2D array
seating_arrangement_list = []
matrix = []
for i in range(len(seating_arrangement)):
    matrix.append(seating_arrangement[i])
    if len(matrix) == 2:
        seating_arrangement_list.append(matrix)
        matrix = []

# Arranging the passenger IDs according to the priority
passenger_id = orderSeating(passenger_id)

# Creating the instance of AeroplaneSeating class
aeroplane1 = AeroplaneSeating(seating_arrangement_list, passenger_id)
aeroplane1.createSeating(seating_arrangement_list)
index = aeroplane1.fillAisleSeats(passenger_id)
passenger_id = passenger_id[index:]
if len(passenger_id) > 0:
    index = aeroplane1.fillWindowSeats(passenger_id)
passenger_id = passenger_id[index:]

if len(passenger_id) > 0:
    aeroplane1.fillMiddleSeats(passenger_id)
aeroplane1.displaySeating()
