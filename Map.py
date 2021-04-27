income = [10, 52, 78]

def double_imcome(dollars):
    return dollars * 2

new_income = list(map(double_imcome, income))
print(new_income)

for item in income:
    print(item * 2)

for x in income:
    print(income * 2)
# If we will write income * 3 , it will print income three times
# We can make this by for loop also,but map is quite more efficient...