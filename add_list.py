#methods to add data in list
#insert method
#append,extend
#concatinate(join)list

fruits1=["mango","apple"]
fruits1.insert(1,"grapes")     #add item at perticular index
print(fruits1)

fruits2=["papaya","watermelon"]
fruits=fruits1 + fruits2       #join 2 lists
print(fruits)

fruits1.extend(fruits2)      #extend----->fruits2 added in fruits1
print(fruits1)
print(fruits2)


fruits1.append(fruits2)      #add list inside list
print(fruits1)
