"""
doc string for models module
"""
from enum import Enum
from typing import ClassVar, List


class SimpleClass:
    """
    This is handwritten
    First Created: 2020-08-30 17:35 UTC+8
    Last Modified: 2020-08-30 20:54 UTC+8
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

    #       public void update( int newX ) {
    #       // requires
    #       //    none
    #       // guarantees
    #       //   state was Exists --> x has been set to new x
    #          if( state == SimpleClass_states.EXISTS ) {
    #             this.updateX( newX );
    #          }
    #       }

    # Private transition actions

    def _initializer(self) -> None:
        # requires
        #    none
        #  guarantees
        #    x has been set to zero
        self._x = 0

    #       private void updateX( int newX ) {
    #       // requires
    #       //   none
    #       // guarantees
    #       //   x has been set to new x
    #          x = newX;
    #       }

    #    // PIM Overlay helper code

    #       // comment 1
    #       // helper comment 2
    #       	// helper comment 3
    #       // comment 4


#       public static ArrayList<SimpleClass> allSimpleClasss() {
#       // requires
#       //   none
#       // guarantees
#       // returns (reference to) ArrayList<> of all class members
#          return simpleClassSet;
#       }


#    // Association participation link and unlink services

#       // none

# All class members accessor
# https://mypy.readthedocs.io/en/stable/class_basics.html#class-attribute-annotations => ClassVar
# https://stackoverflow.com/a/40244539/80353 => How to define ClassVar whose type is its own class
SimpleClass.simpleClassSet: ClassVar[List[SimpleClass]] = []  # Class variable only
