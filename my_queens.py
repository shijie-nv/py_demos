# -*- coding: utf-8 -*-

'''
Created on 2011-4-2

@author: csj
'''


def solve(m, n):
    if n == 0:
        yield []
    else:
        for p in solve(m, n - 1):
            for i in range(m):
                flag = True
                for j in range(n - 1):
                    if abs(i - p[j]) in (0, n - j - 1):
                        flag = False
                        break
                if flag:
                    yield p + [i]


def draw(x):
    n = len(x)
    for i in range(n):
        print('.' * x[i] + 'Q' + '.' * (n - x[i] - 1))
    print()


def flipX(v):
    n = len(v)
    return [n - 1 - x for x in v]


def flipY(v):
    return v[::-1]


def flipXY(v):
    return flipX(flipY(v))


def tp(v):
    n = len(v)
    w = [0] * n
    for i in range(n):
        w[v[i]] = i
    return w


def test(x):
    s = []
    s.append(x)
    s.append(flipX(x))
    s.append(flipY(x))
    s.append(flipXY(x))
    s.append(tp(x))
    s.append(tp(flipX(x)))
    s.append(tp(flipY(x)))
    s.append(tp(flipXY(x)))
    s.sort()
    if x == s[0]:
        return True
    else:
        return False


if __name__ == '__main__':
    n = 8
    count = 0
    for x in solve(n, n):
        if test(x):
            draw(x)
            count += 1
    print(count)

# 不重复的皇后问题
# 8皇后问题的92组解里，有11组解通过水平翻转、竖直翻转、关于主、副对角线翻转，
# 能得到7个衍生解，加上本身是8个解。
# 还有一个解是中心对称的，所以它通过翻转和旋转只能得到3个衍生解。
