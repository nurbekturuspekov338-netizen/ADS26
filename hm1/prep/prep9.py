import sys

sys.setrecursionlimit(200000)

def merge_sort(students):
    if len(students)<=1:
        return students
    
    mid=len(students)//2
    left=merge_sort(students[:mid])
    right=merge_sort(students[mid:])
    
    sorted_list=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i][1]<=right[j][1]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
            
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def main():
    data=sys.stdin.read().split()
    if not data:
        return
    
    n=int(data[0])
    students=[]
    
    idx=1
    for i in range(n):
        name=data[idx]
        grade=int(data[idx+1])
        students.append((name, grade)) 
        idx+=2
    sorted_students=merge_sort(students)
    output=[student[0] for student in sorted_students]
    sys.stdout.write('\n'.join(output)+'\n')
    
if __name__=="__main__":
    main()       