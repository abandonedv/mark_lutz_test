def classtree(cls, indent):
    print("." * indent + cls.__name__)
    print(cls.__bases__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)


def instancetree(inst):
    print("Tree of %s" % inst)
    print(inst.__class__)
    # print(inst.__name__)
    classtree(inst.__class__, 3)


def selftest():
    class A: pass

    class B(A):
        x = 3

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass

    a = B()
    print(a)
    instancetree(B())
    instancetree(F())


selftest()
