# abstraction

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


The `Object()` class can be used to create models that will keep a reference to every instance it has created.
The `Object()` class will have every instance stored in its list.
Subclasses of `Object()` will have their own list of instances.
Subclasses of subclasses will have their own list of instance but the parent class will also have reference to the instance. 

### tests/Object_example1.py
    from abstraction.models import Object

    class Color (Object): pass

    class Blue (Color): pass
    class Red (Color): pass
    class Green (Color): pass

    class A (Object): pass
    class B (A): pass
    class C (B): pass
    
    print ()
    print ("Color:", Color.objects)
    print ("Blue:", Blue.objects)
    print ("Red:", Red.objects)
    print ("Green:", Green.objects)
    
    print ()
    print ("A:", A.objects)
    print ("B:", B.objects)
    print ("C:", C.objects)
    
    
### Output

    Blue: [<Blue>]
    Red: [<Red>]
    Green: [<Green>]
    Color: [<Color>, <Blue>, <Red>, <Green>]

    C: [<C>]
    B: [<B>, <C>]
    A: [<A>, <B>, <C>]

    Object: [<Color>, <Blue>, <Red>, <Green>, <A>, <B>, <C>]

    Object: [<Color>, <Blue>, <Red>, <Green>, <A>, <B>, <C>, <Object>, <Object>, <Object>, <Color>, <B>]
        
