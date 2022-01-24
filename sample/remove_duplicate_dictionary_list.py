'''
dictionary list 중복 제거
@author: lsy
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = [
    {'name': '홍길동1', 'blood': 'A'},
    {'name': '홍길동1', 'blood': 'B'},
    {'name': '홍길동2', 'blood': 'AB'},
    {'name': '홍길동2', 'blood': 'B'},
    {'name': '홍길동3', 'blood': 'A'},
    {'name': '홍길동3', 'blood': 'A'}
]

# 모든 값이 동일한 데이터 중복제거
print([i for n, i in enumerate(data) if i not in data[n + 1:]])
"""
출력결과
[{'name': '홍길동1', 'blood': 'A'},
{'name': '홍길동1', 'blood': 'B'},
{'name': '홍길동2', 'blood': 'AB'},
{'name': '홍길동2', 'blood': 'B'},
{'name': '홍길동3', 'blood': 'A'}]
"""

# 키값을 기준으로 중복제거
print(list({v['name']:v for v in data}.values()))

"""
출력결과
[{'name': '홍길동1', 'blood': 'B'},
{'name': '홍길동2', 'blood': 'B'},
{'name': '홍길동3', 'blood': 'A'}]
"""
