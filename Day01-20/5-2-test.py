"""
5-2-test - 

Author: 蔡兆胜
Version: 1.0
2026/1/28
"""

a = int(input('状态码：'))
match a:
    case 400: description = '1'
    case 401: description = '2'
    case 403: description = '3'
    case 404: description = '4'
    case _: description = '🈚️'
print('状态码分析:', description)
