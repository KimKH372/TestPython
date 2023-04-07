hap, i = 0,0

for i in range(3333, 10000) :
    if i % 1234 == 0 :
        continue
    hap += i
    if hap > 100000 :
        hap = hap - i
        break

print("3,333~9,999의 합계(1,234의 배수 제외) : %d" % hap)
