"""
doc_string for test_python_class
"""
from simple_class import SimpleClass


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
