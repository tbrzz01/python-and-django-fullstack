# Booleans
true = True
false = False

# Tuples
t = (1, 2, 3)
print(t[0])
print(t)
# tuples are immutable, cannot reassign items in tuple

# Sets
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(0.1)
print(x)
# Can't add non-unique items to a set, this will not add another 1 to the set
x.add(1)
print(x)
