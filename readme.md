# Aeroplane Seating Arrangement
### Approach 
1.Creating a 3-d array

2.Ordering ID's according to given priorities

3.Filling Aisle seats 

4.Then followed by Window seats 

5.And at last Middle seats

6.Filled the seats
 
## Sample input 1
C:\Users\SUVETHA\AppData\Local\Programs\Python\Python39\python.exe C:/Users/SUVETHA/squareshift/main.py
[[3,2], [4,3], [2,3], [3,4]]

[29,59,14,11,3,13,15,18,12,16,6,17,7,47,61,5,21,2,41,9,10,8,19,1,4]\
Priority order:  [29, 59, 11, 3, 13, 17, 7, 47, 61, 5, 41, 19, 16, 8, 1, 4, 14, 15, 18, 12, 6, 21, 2, 9, 10] 

[18, 10, 29]
[6, 'xx', 7]


[59, 'xx', 'xx', 11]
[47, 'xx', 'xx', 61]
[16, 'xx', 'xx', 8]


[3, 13]
[5, 41]
[1, 4]


[17, 'xx', 12]
[19, 'xx', 21]
[14, 'xx', 2]
[15, 'xx', 9]



Process finished with exit code 0


## sample input 2
C:\Users\SUVETHA\AppData\Local\Programs\Python\Python39\python.exe C:/Users/SUVETHA/squareshift/main.py
[[4,2], [3,2], [4,3], [5,4]] \
[27,55,14,20,3,13,15,29,12,16,6,17,7,47,61,5,21,2,42,9,10,8,19,1,4]\
Priority order:  [3, 13, 29, 17, 7, 47, 61, 5, 19, 16, 8, 1, 4, 27, 55, 14, 20, 15, 12, 6, 21, 2, 42, 9, 10] 

[20, 42, 9, 3]
[12, 'xx', 'xx', 61]


[13, 10, 29]
[5, 'xx', 19]


[17, 'xx', 'xx', 7]
[16, 'xx', 'xx', 8]
[4, 'xx', 'xx', 27]


[47, 'xx', 'xx', 'xx', 15]
[1, 'xx', 'xx', 'xx', 6]
[55, 'xx', 'xx', 'xx', 21]
[14, 'xx', 'xx', 'xx', 2]



Process finished with exit code 0


## sample input 3
C:\Users\SUVETHA\AppData\Local\Programs\Python\Python39\python.exe C:/Users/SUVETHA/squareshift/main.py
[[1,4], [2,6], [5,7], [5,5]]

[29,43,45,11,3,13,32,18,89,16,6,17,7,75,62,5,21,2,41,9,10,8,15,1,4,98,34,49,81,34,67,54,23]


Priority order:  [29, 43, 11, 3, 13, 89, 17, 7, 5, 41, 67, 23, 32, 16, 8, 1, 4, 45, 18, 6, 75, 62, 21, 2, 9, 10, 15, 98, 34, 49, 81, 34, 54] 

[34]
['xx']
['xx']
['xx']


[29, 43]
[89, 17]
[67, 23]
[1, 4]
[75, 62]
[10, 15]


[11, 'xx', 'xx', 'xx', 3]
[7, 'xx', 'xx', 'xx', 5]
[32, 'xx', 'xx', 'xx', 16]
[45, 'xx', 'xx', 'xx', 18]
[21, 'xx', 'xx', 'xx', 2]
[98, 'xx', 'xx', 'xx', 34]
[49, 'xx', 'xx', 'xx', 81]


[13, 'xx', 'xx', 'xx', 54]
[41, 'xx', 'xx', 'xx', 'xx']
[8, 'xx', 'xx', 'xx', 'xx']
[6, 'xx', 'xx', 'xx', 'xx']
[9, 'xx', 'xx', 'xx', 'xx']



Process finished with exit code 0


## sample input 4
C:\Users\SUVETHA\AppData\Local\Programs\Python\Python39\python.exe C:/Users/SUVETHA/squareshift/main.py
[[2,4], [2,6], [5,4], [1,5]]

[29,43,45,11,3,13,32,18,89,16,6,17,7,75,62,5,21,2,41,9,10,8,15,1,4,98,34,49,81,34,67,54,23]


Priority order:  [29, 43, 11, 3, 13, 89, 17, 7, 5, 41, 67, 23, 32, 16, 8, 1, 4, 45, 18, 6, 75, 62, 21, 2, 9, 10, 15, 98, 34, 49, 81, 34, 54] 

[9, 29]
[15, 89]
[34, 67]
[81, 1]


[43, 11]
[17, 7]
[23, 32]
[4, 45]
[75, 62]
[21, 2]


[3, 'xx', 'xx', 'xx', 13]
[5, 'xx', 'xx', 'xx', 41]
[16, 'xx', 'xx', 'xx', 8]
[18, 'xx', 'xx', 'xx', 6]


[10]
[98]
[49]
[34]
[54]



Process finished with exit code 0


## sample input 5
C:\Users\SUVETHA\AppData\Local\Programs\Python\Python39\python.exe C:/Users/SUVETHA/squareshift/main.py
[[2,4], [3,4], [4,3], [3,2]]

[29,43,45,11,3,13,32,18,89,16,6,17,7,75,62,5,21,2,41,9,10,8,15,1,4,98,34,49,81,34,67,54,23]


Priority order:  [29, 43, 11, 3, 13, 89, 17, 7, 5, 41, 67, 23, 32, 16, 8, 1, 4, 45, 18, 6, 75, 62, 21, 2, 9, 10, 15, 98, 34, 49, 81, 34, 54] 

[75, 15]
[21, 17]
[9, 32]
[10, 45]


[43, 'xx', 11]
[7, 'xx', 5]
[16, 'xx', 8]
[18, 'xx', 6]


[3, 'xx', 'xx', 13]
[41, 'xx', 'xx', 67]
[1, 'xx', 'xx', 4]


[89, 'xx', 62]
[23, 'xx', 2]



Process finished with exit code 0



