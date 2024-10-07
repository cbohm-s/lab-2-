# x = 10.5
# print(type(x))
# print(x)

# x = int(x)
# print(type(x))
# print(x)

x = "This is a string"
y = 24
z = 25.5

print(type(x))
print(type(y))
print(type(z))

print(y + z)
print(type(y + z))

print(y + int(z))
print(type(y + int(z)))

print(z + float(y))
print(type(z + float(y)))

print(str(z))
print(type(str(z)))

print(x + str(y) + str(z))
print(type(x + str(y) + str(z)))

# print(x + y)
#you cannot do x + y due to type error ("Can only concatenate str not int to str")