def tracer(func):  # Запоминает оригинал
    def oncall(*args):  # При последующих вызовах
        oncall.calls += 1
        print("call %s to %s" % (oncall.calls, func.__name__))
        return func(*args)

    oncall.calls = 0
    return oncall


class C:
    @tracer
    def spam(self, a, b, c):
        return a + b + c


x = C()
print(x.spam(1, 2, 3))
print(x.spam("a", "b", "c"))  # Такой же вывод, как у tracer! (в tracer2.py)
