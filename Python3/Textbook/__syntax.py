"""
扩展方法 重载
Python 中还分类型扩展方法和仅当前对象扩展方法，顺便还可以给扩展方法改个名
类型扩展方法：
    setattr(class, 'class_method', new_method)
对象扩展方法：
    import types
    object.class_method = types.MethodType(new_method, object)
如果 class_method 原来不存在，new_method 是 extension_method，
否则就是 override_method，但却没有继承关系。
"""
"""
type() 与 isinstance() 的区别：  
共同点：两者都可以判断对象类型  
不同点：isinstance 可以判断继承的子类，而 type 不行。
"""
"""
class A:
    root = 0
    def __init__(self):
        self.root = 1
root 和 self.root 不是一个变量。
查找顺序： 子类实例变量 >> 子类类型变量 >> 父类/超类(super class)实例变量 >> 父类类型变量
"""

a=set([1, 2, 3])
print(a[0])
