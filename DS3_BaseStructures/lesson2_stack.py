'''
    什么是栈？ 一个项的有序集合。添加和移除项都发生在同一'端'，这一端叫做'顶'，另一端叫做'底'
    后进先出：栈的'底'是有标志性的，因为存储在栈中更靠近'底'的项就是栈中存储时间最长的项。最新添加的项和移出项时也会第一个被移除
             这种排序的原则叫做'LIOF'法，也就是'后进先出'
    栈的抽象数据类型:
        Stack()  创建一个新的空栈，不需要参数，返回一个空栈
        push(item) 入栈     将新项添加到堆栈的顶部。它需要参数item并且没有返回值
        pop() 出栈     从栈项删除项目，不需要参数，返回呗删除的项，栈被修改
        peek()    返回栈顶的顶，不删除它，不需要参数，堆栈不被修改
        isEmpty()   测试栈是否为空，不需要参数，返回布尔值
        size()   返回栈的项目数，不需要参数，返回一个整数
'''

l = []
l.append(4)
l.append('aa')
l.append('bb')
l.pop()
print(l)