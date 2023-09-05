def greetHello(name, ending):
    print("Hello " + name)
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

def letterGenerator(name, date):
    st = f"Hi mam,\n This is {name} and I will not come to work on {date}"
    print(st)

def average(a, b):
    return(a+b)/2

print("Executing Function")
# greetHello()
greetHello("Ashish", "Thank you")
greetHello("Raj", "Thanks")

letterGenerator("Ashish", "26th March 2024")
letterGenerator("Sandeep", "30th March 2024")

print(average(34, 25))
print("Done")
