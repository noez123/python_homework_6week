inFp, outFp = None, None
inStr = ''


inFp = open("C:/Windows/win.ini", 'rt', encoding='UTF8')
outFp = open("datal.txt", 'wt', encoding='UTF8')

inList = inFp.readlines()

for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('-----파일이 정상적으로 복사되었음-----')