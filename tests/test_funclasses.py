import funclasses


class TestClassA:
    def test_init(self):
        obj1 = funclasses.ClassA()
        assert obj1.count == 10
        assert obj1.size == 10

    def test_init_with_params(self):
        obj1 = funclasses.ClassA(20)
        assert obj1.count == 10
        assert obj1.size == 20

    def test_repr(self):
        obj1 = funclasses.ClassA(20)
        assert repr(obj1) == "ClassA(count=10,size=20)"

    def test_str(self):
        obj1 = funclasses.ClassA(20)
        assert str(obj1) == "count=10,size=20"


class TestClassB:
    def test_init(self):
        objb = funclasses.ClassB()
        assert objb.count == 10
        assert objb.size == 10
        assert objb.bsize == 100

    def test_init_with_params(self):
        objb = funclasses.ClassB(bsize=200, size=100)
        assert objb.count == 10
        assert objb.size == 100
        assert objb.bsize == 200

    def test_repr(self):
        objb = funclasses.ClassB(bsize=200, size=100)
        assert repr(objb) == "ClassB(bsize=200)--ClassA(count=10,size=100)"

    def test_str(self):
        objb = funclasses.ClassB(bsize=200, size=100)
        assert str(objb) == "bsize=200,count=10,size=100"
