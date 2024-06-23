class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        print(f"{Counter.count} objects have been created now.")
        # show_details()
    # def new_counter(self):
    #     print(f"{Counter.count} objects have been created now.")

p1 = Counter()
# p1.new_counter()
p2 = Counter()
# p2.new_counter()
