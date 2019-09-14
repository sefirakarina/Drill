# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:55:25 2018

@author: Sefira Karina
"""


data = [50,17,72,12,23,54,76,9,14,19,0,0,67]

def dfs(data,x,i):
    if i <= len(data):

        if  data[i-1] != 0:
            print("check", data[i-1])

        if data[i-1] == x:
                return i

        result = dfs(data, x, i*2) ##left side

        if result != -1:
            return result
        result = dfs(data,x, (i*2)+1)##right side

        if result != -1:
            return result

        return -1
    else:
        return -1

def bfs(data,x,i):
    if i <= len(data):
        #print ("i= ",i)
        q=[]
        temp=i
        for y in range (i):
            #print (temp)
            q.append(data[temp-1])
            if len(data)>temp:
                temp=temp+1
            #print (q)
        for y in range(i):
            print("check" , q[y])
            if q[y]==x:
                print("yay", x , "is found")
                return i
            
        print("change row")
        for y in range(i):
            q.pop()
        result = bfs(data, x, i*2) 
        if result != -1:
            return result
        return -1
    else:
        return -1
    
dfs(data,72,1)
    
#uncomment this to test bfs code
#bfs(data,54,1)