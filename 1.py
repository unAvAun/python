# 在控制台中输出“hello，world“
# print("hello world")
# print("hello python")
# num = 1
# print(num)
# num = num+1
# print(num)
# num = True
# print(num)
# a, b = 1, 2
# print(a)
# print(b)
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
# a = 1
# b = 2
# c = 3
# a, b, c = c, a, b
# print(a, b, c)
# print(type(2))
# print(type(3.0))
# print(type(True))
# print(type("hello"))
# print(type(None))
# a = 1
# print(type(a))
# a = 1
# print(isinstance(a, int))
# s1 = "hello"
# s2 = """
# 你好
# 世界
# """
# print(s2)
# s1="1""2""3"
# print(s1)
# s2="4"
# print(s1+s2)
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python、Java"
# print("大家好,我是"+name+",今年"+str(age)+",学习的专业是"+pro+",爱好"+hobby)
# s1="涛哥"
# print("大家好,我是%s"%s1)
# s1="人生苦短"
# s2="我用python"
# print("吉多.范罗苏姆,%s,%s"%(s1,s2))
# name="涛哥"
# print(f"大家好,我是{name}")
# age=18
# print(f"大家好,我是{name},今年{age}")
# name =input("请输入您的名字:")
# age=input("您的年龄:")
# print(f"您的名字{name},年龄为{age}")
# total=10000
# password=input("请输入您的银行卡密码:")
# print(f"密码正确,{password}")
# num=input("请输入您的取款金额:")
# print(f"取款后银行卡的余额为:{total-int(num)}")
# s1=input("请输入第一个数字:")
# s2=input("请输入第二个数字:")
# print(f"{s1}+{s2}={int(s1)+int(s2)}")
# print("10+4=",10+4)
# print("10-4=",10-4)
# print("10*4=",10*4)
# print("10/4=",10/4)
# print("10//4=",10//4)#整除
# print("10%4=",10%4)#取余
# print("10**4=",10**4)#幂指数
# 算术运算符的优先级-->** -->* / // % -->+ -
# a=input("请输入第一个数:")
# b=input("请输入第二个数:")
# print(F"a+b={int(a)+int(b)},a-b={int(a)-int(b)}")
# a=float(input("请输入第一个数:"))
# b=float(input("请输入第二个数:"))
# print(F"a+b={a+b},a-b={a-b}")
# a=float(input("请输入第一个数:"))
# b=float(input("请输入第二个数:"))
# c=float(input("请输入第三个数:"))
# average=(a+b+c)/3
# print(f"a+b+c的平均数为:{average}")
# a=float(input("请输入梯形的上底:"))
# b=float(input("请输入梯形的下底:"))
# h=float(input("请输入梯形的高:"))
# s=(a+b)*h/2
# print(f"梯形的面积为:{s}")
# a=int(input("请输入一个数:"))
# print(f"该数在 10-20 之间吗:{a>10 and a<20}")
# print(f"该数不在 10-20 之间吗:{a<10 or a>20}")
# score=100
# if score>680:
#     print("欢迎你来清华读书")
#     print("恭喜你即将踏入精彩的大学生活")
# print("------")

# account = int(input("请输入账号"))
# password = int(input("请输入密码"))
# if account == 188888 and password == 1234:
#     print("登录成功")
# else:
#     print("账号或密码错误")

# year = int(input("2000请输入年份"))
# if year % 100 != 0 and year % 4 == 0:
#     print("闰年")
# elif year % 100 == 0 and year % 400 == 0:
#     print("闰年")
# else:
#     print("平年")

# day=input("请输入星期几(1-7):")
# match day:
#     case "1":
#         print("周一上班")
#     case "2":
#         print("周二上班")
#     case "3":
#         print("周三上班")
#     case "4":
#         print("周四上班")
#     case "5":
#         print("周五上班")
#     case "6"|"7":
#         print("周末休息")
#     case _:
#         print("输入错误")

# oc=input("请输入指令:")
# match oc:
#     case "上"|"w"|"W":
#         print("向上")
#     case "下"|"s"|"S":
#         print("向下")
#     case "左"|"a"|"A":
#         print("向左")
#     case "右"|"d"|"D":
#         print("向右")
#     case "跳"|"/"|" ":
#         print("跳跃")
#     case "攻击"|"j"|"J":
#         print("攻击")
#     case "退出"|"esc"|"ESC":
#         print("退出")
#     case _:
#         print("输入错误")

# i=1
# s=0
# while i<=100:
#     if i%2==0:
#         s=s+i
#     i=i+1
# print(s)

# mag=input("请输入需要遍历的字符串:")
# for i in mag:
#     print(i)
# else:
#     print("遍历完成")

# s=0
# for i in range(1,101,2):
#     s+=i
# print(s)

# s=0
# for i in range(100,501):
#     if i%3==0:
#         s+=i
# print(s)

# print()自带换行
# print(a,end="")不换行
# a=int(input("长:"))
# b=int(input("宽:"))
# # for j in range(0,b):
# #     str=""
# #     for i in range(0,a):
# #         str=str+"*"
# #     print(str)
# for j in range(b):
#     for i in range(a):
#         print("*",end="")
#     print()

# for j in range(1,10):
#     for i in range(1,10):
#         if i<=j:
#             print(i,"*",j,"=",i*j,end="\t")
#     print()

# import random
# num=random.randint(1,100)
# a=int(input("请输入数字:"))
# while a!=num:
#     if a>num:
#         print("猜大了")
#         a=int(input("请输入数字:"))
#     else:
#         print("猜小了")
#         a=int(input("请输入数字:"))
# else:
#     print("猜对了")

# s=[1,2,3,4]
# # print(s[0])#正向索引
# # print(s[-4])#负向索引

# for i in s:
#     print(i)
# del s[1] 删除

# s=[1,2,3,4]
# print(s[0:3:1])
# print(s[:3:1])
# print(s[0:3:])
# print(s[:3:])
# print(s[:3])
# s.append(5)#尾部添加元素
# print(s)
# s.insert(2,7)#在索引位置插入元素
# print(s)
# s.remove(3)#移除第一个该元素
# print(s)
# s.pop(1)#删除索引位置的元素
# print(s)
# s.sort()#按从小到大顺序排列
# print(s)
# s.reverse()#反转排序
# print(s)
# s = []
# for i in range(10):
#     num = int(input("请输入十个数字"))
#     s.append(num)
# print(s)
# s.sort()
# print(s)
# print(s[0], s[9])
# sum = 0
# for i in range(10):
#     sum = sum+s[i]
# print(sum/len(s))

# s1 = [12, 34, 23, 56, 25, 67, 89]
# s2 = [34, 35, 67, 45, 88]
# for i in s2:
#     s1.append(i)
# print(s1)
# s3=[]
# for i in s1:
#     if i not in s3:
#         s3.append(i)
# print(s3)
#解包
# s3=[*s1,*s2]
# print(s3)
#合并列表
# s3=s1+s2
# print(s3)

# num_list=[]
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
num_list2=[i**2 for i in range(1,21)]
print(num_list2)
#列表推导式
num_list=[1,2,3,4,5,6]
new_list=[i**2 for i in num_list if i%2==0]
print(new_list)