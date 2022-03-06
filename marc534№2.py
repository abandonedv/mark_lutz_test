import sys
from marc534 import timer

force = list


@timer(trace=True, label="[CCC]==>")
def listcomp(N):  # Подобно listcomp = timer(...) (listcomp)
    return [x * 2 for x in range(N)]  # listcomp(...) triggers Timer.__call__


@timer(trace=False, label="[MMM]==>")
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    result = func(5)  # Время для этого вызова, всех вызовов
    # и возвращаемое значение
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s\n' % func.alltime)  # Суммарное время для всех вызовов
print('**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
