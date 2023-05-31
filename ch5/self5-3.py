inFp = None	# 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("ch5/text/test.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")
num= 1
while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print("%d, %ss" % (num,inStr), end= "")

inFp.close()
