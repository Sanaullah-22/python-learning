# Wrong Code
def print_salary():
    print("Salary is:", salary)
    salary = 50000
    return salary

print_salary()
# This One through error

# correct one
def print_salary():
    salary = 50000
    return salary
result=print_salary()
print("Salary Is:",result)
