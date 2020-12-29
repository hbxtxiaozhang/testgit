# 例如玩游戏这段代码，本来已经写好了，先在需要加个时间限制，晚上10点之后不让玩游戏

# 定义一个装饰器，通过装饰器来实现功能的增加
def can_play(fn):
    def inner(x, y, *args, **kwargs):

        # if args[0] <= 22:
        #     fn(x,y)
        # else:
        #     print('晚上十点之后不能玩游戏！')
        # clock=kwargs['clock']  #直接取值当传入的参数没有关键字为clock的时，程序会崩溃，而用字典的get()方法取kwargs的值，没传入指定参数不会崩溃
        clock=kwargs.get('clock',23)
        if clock <= 22:
            fn(x, y)
        else:
            print('现在{}点了，不能玩游戏了'.format(clock))
    return inner


@can_play
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))


# #调用试试
play_game('张三', '王者荣耀',23)
play_game('李四', '吃鸡', clock=22)

# 开放封闭原则：对于已经写好了的代码尽量不要去动，而是通过其他办法去实现需求的更改
