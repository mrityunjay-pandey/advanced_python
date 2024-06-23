count = 0
def increment():
    count = 10
    print(f"Inside the function, local count: {count}")

print(f"Global count before calling function: {count}")
increment()
print(f"Global count after calling function: {count}")