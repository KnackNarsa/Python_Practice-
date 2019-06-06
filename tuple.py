# Create first tuple

tuple1 = ("disco",10,1.2)
tuple1

# Print the type of the tuple 
type(tuple1)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# use negative index to get the value of the last element

tuple1[-1]

# Use negative index to get the value of the second last element

tuple1[-2]

# Use negative index to get the value of the third last element

tuple1[-3]

# Concatenate two tuples 
tuple2 = tuple1 + ("hard rock", 10)
tuple2

print(tuple2[-2])

# Slice from index 0 to index 2

print(tuple2[0:3])

# Slice from index 3 to index 4

print(tuple2[3:5])
