def my_sort(*nums):
    numlist=[int(n) for n in nums]
    print("입력된 정수의 리스트: ",numlist)
    numlist.sort()
    print("정렬된 정수의 리스트: ",numlist)
    return
inputStr=input('쉼표로 구분된 정수를 여러 개 입력하시오: ')
inputlist=inputStr.split(',')
my_sort(*inputlist)

