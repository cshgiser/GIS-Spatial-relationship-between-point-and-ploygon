# isPointInPloygon
Providing two algorithms for determining whether a point is in a ploygon using Python

## input and output in python file

These two methods both need two parameters.<br>

**parameter1:** a tuple indicating a point. e.g., (2, 2.5)<br>

**parameter2:** a list indicating a ploygon. this list also includes several sub lists, indicating several enclosed regions. <br>
  e.g., [[(1, 1), (2, 3), (2, 4), (1, 6), (3, 10), (11, 8), (11, 3), (7, 0.5), (1, 1)], [(3, 4), (3, 3), (4, 3), (4, 4), (3, 4)]]<br>

***Note that in each sub list, the first point should be equal to the last point in order to form an enclosed region.<br>***

Then, the differe results will be returned, including three circumstances.

1. point is not in the ploygon
2. point is on edge of the ploygon
3. point is in the ploygon


## method1

In python file, it was defined as function method1(ploygon, point)<br>

<center><img src="https://github.com/cshgiser/isPointInPloygon/blob/main/image/method1.jpg" width="300"/></center>

the procedures of this algorithm is as following:<br>

>The minimum bounding rectangle (MBR) is obtained firstly to filter points that are not in MBR. In this case, the point can not be located in the ploygon.<br>
>
>If point is not located in MBR, then,  this function will **return 'point is not in the ploygon'**.<br>
>
>If point is located in MBR, then,
>>Traverse each line in ploygon, determining whether the point is on the edge of the given ploygon. <br>
>>
>>If the point is located on the edge, then, **return 'point is on edge of the ploygon'**.<br>
>>
>>If the point is not located on the edge, then, 
>>>Determine the number of intersection points of vertical line segment and ploygon edges. The vertical line's start point is input point, and its end point should satisfy its y coordinate being less than MBR's minimum y coordinate.
>>>
>>>If the 

## method2

In python file, it was defined as function method2(ploygon, point)<br>


|<center><img src="https://github.com/cshgiser/isPointInPloygon/blob/main/image/method2_1.jpg" width="300"/></center>|<center><img src="https://github.com/cshgiser/isPointInPloygon/blob/main/image/method2_2.jpg" width="300"/></center>|<center><img src="https://github.com/cshgiser/isPointInPloygon/blob/main/image/method2_3.jpg" width="300"/></center>|
|  ----  | ----  | ----  |


to be continued...
