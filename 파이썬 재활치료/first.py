#print("Hello, World!")

#a,b=map(int,input().split())
#print(a+b)
'''
a=int(input())
b=int(input())
print(a+b)'''

'''
a=int(input())
b=int(input())
first=a*(b%10)
second=a*((b//10)%10)
third=a*(b//100)
print(first)
print(second)
print(third)
print(a*b)'''

'''3042
a,b=map(int,input().split())
print(2*b-a)'''

'''2163
a,b=map(int,input().split())
print(a*b-1)'''

'''2525
hours,minutes=map(int,input().split())
input_minutes=int(input())
if input_minutes>=60:
    hours+=input_minutes//60
    minutes+=input_minutes%60
    if minutes>=60:
        hours+=1
        minutes-=60
    if hours>=24:
        hours-=24
else:
    minutes+=input_minutes
    if minutes>=60:
        hours+=1
        minutes-=60
    if hours>=24:
        hours-=24
print(hours, minutes)'''

'''2530
hour, minute, second = map(int, input().split())
input_second = int(input())

total_second = hour * 3600 + minute * 60 + second

total_second += input_second

final_hour = (total_second // 3600) % 24
final_minute = (total_second % 3600) // 60
final_second = total_second % 60

print(final_hour, final_minute, final_second)'''

'''2914
a,b=map(int,input().split())
print(a*(b-1)+1)'''


rows, cols = 3, 4
arr = [[0 for _ in range(cols)] for _ in range(rows)]
a=int(input())
for i in range(a):
    a[i][0],a[i][1],a[i][2],a[i][3]=map(int,input().split())
print(arr)