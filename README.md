# GIS - Spatial Relationship Between Point and Polygon

This repository provides two Python algorithms to determine the spatial relationship between a point and a polygon (including polygons with holes).

## Input and Output

Both methods utilize the following parameters:

* **parameter1 (tuple):** A tuple indicating a point coordinate. 
    * *Example:* `(2, 3.5)`
* **parameter2 (list):** A list representing the polygon. This list contains one or more sub-lists, where each sub-list represents an enclosed region (the exterior ring or interior holes).
    * *Example:* `[[(1, 1), (2, 3), (2, 4), (1, 1)], [(3, 4), (3, 3), (4, 3), (3, 4)]]`
    * **Note:** In each sub-list, the first point must be identical to the last point to form a closed loop.

**The functions return one of three strings:**
1. `point is not in the ploygon`
2. `point is on edge of the ploygon`
3. `point is in the ploygon`

---

## Method 1: Ray Casting Algorithm

Defined as `method1(ploygon, point)` in the script.



### Procedure:
1.  **MBR Filtering:** The Minimum Bounding Rectangle (MBR) is calculated first. If the point is outside the MBR, the function immediately returns that the point is not in the polygon.
2.  **Edge Detection:** The algorithm traverses each segment of the polygon. If the point satisfies the `isOnEdge` condition (based on the triangle inequality of distances), it returns that the point is on the edge.
3.  **Ray Intersection:** A vertical ray is cast from the point downwards. The algorithm counts the number of times this ray intersects with the polygon edges.
    * **Intersection Logic:** To avoid double-counting, if a ray hits a vertex, it is counted if it hits the "start" of a segment but ignored if it hits the "end."
4.  **Parity Check:** * If the number of intersections is **odd**, the point is inside.
    * If the number of intersections is **even**, the point is outside.

---

## Method 2: Sum of Angles (Winding Number)

Defined as `method2(ploygon, point)` in the script.



### Procedure:
1.  **Initial Checks:** Like Method 1, this method begins with MBR filtering and an edge-on-polygon check for efficiency.
2.  **Vector Calculation:** For every segment $(V_i, V_{i+1})$ in the polygon, two vectors are created: one from the target point to $V_i$ and one from the target point to $V_{i+1}$.
3.  **Angle Summation:** * The angle between these vectors is calculated using the Dot Product and `math.acos`.
    * The **Cross Product** is used to determine the orientation (direction) of the angle. If the cross product is negative, the angle is treated as negative.
4.  **Result Interpretation:**
    * The total sum of these signed angles is calculated.
    * If the sum divided by $2\pi$ is an **odd integer**, the point is considered inside the polygon.
    * If the sum results in **0** (or an even multiple of $2\pi$), the point is outside.

---

## Comparison of Methods

| Feature | Method 1 (Ray Casting) | Method 2 (Sum of Angles) |
| :--- | :--- | :--- |
| **Computational Speed** | Fast (Linear equations) | Slower (Trigonometric functions) |
| **Complexity** | Simple logic | Uses Vector Calculus |
| **Robustness** | High, with vertex handling | Very High for complex shapes |

## Usage

```python
point = (2, 3.5)
polygon = [[(1, 1), (2, 3), (2, 4), (1, 6), (3, 10), (11, 8), (11, 3), (7, 0.5), (1, 1)]]

# Using Ray Casting
print(method1(polygon, point))

# Using Sum of Angles
print(method2(polygon, point))


to be continued...
