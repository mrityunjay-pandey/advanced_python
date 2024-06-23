class Sentence:
    def __init__(self,text):
        self.text = text

    def __add__(self,other):
        t = self.text + other.text
        return t
t1 = Sentence("Sumedha ek mehnati employee hai.")
t2 = Sentence("vo subah office me sabse pahle aati hai aur sabse baad me jati hai.")
t3 = t1 + t2
print(t3)