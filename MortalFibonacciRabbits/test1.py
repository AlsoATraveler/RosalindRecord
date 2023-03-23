list = [0,1,2,3]

list_shifted_backwards = list[1:] + list[:1]
list_shifted_forward = list[-1:] + list[:-1]

list[-1] = sum(list[1:])

a = list[-1:] + list[:-1]

print(list_shifted_backwards)
print(list_shifted_forward)

print(a)

