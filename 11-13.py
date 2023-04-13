myStr = '파이썬은 재미 있어요. 파이썬만 매일매일 공부하고 싶어요. ^^'
strPosList = []
index = 0

while True:
    index = myStr.index('파이썬', index)
    strPosList.append(index)
    index += 1


print('파이썬 글자 위치 -->', strPosList)

# 11-14.py 에서 예외처리를 추가하여 정상출력 가능 (현재 이파일은 오류 뜸)
