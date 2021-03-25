mylist = [1, 2, 3]
mylist_string = ['string', 2, 3, True]
print(mylist)
print(mylist_string)

print(mylist[0])
print(mylist[:2])
mylist[0] = 5
print(mylist)

mylist.append(10)
print(mylist)
listtwo = [6,7,8]
mylist.extend(listtwo)
print(mylist)
item = mylist.pop()
print(mylist)
print(item)
item = mylist.pop(0)
print(mylist)
print(item)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

mylist_nested = [1, 2, ['x', 'y', 'z']]
print(mylist_nested[2])
print(mylist_nested[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# List comprehension
first_col = [row[0] for row in matrix]

print(first_col)
