from collections import namedtuple


''' Simplified Solution '''
total_students, Student = int(input()), namedtuple('Student', list(str(input()).split('\t')))
print('{:.2f}'.format(sum([int(Student(*input().split()).MARKS) for _ in range(total_students)]) / total_students))


''' Descriptive Solution '''
# total_students = int(input())           
# cols = list(input().split('\t'))        
# Student = namedtuple('Student', cols)   
# marks = 0
# for _ in range(total_students):
#     marks += int(Student(*input().split('\t')).MARKS)
# print('{:.2f}'.format(marks / total_students))
