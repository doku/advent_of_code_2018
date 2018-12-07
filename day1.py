



with open("day1.input") as f:
    data = f.read()


res = 0
aList = []
for d in data.split("\n"):
    if len(d) > 1:
        aList.append(int(d))
        if d[0] == "+":
            res += int(d[1:])
            #print(" + " + d[1:])
        else:
            res -= int(d[1:])
print("result is " + str(res))

#print(aList)
print(sum(aList))
# 442

#print(aList)
#aList = [+1, -1]
#aList = [+3, +3, +4, -2, -4]
#aList = [-6, +3, +8, +5, -6]
#aList = [+7, +7, -2, -7, -4]

memo = {0}
iLen = len(aList)
i = 0
prev, freq = 0, 0
while True:
    if i >= iLen:
        i = 0
        print(" ... " + str(freq))
    freq = (freq + aList[i])
    if freq in memo:
        print("freq: " + str(freq))
        break
    else:
        memo.add(freq)
    i += 1

  
print( str(freq in memo))
  


