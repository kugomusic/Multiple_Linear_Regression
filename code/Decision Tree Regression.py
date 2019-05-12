# -*- coding: utf-8 -*-

from numpy import genfromtxt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# 读数据，分别为训练集和测试集
data = genfromtxt('data.csv', delimiter=',')
data_test = genfromtxt('data_test.csv', delimiter=',')

# X为特征，Y为结果
X = data[:, 0:-1]
Y = data[:, -1]

X_test = data_test[:, 0:-1]
Y_test = data_test[:, -1]

# 决策树回归模型
regression_equation = DecisionTreeRegressor();
regression_equation.fit(X,Y)

# print('系数为')
# print(regression_equation.coef_)
# print('截面或截距为')
# print(regression_equation.intercept_)

# 为三维图准备数据，x,y,z为三维坐标值
xs = []
ys = []
zs = []
zs_predict = []

for x in X_test:
    xs.append(x[0])
    ys.append(x[1])
    x = np.array(x).reshape(1, -1)
    predict = regression_equation.predict(x)
    print('流量负载和转发负载阈值为：' + str(x) + ' 时，')
    print('预测结果为：', predict[0])
    zs_predict.append(predict[0])

for z in Y_test:
    zs.append(z)

print("预测值")
print(zs_predict)
print("真实值")
print(zs)

# 训练集坐标数据
xs_train = []
ys_train = []
zs_train = Y
for x in X:
    xs_train.append(x[0])
    ys_train.append(x[1])

# 绘制3D散点图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, s=20, c='blue', depthshade=True)
ax.scatter(xs, ys, zs_predict, s=20, c='red', depthshade=True)
# ax.scatter(xs_train, ys_train, zs_train, s=35, c='black', depthshade=True, marker='+')

ax.set_xlabel('Traffic load')
ax.set_ylabel('Forwarding load threshold')
ax.set_zlabel('Hot spot proportional threshold')

plt.show()