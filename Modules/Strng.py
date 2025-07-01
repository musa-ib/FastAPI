def LargestString(s:str,size:int) ->int:
    max, index =0,0
    for i in range(size):
        curLen = 0
        f = 0
        for j in range(i,size):
            for k in range(i,j):
                if s[k]==s[j]:
                    f=1
                    break
            if f==1:
                break
            else:
                curLen+=1
        if max<curLen:
            max = curLen
            index = i
    return max, index

# s = "aabbabcdaabbcd"
# l = len(s)

# length,index = LargestString(s,l)

# # for i in range(index,length+index):
# #     print(s[i])
# print(s[index:index+length])


