from functools import reduce

nums = [32, 35, 45, 254, 21, 96, 54, 86,73, 78]

print(list(filter(lambda n : n%2==0,nums)))

# We can also can it by using a varialble

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n: n*2, evens))

sum = reduce(lambda a,b : a+b, doubles)

sum2 = reduce(lambda a,b : a+b, evens)

print(evens)
print(doubles)
print(sum)
print(sum2)
