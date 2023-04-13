inFp = None
inStr = ""

inFp = open("datal.txt", 'rt', encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr == '':
        break;
    print(inStr, end='')

inFp.close()
