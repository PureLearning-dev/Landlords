

def  inherit_docstring(cls: type):
    """子类如果没有写属性的 __doc__，则直接继承父类对应属性的 __doc__"""
    parents = cls.__mro__[1:]

    for parent in parents:
        for name, method in parent.__dict__.items():

            # 如果子类函数中没有 doc，继承父类的
            if name in cls.__dict__ and not cls.__dict__[name].__doc__:
                # 不用使用默认返回，因为在类中，没有 __doc__ 就是 Node
                cls.__dict__[name].__doc__ = getattr(parent, name).__doc__

    return cls



