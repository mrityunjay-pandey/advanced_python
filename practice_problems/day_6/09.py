class ReverseRangeIterator:
    def __init__(self, start, end):
        self.current = end - 1
        self.start = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.start:
            raise StopIteration
        else:
            result = self.current
            self.current -= 1
            return result

# Example usage
if __name__ == "__main__":
    iterator = ReverseRangeIterator(1, 6)
    for num in iterator:
        print(num)
