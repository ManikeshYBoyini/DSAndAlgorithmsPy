list_1 = [1,2,3,4,5,6]
list_2 = [2,3,4,5,6,7,8,9]

set_1 =set(list_1)
set_2 = set(list_2)
answer_1 = set_1.difference(set_2)
answer_2 =set_1.symmetric_difference(set_2)

answer_1=sorted(set(answer_1))
answer_2=sorted(set(answer_2))

print(answer_1)
print(answer_2)