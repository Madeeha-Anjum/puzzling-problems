# 1603. Design Parking System

In English: 
- Big, medium, and small spaces in the parking lot with fixed slots for each size.
- 
class ParkingSystem(int big, int medium, int small):
 - constructor has the number of slots 
    - bool addCar(int carType):
        - Checks whether there is a parking space of carType
        - carType can be of three kinds: big =1 , medium =2, small =3.
        - 

A car can only park in a parking space of its carType

Input/ output: If there is no space available, return false, else park the car in that size space and return true.
Example:

Input

["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]