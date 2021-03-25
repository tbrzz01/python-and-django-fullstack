some_range = range(5)
print(some_range)


x = [1,2,3,4]
out = []

for num in x:
    out.append(num**2)

print(out)


out_new = [num**2 for num in x]
print(out_new)
