#program for finding the percentage:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    n=0
    sum=0
    for i in student_marks[query_name]:
        n+=1 
        sum=sum+i
    sum=sum/n
    num="{:.2f}".format(sum)
    print(num)
