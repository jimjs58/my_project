#!/usr/bin/env python 
# -*- coding:utf-8 -*-
user_infos={
    "王":{
        "work":"sicience",
        "salary":3000,
        "level":1
    },
    "周":{
        "work":"market",
        "salary":5000,
        "level":2
    },
    "林":{
        "work":"market",
        "salary":7000,
        "level":3
    },
    "张":{
        "work":"sicience",
        "salary":4000,
        "level":1
    },
    "刘":{
        "work":"market",
        "salary":6000,
        "level":2
    },
}
print(f"原始列表为{user_infos}")
for user_name in user_infos:
    if user_infos[user_name]["level"]==1:
        #解法二 直接写，不加临时变量引用
       # user_infos[user_name]["level"]+=1
       # user_infos[user_name]["salary"]=user_infos[user_name]["salary"]+1000

        a = user_infos[user_name]
        #注意： 如果按如下两行来写，则最后输出的列表中level不会改变，因为临时变量的赋值
        #b=a["level"]
        #b+=1

        a["level"]+=1
        a["salary"]=user_infos[user_name]["salary"]+1000
print(f'改变后的列表为{user_infos}')

def sum(sums):
    result=sums(2,3)
    print(f"结果是{result}")
sum(lambda x,y:x+y)
