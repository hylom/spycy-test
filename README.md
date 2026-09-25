# Spycy-test: BDD style test helper library

`Spycy-test` is a BDD style test helper library inspired by JavaScript's [Chai Assertion Library](https://www.chaijs.com/).


# How to use

Based on Python's `unittest`module.

```
import unittest
from spycy_test import BddTest
```

You can create tests extending with `BddTest`.

```
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
```

