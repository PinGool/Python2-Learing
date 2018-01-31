# -*- coding: utf-8 -*-

def log(level,*args,**kwargs):

    '''
    * 无名字参数
    ** 有名字参数
    '''

    def inner(func):
        def wrapper(*args, **kwargs):
             print level,'before calling',func.__name__
             print level,'args',args, 'kwargs',kwargs
             func(*args, **kwargs)
             print level,'end calling', func.__name__
        return wrapper
    return inner


@log          #装饰器
def hello():
    print 'hello'

@log(level='INFO')
def hello2(name,age):
    print 'hello',name,age


if __name__== '__main__':
   # hello()  # = log(hello())  底层是这样东西
    hello2(name='nowcoder',age=2)