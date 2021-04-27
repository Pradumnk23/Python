def health_calc(age, apples, wine):
    answer = (100-age) + (apples * 2.5) + (wine * 5)
    print(answer)

data = [20, 5, 2]
health_calc(data[0], data[1], data[2])
health_calc(*data)
# *data is called a sunpacking arguments, no need to write in array form..
