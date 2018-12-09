from functools import reduce

players = [('a',[10,100,8000,37,47]),('b',[10,0,9000,200])]

# print(reduce(lambda x,y: max(y,x),players))
print (reduce(lambda a,b : a if a < b else b,players))