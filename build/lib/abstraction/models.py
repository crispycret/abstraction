
       
class ObjectManager(list):
    pass

class Object(object):
    
    last_id = 0
    objects = ObjectManager()
    
    @staticmethod
    def __add_new__ (obj): 
        Object.objects.append(obj)
        obj.id = Object.last_id        
        Object.last_id += 1   
        
    def __init__(self): 
        Object.__add_new__(self)




### An object that can describe anything. 
### It accepts any parameter to initialize,
### including type, a variable that can be used to better describe this object
class AbstractObject(dict):
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
            
    def __str__(self):
        string = "<" + self.type + ': '
        for variable, value in self.__dict__.items():
            string += variable + "=" + str(value) + ", "
        return string + ">"
            
