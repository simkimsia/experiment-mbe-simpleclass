"""
doc string for models module
"""
from enum import Enum
from typing import ClassVar, List


class SimpleClass:
    """
    This is handwritten
    First Created: 2020-08-30 17:35 UTC+8
    Last Modified: 2020-08-31 22:00 UTC+8
    """

    # Class description
    # none

    # PIM constants
    # none

    SimpleClass_states = Enum("SimpleClass_states", "EXISTS DOESNTEXIST")

    # Attribute instance variables
    # Python doesn't treat private variables too strictly
    # by convention it uses _ for private variables
    # https://docs.python.org/3/tutorial/classes.html#private-variables
    # and it treats client code as responsible users if they choose to ignore the convention
    # https://docs.python-guide.org/writing/style/#we-are-all-responsible-users
    _x: int
    _state: SimpleClass_states

    # Association participation instance variables
    # none

    #   Constructor
    def __init__(self) -> None:
        # requires
        #     none
        # guarantees
        #    --> x has been set to zero and state == Exists
        self._initializer()
        self._state = SimpleClass.SimpleClass_states.EXISTS
        SimpleClass.simpleClassSet.append(self)

    # Attribute getters
    # https://www.geeksforgeeks.org/getter-and-setter-in-python/

    # prefer the 2nd way of using property decorator if insist on getters and setters
    # for completeness, include getters for the private variables
    # for more pythonic approach,
    # if a private variable has a getter that doesn't change anything
    # then simply allow the variable
    @property
    def x(self) -> int:
        # requires
        #    none
        # guarantees
        #    returns the x
        return self._x

    @property
    def state(self) -> SimpleClass_states:
        # requires
        #    none
        # guarantees
        #    returns the state
        return self._state

    # Derived attributes
    #   none

    # Pushed events

    def destroy(self) -> None:
        # requires
        #    none
        # guarantees
        #   state was Exists --> state == Doesn't exist
        if self._state == SimpleClass.SimpleClass_states.EXISTS:
            self._state = SimpleClass.SimpleClass_states.DOESNTEXIST
            SimpleClass.simpleClassSet.remove(self)

    def update(self, newX: int) -> None:
        # requires
        #    none
        # guarantees
        #    state was Exists --> x has been set to new x
        if self._state == SimpleClass.SimpleClass_states.EXISTS:
            self._updateX(newX)

    # Private transition actions

    def _initializer(self) -> None:
        # requires
        #    none
        #  guarantees
        #    x has been set to zero
        self._x = 0

    def _updateX(self, newX: int) -> None:
        # requires
        #    none
        #  guarantees
        #    x has been set to new x
        self._x = newX

    # PIM Overlay helper code

    #    comment 1
    #       helper comment 2
    #       helper comment 3
    #       comment 4


#    // Association participation link and unlink services

#       // none

# ClassVariable that holds all class member
# https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations => ClassVar
# https://stackoverflow.com/a/40244539/80353 => How to define ClassVar whose type is its own class
SimpleClass.simpleClassSet: ClassVar[List[SimpleClass]] = []  # Class variable only

# declare a all class member accessor as staticmethod
# https://www.studytonight.com/python/python-static-keyword
# note we use staticmethod not classmethod because no change on class variable
# also we do this outside of class because the return type involves the class itself
def allSimpleClass() -> List[SimpleClass]:
    # requires
    #   none
    # guarantees
    # returns (reference to) List of all class members
    return SimpleClass.simpleClassSet


SimpleClass.allSimpleClass = staticmethod(allSimpleClass)


class PythonicSimpleClass:
    """
    This is handwritten
    First Created: 2020-08-31 21:52 UTC+8
    Last Modified: 2020-08-31 22:10 UTC+8
    """

    # Class description
    # none

    # PIM constants
    # none

    SimpleClass_states = Enum("SimpleClass_states", "EXISTS DOESNTEXIST")

    # Attribute instance variables
    # Python doesn't treat private variables too strictly
    # by convention it uses _ for private variables
    # https://docs.python.org/3/tutorial/classes.html#private-variables
    # and it treats client code as responsible users if they choose to ignore the convention
    # https://docs.python-guide.org/writing/style/#we-are-all-responsible-users
    x: int
    state: SimpleClass_states

    # Association participation instance variables
    # none

    #   Constructor
    def __init__(self) -> None:
        # requires
        #     none
        # guarantees
        #    --> x has been set to zero and state == Exists
        self.x = 0
        self.state = PythonicSimpleClass.SimpleClass_states.EXISTS
        PythonicSimpleClass.simpleClassSet.append(self)

    # Derived attributes
    #   none

    # Pushed events

    def destroy(self) -> None:
        # requires
        #    none
        # guarantees
        #   state was Exists --> state == Doesn't exist
        if self.state == PythonicSimpleClass.SimpleClass_states.EXISTS:
            self.state = PythonicSimpleClass.SimpleClass_states.DOESNTEXIST
            PythonicSimpleClass.simpleClassSet.remove(self)

    def update(self, newX: int) -> None:
        # requires
        #    none
        # guarantees
        #    state was Exists --> x has been set to new x
        if self.state == PythonicSimpleClass.SimpleClass_states.EXISTS:
            self.x = newX

    # Private transition actions
    #   none

    # PIM Overlay helper code

    #    comment 1
    #       helper comment 2
    #       helper comment 3
    #       comment 4

    #  Association participation link and unlink services

    #    none


# ClassVariable that holds all class member
# https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations => ClassVar
# https://stackoverflow.com/a/40244539/80353 => How to define ClassVar whose type is its own class
PythonicSimpleClass.simpleClassSet: ClassVar[List[PythonicSimpleClass]] = []  # Class variable only
