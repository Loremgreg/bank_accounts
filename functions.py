def hello_w():
    print("Hello world!")

hello_w()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(7, 2)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave", last="Gray")


def intro(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} is {value}")

intro(FirstName="John", LastName="Doe", Age=42)