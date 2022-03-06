# class A:
#     __slots__ = ["a", "b"]
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class B(A):
#     __slots__ = ["c"]
#
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.c = c
#
#
# a = B(1, 2, 3)
# print(a.__slots__)
# # print(a.__dict__)
# print(list(x for x in dir(a) if not x.startswith("__")))

class X: pass
class Y: pass

X.a = 1
X.b = 2
X.c = 3
Y.a = X.a + X.b + X.c
for X.i in range(Y.a): print(X.i)
print(X.__dict__)