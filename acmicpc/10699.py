"""
백준 10699. 오늘 날짜
problem : https://www.acmicpc.net/problem/10699
"""

from datetime import datetime

# 방법1
datetime.today().strftime("%Y-%m-%d")

# 방법2
print(str(datetime.today())[:10])
