# #sort方法的使用
##求names里面的age的和
# names = [{'name':'zhangsan','age':26,'score':100,'height':180},
#         {'name':'zhangsan','age':16,'score':100,'height':180},
#         {'name':'zhangsan','age':21,'score':100,'height':180},
#         {'name':'zhangsan','age':20,'score':100,'height':180},
#
# ]
# print(type(names))
#
# def foo(ele):
#     return ele['age']
#
# names.sort(key=foo)
# print(names)

# #reduce的使用
# from functools import reduce
# #用reduce求一个列表数字的和
# score=[98,100,78,65,40]
# t=reduce(lambda ele1,ele2:ele1+ele2,score)
# print(t)

from functools import reduce
#求names里面的age的和
names = [{'name':'zhangsan','age':26,'score':100,'height':180},
        {'name':'zhangsan','age':16,'score':100,'height':180},
        {'name':'zhangsan','age':21,'score':100,'height':180},
        {'name':'zhangsan','age':20,'score':100,'height':180},

]
# #方法一：
# def foo(ele):
#     return ele['age']
# i=[]
# for x in names:
#     i.append(x['age'])
# print(i)
# print(reduce(lambda x, y: x + y, i))
#方法二
def add(x,y):
    return x+y['age']
print(reduce(add, names, 0))
#可以简化为
print(reduce(lambda x,y:x+y['age'],names,0))
import this

