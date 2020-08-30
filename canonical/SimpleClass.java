package SimpleClass;

import java.util.ArrayList;
import java.util.something;;

public class SimpleClass {

   // generated 2020/08/30 17:23:21 by JAL open model compiler v5.3
   
   
   // Class description
   
      // none
   
   
   // PIM constants
   
      // none
   
   
   public enum SimpleClass_states { EXISTS, DOESNTEXIST };
   
   
   // Attribute instance variables
   
      private int x;
      private SimpleClass_states state;
   
   
   // Association participation instance variables
   
      // none
   
   
   // Constructor
   
      public SimpleClass() {
      // requires
      //    none
      // guarantees
      //    --> x has been set to zero and state == Exists
         this.initializer();
         state = SimpleClass_states.EXISTS;
         simpleClassSet.add( this );
      }
   
   
   // Attribute getters
   
      public int x() {
      // requires
      //   none
      // guarantees
      //   returns the x
         return x;
      }
      
      public SimpleClass_states state() {
      // requires
      //   none
      // guarantees
      //   returns the state
         return state;
      }
      
   
   // Derived attributes
   
      // none
      
   
   // Pushed events
   
      public void destroy() {
      // requires
      //    none
      // guarantees
      //   state was Exists --> state == Doesn't exist
         if( state == SimpleClass_states.EXISTS ) {
            state = SimpleClass_states.DOESNTEXIST;
            simpleClassSet.remove( this );
         }
      }
      
      public void update( int newX ) {
      // requires
      //    none
      // guarantees
      //   state was Exists --> x has been set to new x 
         if( state == SimpleClass_states.EXISTS ) {
            this.updateX( newX );
         }
      }
      
   
   // Private transition actions
   
      private void initializer() {
      // requires
      //   none
      // guarantees
      //   x has been set to zero
         x = 0;
      }
      
      private void updateX( int newX ) {
      // requires
      //   none
      // guarantees
      //   x has been set to new x
         x = newX;
      }
      
   
   // PIM Overlay helper code
   
      // comment 1
      // helper comment 2
      	// helper comment 3
      // comment 4
      
   
   // All class members accessor
   
      private static ArrayList<SimpleClass> simpleClassSet = new ArrayList<SimpleClass>();
      
      public static ArrayList<SimpleClass> allSimpleClasss() {
      // requires
      //   none
      // guarantees
      // returns (reference to) ArrayList<> of all class members
         return simpleClassSet;
      }
   
   
   // Association participation link and unlink services
   
      // none
   
}


