#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    fibValues = {1:1,2:1}
    count = 1
    while count <= n:
        if count not in fibValues:
            fibValues[count] = fibValues[count-1] + fibValues[count -2]
        count += 1
    return fibValues[n]

def getPrev():
    value = [0,5,1,8,4,6,3,2,4]
    time = [(0,0), (1,4),(3,5),(0,6),(4,7),(3,8),(5,9),(6,10),(8,11)]
    prev = [0 for _ in range(len(value))]

    for n in range(2, len(value)):
        count = n - 1
        while count >= 1:
            if time[n][0] >= time[count][1]:
                prev[n] = count
                break
            count -= 1
    dp = [[0,[]]for _ in range(len(value))]

    for i in range(1, len(value)):
        # 同时确定是哪几个任务
        dp[i] = dp[i-1] if dp[i-1][0] > (value[i]+ dp[prev[i]][0]) else (value[i]+ dp[prev[i]][0], dp[prev[i]][1]+[i])
        
    return dp[-1]

def rec_opt(arr, i):
    """
    数据[1,2,4,1,7,8,3]
    条件：
        1. 选择对应的不相邻的数据
        2. 确保选出的数最大
    """
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0],arr[1])
    else:
        A = rec_opt(arr,i-2) + arr[i]
        B = rec_opt(arr,i-1)
        return max(A,B)
    
def dp_opt(arr):
    opt = [0 for _ in range(len(arr))]

    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[-1]

"""
arr = [3, 34, 4, 12, 5, 2]
S = 9
从arr中选出指定的数等于S的值
有则返回Tue
否则返回False
"""
def rec_sub(arr, i, s):
    """
    两种情况：选，不选
    选：rec_sub(arr,i-1,s - arr[i])
    不选：rec_sub(arr, i-1,s)

    终止条件：
        1. s找到了 s== 0
        2. arr[0] == s
        3. arr[i] > s: arr[i] 不可选,rec_sub(arr,i-1,s) 选
    """
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_sub(arr, i-1, s)
    else:
        return rec_sub(arr,i-1,s-arr[i]) or rec_sub(arr,i-1,s)


arr_dict = {}
def sub_que(arr, s):
    """
    两种情况：选，不选
    选：rec_sub(arr,i-1,s - arr[i])
    不选：rec_sub(arr, i-1,s)

    终止条件：
        1. s找到了 s== 0
        2. arr[0] == s
        3. arr[i] > s: arr[i] 不可选,rec_sub(arr,i-1,s) 选
    """
    queue = [(0,s)]
    len_arr = len(arr)
    
    while queue:
        node = queue.pop(0)
        if arr[node[0]] == node[1]:
            return True
        # chosed
        if node[0] + 1 < len_arr:
            if arr[node[0]] < node[1]:
                queue.append((node[0]+1, node[1] - arr[node[0]]))
            # not chose
            queue.append((node[0]+1, node[1]))
    return False
    
def dp_sub(arr, S):
    sub = [[False for _ in range(S+1)] for _ in range(len(arr))]
    for i in range(1, len(arr)):
        for s in range(1,S+1):
            if arr[i] > s:
                sub[i][s] = sub[i-1][s]
            else:
                A = sub[i-1][s-arr[i]]
                B = sub[i-1][s]
                sub[i][s] = A or B
    return sub[-1][-1]
    
if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    s = 34000
    print(dp_sub(arr, s))
