import numpy as np

N = int(input())

x = list()  # 3kg 봉지의 개수
y = list()  # 5kg 봉지의 개수
result = 0
for i in range(int(N/3)+1):
    for j in range(int(N/5)+1):
        if ((3*i + 5*j) ==N):
            x.append(i)
            y.append(j)
            # idx = np.argmax(y)
            # result = x[idx] + y[idx]
            # print("x:", i, "y:", j)
        # else:
        #     x.append(-1)
            # y.append(-1)
            # result = -1
            # print("result:", result)
if not x:
    result = -1
else:
    idx = np.argmax(y)
    result = x[idx] + y[idx]
print("result: ", result)

# max = y[0]
# for i in range(len(y)):
#     if (max < y[i]):
#         max = y[i]

# index = np.argmax(y)
# print("x: ", x[index])
# print("y: ", y[index])
# print("result: ", result)
