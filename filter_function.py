import statistics

data = [1.3,3.2,0.8,1.9,-2.3]
avg = statistics.mean(data)
print(avg)

print(list(filter (lambda x: x > avg , data)))

print(list(filter (lambda x: x < avg , data)))


# output
# $ python filter_function.py
# 0.9800000000000001
# [1.3, 3.2, 1.9]
# [0.8, -2.3]
# ---------------------------------------------------------------------------------------------------------------------------------------

# Another use of filter function ----Remove missing data

countries= ["","India","China","","Brazil"]
print(list(filter(None,countries)))
# ------output------------
# ['India', 'China', 'Brazil']