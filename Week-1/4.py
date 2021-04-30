# def sec_low(stud):
#     grades=[]
#     for j in stud:
#         grades.append(j[1])
    # sort_grades=sorted(grades)
    # seclow_grade = sort_grades[0]
    # for grade in sort_grades:
    #     if(grade!=seclow_grade):
    #         seclow_grade=grades
    #         break
    # seclow_stud=[]
    # for j in stud:
    #     if j[1] == seclow_grade:
    #         seclow_stud.append(j[0])
    # for name in sorted(seclow_stud):
    #     print(name)



# stud = []
# n=int(input())
# for i in range(n):
#     stud_data=[input(),float(input())]
#     stud.append(stud_data)
# sec_low(stud)


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









