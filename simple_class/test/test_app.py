"""
doc_string for test_python_class
"""
from simple_class import SimpleClass


def test_states():
    """
    test states
    """
    assert SimpleClass.SimpleClass_states.EXISTS == SimpleClass.SimpleClass_states.EXISTS
    assert SimpleClass.SimpleClass_states.DOESNTEXIST == SimpleClass.SimpleClass_states.DOESNTEXIST
