"""
5-3 - 

Author: 蔡兆胜
Version: 1.0
2026/1/28
"""

a = float(input('请输入三角形的边,a='))
b = float(input('请输入三角形的边,b='))
c = float(input('请输入三角形的边,c='))
if a + b > c and b + c > a and c + a > b:
    p = a + b + c
    print(f'周长: {p:.2f}')
    s = p / 2
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    print(f'面积: {area:.2f}')
else:
    print('无法构成三角形')