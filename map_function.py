import math
def area(r):
    return math.pi * (r ** 2)
radii = [2,5,7.1,8,6]

#Method 1: Direct Method

areas = []
for r in radii:
    a=area(r)
    areas.append(a)
print(areas)

# Method 2: map function -------  map(f,data)    :--data:a1,a2,....an      function:f
# it gives   f(a1),f(a2),....f(an)

print(list(map(area,radii)))


# ---$ python map_function.py
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 201.06192982974676, 113.09733552923255]
# [12.566370614359172, 78.53981633974483, 158.36768566746147, 201.06192982974676, 113.09733552923255]--output------
