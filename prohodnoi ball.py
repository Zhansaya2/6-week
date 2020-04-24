class Text:
    bal1 = 0
    bal2 = 0
    bal3 = 0


fin = open('input.txt', 'r', encoding='utf-8')
fun = open('output.txt', 'w', encoding='utf-8')
a = fin.readlines()
k = int(a[0])
text = []
temp = []
m = 0
for n in range(1, len(a)):
    kl = Text()
    kl.bal1 = a[n].split()[int(len(a[n].split())) - 3]
    kl.bal2 = a[n].split()[int(len(a[n].split())) - 2]
    kl.bal3 = a[n].split()[int(len(a[n].split())) - 1]
    text.append(kl)

for kl in text:
    if int(kl.bal1) >= 40 and int(kl.bal2) >= 40 and int(kl.bal3) >= 40:
        c = (int(kl.bal1) + int(kl.bal2) + int(kl.bal3))
        temp.append(c)
temp.sort()
d = [0] * 301
for n in temp:
    d[n] += 1
if len(temp) == 0 or temp.count(max(temp)) > k:
    print(1, file=fun)
elif len(temp) <= k or k == 0:
    print(0, file=fun)
else:
    for n in range(len(d) - 1, 0, -1):
        if d[n] > 0 and (k - d[n]) < 0:
            break
        else:
            if d[n] > 0 and (k - d[n]) >= 0:
                k -= d[n]
                m = n
    print(m, file=fun)
fin.close()
fun.close()
