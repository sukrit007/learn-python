class ClassA:
    count = 10

    def __init__(self, size=10):
        self.size = size

    def __repr__(self) -> str:
        return "ClassA(count=%d,size=%d)" % (self.count, self.size)

    def __str__(self) -> str:
        return "count=%d,size=%d" % (self.count, self.size)


class ClassB(ClassA):
    bcount = 20

    def __init__(self, size=10, bsize=100):
        super().__init__(size)
        self.bsize = bsize

    def __repr__(self) -> str:
        return "ClassB(bsize=%d)" % self.bsize + "--" + super().__repr__()

    def __str__(self):
        return "bsize=%d" % self.bsize + "," + super().__str__()


if __name__ == "__main__":
    print("ClassA#count: %d" % ClassA.count)
    obj1 = ClassA()
    obj2 = ClassA(20)

    print("obj1#count(original): %d" % obj1.count)
    obj1.count = 100
    print("obj1#count(modified): %d" % obj1.count)
    print("obj2#count: %d" % obj2.count)

    print("Obj1: %r" % obj1)
    print("Obj2.__dict__: %r" % obj2.__dict__)

    objB = ClassB(100)
    print("ObjB(repr): %r" % objB)
    print("ObjB(str): %s" % objB)
