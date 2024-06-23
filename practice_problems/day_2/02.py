x = (1,2,3,4)
# y = (1,2,3,4)
# my_dict = dict.fromkeys(x,y)
def func1 (a,b,c,d):
    a , b , c, d = a, b, c, d
    print(a,b,c,d)
func1(*x)
