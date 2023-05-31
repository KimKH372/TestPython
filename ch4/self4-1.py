aa = []
for i in range(0, 10) :
    aa.append(0)
hap = 0
avg = 0

i = 0
while True:
    if i < 10:
        aa[i] = int(input(str(i+1) + "번째 숫자 : " ))
        i = i+1
    else :
        break

hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] + aa[9]
avg = (aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] + aa[9])/10

print("합계 ==> %d" % hap)
print("평균 ==> %d" % avg)
