

def inherit_docstring(cls: type):
    """子类如果没有写属性的 __doc__，则直接继承父类对应属性的 __doc__"""
    for parent in cls.__mro__[1:]:
        for name, attr in cls.__dict__.items():
            # 子类已经自己写了 __doc__，不覆盖
            if getattr(attr, '__doc__', '') != '':
                continue
            parent_attr = getattr(parent, name, None)
            if parent_attr is not None:
                parent_doc = getattr(parent_attr, '__doc__', None)
                if parent_doc:
                    try:
                        attr.__doc__ = parent_doc
                    except AttributeError:
                        pass  # 内置类型（str/int 等）的 __doc__ 不可写，跳过
    return cls