greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"
greet_format = "Hello {}"
name = "Daniel"
intrupution = f"Hello {name}"
formatted = greet_format.format(name)

#print(intrupution)
#print(formatted)
#print(formatted.upper())
#print(formatted.lower())
#print(formatted.replace("Daniel", "Candace"))
#print(greet, formatted)
#print(greet, formatted.replace("Daniel", "Candace"))
#print(extened_grt)

hello = "testing"
world = "this"
number = "because"
thanks = "why"
goodbye = "not"
salary = "77000"

hi = f"{hello} {world}"
print(hi)

hstring = "{} {} {} {} {}".format(hello, world, number, thanks, goodbye)
print(hstring)

fsalary = f"{name}'s ${salary:.2f}"
print(fsalary)

