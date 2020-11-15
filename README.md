# abstraction

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


##models.py:
##models.py:

from abstraction.models import Object

class Color (Object): pass

class Blue (Color): pass
class Red (Color): pass
class Green (Color): pass

class A (Object): pass
class B (A): pass
class C (B): pass

def foo():
    if not bar:
        return True
        
