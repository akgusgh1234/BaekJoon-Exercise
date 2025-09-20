width=int(input('밑변을 입력하세요: '))
height=int(input('높이를 입력하세요: '))
def cal_area(width,height):
    return width*height/2
print('삼각형의 면적 : ',cal_area(width,height))
