'''
딕셔너리 목록에서 특정키 값을 기준으로 분류합니다
@link https://docs.python.org/3.7/library/itertools.html
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import operator

data = [
    {'name': '홍길동1', 'blood': 'A'},
    {'name': '홍길동3', 'blood': 'A'},
    {'name': '홍길동1', 'blood': 'B'},
    {'name': '홍길동2', 'blood': 'AB'},
    {'name': '홍길동2', 'blood': 'B'},
    {'name': '홍길동3', 'blood': 'A'}
]

# blood값을 기준으로 정렬 오름차순 정렬합니다.
# 정렬하지 않는 경우 동일한 분류목록이 여러개가 생기는 문제점이 있으므로 정렬 필수!
data = sorted(data, key = operator.itemgetter('blood'))

# blood 키값이 동일한 기준으로 분류합니다.
grouped_data = itertools.groupby(data, key = operator.itemgetter('blood'))
for key, group_data in grouped_data:
    glist = list(group_data)
    print(key, "=>" , glist)

"""
실행결과
A => [{'name': '홍길동1', 'blood': 'A'}, {'name': '홍길동3', 'blood': 'A'}, {'name': '홍길동3', 'blood': 'A'}]
AB => [{'name': '홍길동2', 'blood': 'AB'}]
B => [{'name': '홍길동1', 'blood': 'B'}, {'name': '홍길동2', 'blood': 'B'}]
"""

# 분류할 기준 키가 2개 이상인 경우
data = sorted(data, key = operator.itemgetter('blood', 'name'))
grouped_data = itertools.groupby(data, key = operator.itemgetter('blood', 'name'))

for key, group_data in grouped_data:
    glist = list(group_data)
    print(key, "=>" , glist)

"""
실행결과
('A', '홍길동1') => [{'name': '홍길동1', 'blood': 'A'}]
('A', '홍길동3') => [{'name': '홍길동3', 'blood': 'A'}, {'name': '홍길동3', 'blood': 'A'}]
('AB', '홍길동2') => [{'name': '홍길동2', 'blood': 'AB'}]
('B', '홍길동1') => [{'name': '홍길동1', 'blood': 'B'}]
('B', '홍길동2') => [{'name': '홍길동2', 'blood': 'B'}]
"""

