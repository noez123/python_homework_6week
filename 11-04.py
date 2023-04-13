inFp = None
inList, inStr = [], ""

inFp = open("datal.txt", 'rt', encoding='UTF8')

inList = inFp.readlines()

for inStr in inList:
    print(inStr, end="")

inFp.close()
