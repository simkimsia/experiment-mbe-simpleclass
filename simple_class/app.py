"""
doc string for app module
"""
from enum import Enum


class SimpleClass:
    """
    This is handwritten
    First Created: 2020-08-30 17:35 UTC+8
    Last Modified: 2020-08-30 17:41 UTC+8
    """

    # Class description
    # none

    # PIM constants
    # none

    SimpleClass_states = Enum("SimpleClass_states", "EXISTS DOESNTEXIST")

    def __init__(self):
        pass


#    // Attribute instance variables

#       private int x;
#       private SimpleClass_states state;


#    // Association participation instance variables

#       // none


#    // Constructor

#       public SimpleClass() {
#       // requires
#       //    none
#       // guarantees
#       //    --> x has been set to zero and state == Exists
#          this.initializer();
#          state = SimpleClass_states.EXISTS;
#          simpleClassSet.add( this );
#       }


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


#    // Private transition actions

#       private void initializer() {
#       // requires
#       //   none
#       // guarantees
#       //   x has been set to zero
#          x = 0;
#       }

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


#    // All class members accessor

#    private static ArrayList<SimpleClass> simpleClassSet = new ArrayList<SimpleClass>();

#       public static ArrayList<SimpleClass> allSimpleClasss() {
#       // requires
#       //   none
#       // guarantees
#       // returns (reference to) ArrayList<> of all class members
#          return simpleClassSet;
#       }


#    // Association participation link and unlink services

#       // none
