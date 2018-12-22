#!/usr/bin/python3
# -- coding: utf-8 -- 
suspects=['A','B','C','D']#嫌疑人
def who_is_thief(suspects,n):
    print("此次问题共有",n,"人说的为真")
    for thief in suspects:
        print("如果"+thief+"是小偷")
        if thief!='A':
            print("A所说为真")
        else:
            print("A所说为假")
        if thief=='D':
            print("B所说为真")
        else:
            print("B所说为假")
        if thief=='B':
            print("C所说为真")
        else:
            print("C所说为假")
        if thief!='D':
            print("D所说为真")
        else:
            print("D所说为假")
        A=(thief!='A')
        B=(thief=='D')
        C=(thief=='B')
        D=(thief!='D')
        if(A+B+C+D==n):
            print("小偷是"+thief+"\n\n")
            break
        else:
            print("假设错误\n\n")
who_is_thief(suspects,1)
who_is_thief(suspects,3)
