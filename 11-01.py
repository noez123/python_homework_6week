inFp = None
inStr = ""

inFp = open("datal.txt", 'rt', encoding='UTF8')

inStr = inFp.readline()
print(inStr, end='')

inStr = inFp.readline()
print(inStr, end='')

inStr = inFp.readline()
print(inStr, end='')

inFp.close()
