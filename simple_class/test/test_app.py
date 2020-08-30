"""
doc_string for test_python_class
"""
from simple_class import SimpleClass


def test_states():
    """
    test states
    """
    s = SimpleClass()
    assert s.SimpleClass_states.EXISTS == s.SimpleClass_states.EXISTS
    assert s.SimpleClass_states.DOESNTEXIST == s.SimpleClass_states.DOESNTEXIST
