class Device:
    def operate(self):
        print("Operating device")
class Phone(Device):
    def make_call(self):
        print("Making call...")
class Tablet(Device):
    def browse(self):
        print("Browsing now....")
class Smartphones(Phone,Tablet):
    pass

obj = Smartphones()
obj.operate()
obj.make_call()
obj.browse()