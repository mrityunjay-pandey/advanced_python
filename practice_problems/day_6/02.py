def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1())
print(counter1())


print(counter2())
print(counter2())

print(counter1())