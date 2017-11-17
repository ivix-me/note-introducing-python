装饰器

其本质是个函数

```python
def 装饰器(要调用的函数)
    def 内联函数(*args, **kargs)
        包装语句
        result = 要调用的函数(*args, **kargs)
        包装语句
        return result
    return 内联函数
    

@装饰器
def foo():
    pass
```