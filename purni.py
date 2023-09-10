class Person:
    def __init__(self,name,sex,professional):
        self.name=name
        self.sex=sex
        self.professional=professional

    def show(self):
        print('name:',self.name,'sex:',self.sex,'professional:',self.professional)
    def work(self):
        print(self.name,'working as a',self.professional)

purni=Person('purni','Female',"Student")

purni.show()
purni.work()
            
