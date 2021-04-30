n=int(input())
stud=[]
grades=[]
for i in range(n):

    stud_data=[input(),float(input())]
    stud.append(stud_data)
 
for j in stud:
    grades.append(j[1])
sort_grades=sorted(grades)

sec_grade=sort_grades[1]
sec_stud =[]
for j in stud:
    if(j[1]==sec_grade):
        sec_stud.append(j[0])

for name in sec_stud:
    print(name)









