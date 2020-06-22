from timeit import Timer


def test01():
    list = []
    for i in range(1000):
        list += [i]
    return list


def test02():
    list = []
    for i in range(1000):
        list.append(i)
    return list


def test03():
    return [i for i in range(1000)]


def test04():
    alist = list(range(1000))
    return alist


if __name__ == "__main__":
    timer = Timer("test01()", "from __main__  import test01")
    t1 = timer.timeit(1000)
    print(t1)
    timer2 = Timer("test02()", "from __main__  import test02")
    t2 = timer2.timeit(1000)
    print(t2)
    timer3 = Timer("test03()", "from __main__  import test03")
    t3 = timer3.timeit(1000)
    print(t3)
    timer4 = Timer("test04()", "from __main__  import test04")
    t4 = timer4.timeit(1000)
    print(t4)
