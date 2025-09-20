def sort3(num1,num2,num3):
    a=[]
    a.append(num1)
    a.append(num2)
    a.append(num3)
    a.sort()
    return a[0],a[1],a[2]
print("세 수를 입력하세요 :")
num1=int(input())
num2=int(input())
num3=int(input())
num1,num2,num3=sort3(num1,num2,num3)
print("정렬된 리스트는 다음과 같습니다: {0} {1} {2}".format(num1,num2,num3))
