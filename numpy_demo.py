# -*- coding:utf-8 -*-
import numpy as np

'''
ndarray是N维数组对象（矩阵），其中所有的元素都必须是相同类型。ndarray主要包含以下几个属性：

ndarray.ndim：表示数组对象或矩阵的维度；

ndarray.shape：表示每个维度上的数组的大小；

ndarray.size：表示数组中元素的总数，等同于ndarray.shape中两个元素的乘积；

ndarray.dtype：表示数组中元素的类型；

ndarray.itemsize：表示数组中每个元素的字节大小，比如数据类型为float64的数组，其元素的字节大小为64/8=8。
'''


def test():
    # 创建二维数组 三行 一行5个
    a = np.arange(27).reshape(3, 3, 3)
    print(a)
    # 获取矩阵大小
    print("获取矩阵大小", a.shape)
    # 获取矩阵维度   一维数组 二维等
    print("获取矩阵维度", a.ndim)
    # 获取数组中元素的类型
    print("获取元素类型", a.dtype.name)
    # 获取数组中元素的大小
    print("获取数组中元素的大小", a.itemsize)
    # 获取元素总数量
    print("获取元素总数量", a.size)


'''
创建Numpy数组
'''


def create_numpy():
    a = np.array([2, 3, 4])  # 创建一维数组
    b = np.array([(2, 3, 4), (5, 6, 7)])  # 创建二维数组
    c = np.array([[1, 2], [3, 4]], dtype=np.float64)  # 创建指定数据类型的数
    d = np.zeros((3, 4))  # 创建3行4列矩阵，用0初始化矩阵中所有的元素
    e = np.ones((2, 3, 4), dtype=np.int16)  # 创建三维矩阵，维度分别为2，3，4，且用1来初始化矩阵中所有的元素
    f = np.empty((2, 3))  # 创建2行3列空矩阵，矩阵中元素初始值随机，取决于内存状态，默认情况下，创建的数组的dtype为float64
    g = np.arange(6)
    h = np.arange(10, 30, 5)
    print(type(h))
    print(h)


'''
数学计算增删改查
'''
def calculate_numpy():
    pass


if __name__ == '__main__':
    # 测试语句
    test()
    # 创建数组
    create_numpy()
    # 科学技术计算学习
    calculate_numpy()

