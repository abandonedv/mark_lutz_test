# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError
#
#         return args[0].strip(self.__chars)

# def StripChars(chars):
#     def stringStrip(string):
#         if not isinstance(string, str):
#             raise ValueError
#         return string.strip(chars)
#     return stringStrip
#
# s1 = StripChars("?:!.; ")
# print(s1(" Hello World! "))

class DefVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        # print(self)
        # print(self.__dict__)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return True


v1 = [1, 2, 3]
v2 = [1, 2, 3]
with DefVector(v1) as dv:
    for i in range(len(dv)):
        dv[i] += v2[i]

print(v1)
