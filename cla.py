class MyClass(object):
    class_name = "MyClass"    '''类属性，三种方法都能调用'''
    def __init__(self):
        self.instance_name = "instance_name"   '''实例属性，只能被实例方法调用'''
        self.class_name = "instance_class_name"
    def get_class_name_instancemethod(self):
        '''实例方法，只能通过实例调用'''
        return MyClass.class_name
    @classmethod
    def get_class_name_classmethod(cls):
        '''类方法，可通过类名.方法名直接调用
        类方法可以访问属性，不能访问属性实例'''
        return MyClass.class_name
    @staticmethod
    def get_class_name_staticmethod():
        '''静态方法，可通过类名.方法名直接调用
        静态方法可以访问类属性，不能访问实例属性'''
        return MyClass.class_name
    def instance_visit_class_attribute(self):
        '''实例属性与类属性重名时，self.class_name优先访问实例属性'''
        print("实例属性与类属性重名时，优先访问实例属性")
        print("self.class_name:",self.class_name)
        print("MyClass.name: ",MyClass.class_name)
if __name__=='__main__':
    MyClass.class_name = "MyClassNew"
    instance_class = MyClass()
    print("instance method: ",instance_class.get_class_name_classmethod())
    print("class method: ",MyClass.get_class_name_classmethod())
    print("static method: ",MyClass.get_class_name_staticmethod())
    instance_class.instance_visit_class_attribute()