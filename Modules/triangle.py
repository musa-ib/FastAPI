def WordValue(word:str)->int:
    sum = 0
    for i in word:
        sum += ord(i)-ord('A')+1
    return sum

def TrangleNumber(s:int)->bool:
    i = 1
    n = 1
    while(n<=s):
        if n == s:
            return True
        n = i*(i+1)//2
        i += 1
    return False

#
def readfile(path:str)->int:
    file = open(path,'r')
    content = file.read()
    words = (content.split('"'))
    count = 0
    e = ','
    for e in words:
        words.remove(e)
    for i in words:
        if TrangleNumber(WordValue(i)):
            count += 1
    return count