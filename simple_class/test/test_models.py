"""
doc_string for test_python_class
"""
import random

from simple_class import PythonicSimpleClass, SimpleClass


class TestSimpleClass:
    def teardown_method(self, test_method):
        SimpleClass.simpleClassSet.clear()

    def test_states(self):
        """
        test states
        """
        assert SimpleClass.SimpleClass_states.EXISTS == SimpleClass.SimpleClass_states.EXISTS
        assert (
            SimpleClass.SimpleClass_states.DOESNTEXIST == SimpleClass.SimpleClass_states.DOESNTEXIST
        )

    def test_constructor(self):
        """
        test the constructor
        """
        # this tests that the constructor will append the new instance into the class variable
        assert len(SimpleClass.simpleClassSet) == 0
        s = SimpleClass()
        assert len(SimpleClass.simpleClassSet) == 1
        assert SimpleClass.simpleClassSet[0] == s

        # this tests the _state instance attribute
        assert s._state == SimpleClass.SimpleClass_states.EXISTS

        # this tests the initializer method which sets _x
        assert s._x == 0

    def test_getters(self):
        """
        test the getters
        """
        s = SimpleClass()
        assert s.x == 0
        assert s.state == SimpleClass.SimpleClass_states.EXISTS

    def test_destroy(self):
        """
        test the destroy
        """
        assert len(SimpleClass.simpleClassSet) == 0
        s = SimpleClass()
        assert len(SimpleClass.simpleClassSet) == 1
        assert SimpleClass.simpleClassSet[0] == s
        s.destroy()
        assert len(SimpleClass.simpleClassSet) == 0

    def test_update(self):
        """
        test the update
        """
        s = SimpleClass()
        assert s.x == 0
        newX = random.randint(1, 1000000)
        s.update(newX)
        assert s.x == newX

    def test_static_all_class_member_accessor(self):
        """
        test the static_all_class_member_accessor
        """
        assert len(SimpleClass.allSimpleClass()) == 0


class TestPythonicSimpleClass:
    def teardown_method(self, test_method):
        PythonicSimpleClass.simpleClassSet.clear()

    def test_states(self):
        """
        test states
        """
        assert (
            PythonicSimpleClass.SimpleClass_states.EXISTS
            == PythonicSimpleClass.SimpleClass_states.EXISTS
        )
        assert (
            PythonicSimpleClass.SimpleClass_states.DOESNTEXIST
            == PythonicSimpleClass.SimpleClass_states.DOESNTEXIST
        )

    def test_constructor(self):
        """
        test the constructor
        """
        # this tests that the constructor will append the new instance into the class variable
        assert len(PythonicSimpleClass.simpleClassSet) == 0
        s = PythonicSimpleClass()
        assert len(PythonicSimpleClass.simpleClassSet) == 1
        assert PythonicSimpleClass.simpleClassSet[0] == s

        # this tests the _state instance attribute
        assert s.state == PythonicSimpleClass.SimpleClass_states.EXISTS

        # this tests the initializer method which sets _x
        assert s.x == 0

    def test_destroy(self):
        """
        test the destroy
        """
        assert len(PythonicSimpleClass.simpleClassSet) == 0
        s = PythonicSimpleClass()
        assert len(PythonicSimpleClass.simpleClassSet) == 1
        assert PythonicSimpleClass.simpleClassSet[0] == s
        s.destroy()
        assert len(PythonicSimpleClass.simpleClassSet) == 0

    def test_update(self):
        """
        test the update
        """
        s = PythonicSimpleClass()
        assert s.x == 0
        newX = random.randint(1, 1000000)
        s.update(newX)
        assert s.x == newX
