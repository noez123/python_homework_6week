inFp = None
inList = ""

inFp = open("datal.txt", 'rt', encoding='UTF8')

inList = inFp.readlines()
print(inList)

inFp.close()
