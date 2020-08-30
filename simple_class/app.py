"""
doc string for app module
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
    # python doesn't do private so by convention use _
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
        # import ipdb

        # ipdb.set_trace()
        self._initializer()
        self._state = SimpleClass.SimpleClass_states.EXISTS
        SimpleClass.simpleClassSet.append(self)

    #    // Attribute getters

    #       public int x() {
    #       // requires
    #       //   none
    #       // guarantees
    #       //   returns the x
    #          return x;
    #       }

    #       public SimpleClass_states state() {
    #       // requires
    #       //   none
    #       // guarantees
    #       //   returns the state
    #          return state;
    #       }

    #    // Derived attributes

    #       // none

    #    // Pushed events

    #       public void destroy() {
    #       // requires
    #       //    none
    #       // guarantees
    #       //   state was Exists --> state == Doesn't exist
    #          if( state == SimpleClass_states.EXISTS ) {
    #             state = SimpleClass_states.DOESNTEXIST;
    #             simpleClassSet.remove( this );
    #          }
    #       }

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
