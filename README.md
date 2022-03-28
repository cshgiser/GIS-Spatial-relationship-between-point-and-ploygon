# isPointInPloygon
Providing two algorithms for determining whether a point is in a ploygon using Python

## input and output in python file
the method need to two parameters.
**parameter1:** a tuple indicating a point. e.g., (2, 2.5)
**parameter2:** a list indicating a ploygon. this list also includes several sub lists, indicating several enclosed regions. 
  e.g., [[(1, 1), (2, 3), (2, 4), (1, 6), (3, 10), (11, 8), (11, 3), (7, 0.5), (1, 1)], [(3, 4), (3, 3), (4, 3), (4, 4), (3, 4)]]
Note that in each sub list, the first point should be equal to the last point inorder to form a enclosed region.

then, the differe results will be returned, including three circumstances.

1. point is not in the ploygon
2. point is on edge of the ploygon
3. point is in the ploygon



