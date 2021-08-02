import numpy as np


def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    calculations = {
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }
    a = np.array(list).reshape(3, 3)
    # 求平均值
    me = a.mean(0)
    me = np.append(me, a.mean(1))
    me.resize(2, 3)
    me = me.tolist()
    tme = sum(list) / 9
    me.append(tme)
    calculations['mean'] = me
    # 求标准差
    va = a.var(0)
    va1 = a.var(1)
    va = np.append(va, va1, axis=0).reshape(2, 3)
    va = va.tolist()
    l = np.array(list)
    va.append(l.var())
    calculations['variance'] = va
    # 求方差
    st = a.std(0)
    st = np.append(st, a.std(1)).reshape(2, 3)
    st = st.tolist()
    st.append(l.std())
    calculations['standard deviation'] = st
    # 最大值
    ma = a.max(0)
    ma = np.append(ma, a.max(1)).reshape(2, 3)
    ma = ma.tolist()
    ma.append(l.max())
    calculations['max'] = ma
    # 求最小值
    mi = a.min(0)
    mi = np.append(mi, a.min(1)).reshape(2, 3)
    mi = mi.tolist()
    mi.append(l.min())
    calculations['min'] = mi
    # 求和
    su = a.sum(0)
    su = np.append(su, a.sum(1)).reshape(2, 3)
    su = su.tolist()
    su.append(l.sum())
    calculations['sum'] = su
    return calculations
