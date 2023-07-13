import unittest
from spicy_bdd import BddTest

class TestStorage(dict):
    def append(self, key, value):
        self[key] = value


class BddTestTest(BddTest):
    def scenario_add_two_numbers(self, given, when, then):
        given(add=lambda x, y: x + y,
              a=1,
              b=2,
              c=3)
        when.add(given.a, given.b)
        then.it.should.equal(3)

        when.add(given.a, given.c)
        then.it.should.equal(4)

        when.add(given.b, given.c)
        then.it.should.equal(5)

    def scenario_append_and_get_item(self, given, when, then):
        given(storage=TestStorage(),
              value="this is test",
              key="hoge")
        when.storage.append(given.key, given.value)
        then.storage.get(given.key).should.equal(given.value)

    def scenario_append_item_to_list(self, given, when, then):
        given(the_list=[1, 2, 3])
        when.the_list.append(6)
        then.the_list.length.should.equal(4)\
            ._and.the.value.at(0).should.equal(1)\
            ._and.the.value.at(1).should.equal(2)\
            ._and.the.value.at(2).should.equal(3)
        
    def scenario_append_item_to_list_twice(self, given, when, then):
        given(the_list=[1, 2, 3])
        when.the_list.append(7)\
            ._and.the_list.append(8)
        then.the_list.length.should.greater_equal(4)\
            ._and.the.length.should.equal(5)\
            ._and.the.length.should.be.less_than(6)\
            ._and.the.length.should.greater_equal(4)\
            ._and.the.length.should.less_equal(6)

    def scenario_raise_exception(self, given, when, then):
        given(fn1=lambda : 1,
              fn2=lambda : [].foo)
        when.fn1()
        then.fn2().should._raise(AttributeError)\
            ._and.fn1().should.not_raise(AttributeError)
        
if __name__ == '__main__':
    unittest.main()
