x1=int(input('x1 좌표를 입력하세요: '))
y1=int(input('y1 좌표를 입력하세요: '))
x2=int(input('x2 좌표를 입력하세요: '))
y2=int(input('y2 좌표를 입력하세요: '))
def area(x1,y1,x2,y2):
    width=abs(x2-x1)
    height=abs(y2-y1)
    return width*height
print('직각삼각형의 면적은 : ',area(x1,y1,x2,y2)/2)