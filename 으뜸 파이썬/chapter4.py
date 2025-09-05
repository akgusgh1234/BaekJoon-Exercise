#4.1
def my_greet():
    print("환영합니다.")
    print("환영합니다.")
my_greet()

#4.2
def square(x):
    return x * x
print('3의 제곱은 : ', square(3))
print('4의 제곱은 : ', square(4))

#4.3
def max2(x, y):
    if x > y:
        return x
    else:
        return y
def min2(x, y):
    if x < y:
        return x
    else:
        return y
print('100과 200 중 큰 수는 : ', max2(100, 200))
print('100과 200 중 작은 수는 : ', min2(100, 200))

#4.4
def mile2km(mile):
    return mile * 1.61
for i in range(1, 6):
    print(i,'마일 = ',i*1.61,'킬로미터')

#4.5
def inch2cm(inch):
    return inch * 2.54
for i in range(1, 6):
    print(i,'인치 = ',i*2.54,'센티미터')

#4.6
def cel2fah(cel):
    return cel * 9 / 5 + 32
for i in range(10,60,10):
    print('섭씨 ',i,'도 = 화씨 ',cel2fah(i),'도')
'''
#4.7
a,b,c=map(int,input('세 수를 입력하세요: ').split())
def max3(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
def avg3(x,y,z):
    return (x+y+z)/3
def min3(x,y,z):
    if x<=y and x<=z:
        return x
    elif y<=x and y<=z:
        return y
    else:
        return z
print(a, b, c,'의 평균값은 ',avg3(a,b,c))
print(a, b, c,'의 최대값은 ',max3(a,b,c))
print(a, b, c,'의 최소값은 ',min3(a,b,c))

#4.8
a,b,c,d,e,f=map(int,input('여섯 수를 입력하세요: ').split())
def max6(x1,x2,x3,x4,x5,x6):
    abc=max3(x1,x2,x3)
    de=max3(x4,x5,x6)
    if abc>=de:
        return abc
    else:
        return de
def min6(x1,x2,x3,x4,x5,x6):
    abc=min3(x1,x2,x3)
    de=min3(x4,x5,x6)
    if abc<=de:
        return abc
    else:
        return de
def avg6(x1,x2,x3,x4,x5,x6):
    abc=avg3(x1,x2,x3)
    de=avg3(x4,x5,x6)
    return (abc*3+de*3)/6
print('평균값은',avg6(a,b,c,d,e,f))
print('최대값은',max6(a,b,c,d,e,f))
print('최소값은',min6(a,b,c,d,e,f))

#4.9
nums = list(map(int, input('정수를 여러 개 입력하시오 : ').split()))
def max_in_list(num_list):
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value
def min_in_list(num_list):
    min_value = num_list[0]
    for num in num_list:
        if num < min_value:
            min_value = num
    return min_value
def avg_in_list(num_list):
    return sum(num_list) / len(num_list)
print('평균값은 {0:.1f}'.format(avg_in_list(nums)))
print('최대값은', max_in_list(nums))
print('최소값은', min_in_list(nums))
'''
#4.10
x1=int(input('x1 좌표를 입력하세요: '))
y1=int(input('y1 좌표를 입력하세요: '))
x2=int(input('x2 좌표를 입력하세요: '))
y2=int(input('y2 좌표를 입력하세요: '))
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
print('두 점의 거리: {0:.1f}'.format(distance(x1,y1,x2,y2)))
