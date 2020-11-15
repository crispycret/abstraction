




class Object(object):
  
  next_id = 0
  last_id = 0
  objects = []
  
  def __init__(self):
      cls = self.__class__
    
      if ('objects' not in cls.__dict__.keys()):
          setattr(cls, 'objects', [])
          
      if ('next_id' not in cls.__dict__.keys()):
          setattr(cls, 'next_id', 0)
      
      cls.__addnew__(self)
      
  @classmethod
  def __addnew__(cls, obj):
      obj.id = cls.next_id
      cls.objects.append(obj)
      
      cls.last_id = cls.next_id
      cls.next_id += 1
      
      for base_cls in cls.__bases__:
          func = getattr(base_cls, '__addnew__', None)
          if callable(func):
              base_cls.__addnew__(obj)
  
  
  def __repr__(self):
    return '<%s>' % self.__class__.__name__
            
        




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
            








