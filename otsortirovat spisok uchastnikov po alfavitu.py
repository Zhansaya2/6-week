fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
studs = []
for stud in fin.readlines():
    if list(stud.split()):
        studs.append([list(stud.split())[0], list(stud.split())[1],
                      list(stud.split())[3], ])

studs.sort()

for student in studs:
    student = [student[0], student[1], student[-1]]
    print(*student, file=fout)
fout.close()
