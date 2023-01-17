{% include navigation.html %}

# Units 1-10 Work

# CB Unit 1: Primitives & Data Types

Java:
    - code must be in main method, use System.out.print();
    - comment code with //
Hacks
    
        public class Printing {
            public static void man(String[] args) {
                System.out.print(“Vaishavi”);
                System.out.println(“Team “JuiceWRLD);
                    System.out.println(“Rebecca, Lin, Divya”);
                }
            }
        Printing.main(null);

Data Types:
    * Integer (int): for whole numbers
    * Double (double): for numbers with decimals
    * Boolean (boolean): for true or false conditionals

Hack:

public class Biodata {

    public static void main(String[] args) {

	int age = 17;
        double height = 63.75;
        final boolean senior = true;
        String name = “Vaishavi is a senior”;

        System.out.println(age);
        System.out.println(height);
        System.out.println(name + senior);

    }
}

Biodata.main(null);

Operators:
Main ones are +, -, *, /
    - Dividing integers, it always rounds down because output must be an integer
    - Dividing by 0, will get the ArithemticException Error

Hack:

public class Operators {

    public static void main(String[] args) {
int number = 2;
        int number2 = 5;
        double number3 = 2.0;
        double number4 = 5.0;

        System.out.println(number+number2);
        System.out.println(number3+number4);
        System.out.println(number-number2);
        System.out.println(number3-number4);
        System.out.println(number * number2);
        System.out.println(number3 * number4);
        System.out.println(number/number2);
        System.out.println(number3/number4);
        System.out.println(number4 % number3);
        System.out.println(number2 % number);
    }
}

Operators.main(null);

Assignment operators (as per website, for notes/reference):
    
    * += adds value of a variabe to another variable and assigns total value to first variable
    
    * -= subtracts value of a variabe to another variable and assigns total value to first variable
    
    * *= multiplies value of a variabe to another variable and assigns total value to first variable
    
    * /= multiplies value of a variabe to another variable and assigns total value to first variable
    
    * %= takes the remainder of a variable with a second variable and assigns remainder to first variable
    
    * ++ increments a variable by 1, to incrememt by more change second plus to number which you want to incrememnt by
    
    * -- subracts a variable by 1, to incrememt by more change second plus to number which you want to subtract by



# CB Unit 2: Using Objects

### Notes:
Vocab: 
- programming paradigm that organizes software design around objects
- compartmentalize data and functions in such a way that data and the functions that operate on the data are bound together
- Classes: template or blueprint from which objects are created
    - initialized by calling class conductor
- Objects: created under the same class will share common methods and attributes.

Ex:
    
    // TO DO #1: Instigate a Painter object called myPainter
    Painter myPainter = new Painter();


Method declaration:
    
- Access modifier: Public, protected, private, or default (lack of modifier)
- Return type: The data type returned by the method. If there is no return value, this will be “void."
- Method name: The name of the method
- Parameter list: The list of variables the method will operate on, enclosed in parentheses
- Exception list: List of exceptions you expect during program runtime (i.e. exceptions the method should throw)
- Method body: The code the method will run on execution, enclosed in curly brackets

Calling a method looks something like the below:

	methodName(parameter1, parameter2);

Alternatively, to call an object’s method:

	objectReference.methodName(parameter1, parameter2);



# CB Unit 3: Boolean Expressions and If Statements

### Boolean Expressions:def: represent logic and tell whether something is true or false

Operators used to create Booleans:
    * == (same value/equals to)
    - != (checks for inequality)
    - < (less than)
    - <= (less than or equal to)
    - > (greater than)
    - >= (greater than or equal to)

Example: (a%2) == 0
     Is the variable "a" even?


### If Statements and Control Flow

Conditional Statements: perform computations depending on whether a Boolean condition evaluates to true or false
If Statements: if statement occurs if a block of code is run only if the condition is true

        public static boolean isEven(int number) }
        if (number % 2 == 0) {
        return true;
        }
        return false
        }

### If-Else Statements: statement to run a block of code among more than one alternative

        public static void main(String[] args) {
        int user = 17;
        if (user <= 18) {
        System.out.println(“User is 18 or younger”);
        }
        else {
        System.out.println(“User is older than 18);
        }
        }

### Else-if Statements: statement to run a condition if the original condition was false

        int time = 15;
        if (time > 21) { // 9 PM to 4 AM
        System.out.println("Good night");
        7
        else if (time > 17) {// 5 PM to 9 PM
        System.out.println("Good evening");
        }
        else if (time > 12) { // 12 PM to 5 PM
        System.out.println("Good afternoon");
        1
        else if (time > 4) {// 4 AM to 12 PM
        System.out.println("Good morning");
        1
        else { // 12 AM to 4 AM
        System.out.println("Good night");
        }


### Compound Boolean Expressions
Nested if statements: If-statements within if-statements
Note: If the outer if-statement evaluates to false, the inner if-statements are not evaluated.
    Logical operators: Used to combine Boolean expressions
    &&: and
    || : or
    ! : not 
    Short-circuited evaluation: The result of a compound Boolean expression can be determined just by looking at a few expressions

    boolean cloudy = true;
    boolean rainy = false;

    if (!cloudy && !rainy) {
    System.out.println(“Don’t forget to bring a hat!”);
    }

### Compound Boolean Expressions
    De Morgan's laws: Help simplify Boolean expressions
    !(a&&b) = (!a || !b)
    !(a || b) = (!a && !b)

Truth tables are a good way to visualize Boolean identities

### Comparing Objects
Use '==' to see if two object references are aliases for the same object or to see if an object is null
Use '.equals()' to see if the attributes of two objects are the same

    Vehicle car = new Vehicle("blue", 4);
    Vehicle car2 = new Vehicle("blue", 4); 
    Vehicle bluecar = car;

    car == car2     False
    car == bluecar   True
    car.equals(car2)  True

# CB Unit 4: Iteration

### While Loops
* Repeats lines of code until a certain condition evaluates to false
* Boolean expression is checked before the loop is started and every time the loop ends and is about to start anew
* Inside the loop something is done that slightly changes the conditions for the boolean expression until it reads false and ends
        int x = 5;

        // The boolean expression in this case is x > 0
        while (x > 0) {
            System.out.println(x);
            x--;
        }

* In the example below, the condition is x > 0, meaning that x has to be changed for the loop to stop. Inside the loop, x is decremented by 1 every time, changing the conditions over and over again until it finally returns false and terminates the while loop


        int[] array = {3, 7, 0, 2, 4, 5, 9, 1, 3, 6, 3};
        int total = 0;
        int i = 0;

        while (i < array.length) {
            total += array[i];
            i++;
        }

        System.out.println(total);


- While loops lie in infinite while loops, loops that run over and over again permanently
    - Usually accomplished by setting the boolean condition to be true at all times
    - Only way to stop these loops are to use a break command, which ends the loop regardless of the conditions present

### For Loops
Three Parts of a For Loop
* Initialization of a variable
* Test condition
* The code in the initialization area is executed only one time before the loop begins
* the test condition is checked each time through the loop and the loop continues as long as the condition is true
* the loop control variable change is done at the end of each execution of the body of the loop
* When the loop condition is false, execution will continue at the next statement after the body of the loop

### Loops and Strings

    String name = "CodeCodeCode";

    for (int i = 0; i < name.length(); i+=2) {
        System.out.println(name.substring(i,i+2));
    }

### Nested Iteration
- “Loop within loop”

    for (int row = 0; row < 5; row ++) {
        for (int column = 0; column < 4; column++) {
            System.out.print('*');
        }
        System.out.println();
    }

    —— 
    import java.util.ArrayList;

/*
 * Creator: Nighthawk Coding Society
 * Mini Lab Name: Hello Series,featuring Monkey Jumpers
 */

/**
 * Class for Monkey: a 2D array of Monkey
 * As well as method to print the Poem
 */
    
        class Monkey {
            //The area between class definition and the 1st method is where we keep data for object in Java
            private static ArrayList<String[]> monkeyList = new ArrayList<String[]>();    //2D Array: AP CSA Unit 8: 2D array of strings
            private String[] monkeyASCII;

        /**
        * Constructor initializes a 2D array of Monkey
        */
        public Monkey(String[] monkeyASCII) {
            this.monkeyASCII = monkeyASCII;
            monkeyList.add(monkeyASCII);
        }

        /**
        * Loop and print monkey in array
        * ... repeat until you reach zero  ...
        */
        public static void printPoem() {
            //begin the poem
            System.out.println();
            System.out.println("Monkey Jumpers Poem in Java with Objects!!!");

            // monkey (non-primitive) defined in constructor knows its length
            int monkeyCount = monkeyList.size();
            for (int i = 1; i <= monkeyCount; i++)  //loops through 2D array length forwards
            {

                //this print statement shows current count of Monkey
                //  concatenation (+) of the loop variable and string to form a countdown message
                System.out.println(i + " little monkey jumping on the bed...");

                //how many separate parts are there in a monkey monkey?
                for (int row = 0; row < i; row++) {  //cycles through "cells" of 2d array

                    /*cycles through columns to print
                    each monkey part by part, will eventually print entire column*/
                    for (int col = 0; col < monkeyList.get(row).length; col++) {

                        // prints specific part of the monkey from the column
                        System.out.print(monkeyList.get(row)[col] + " ");

                        //this is new line between separate parts
                        System.out.println();
                    }
                    
                    //this new line gives separation between stanza of poem
                    System.out.println();
                }

                //countdown for poem, decrementing monkeyCount variable by 1
                monkeyCount -= 1;
            }

            //out of all the loops, prints finishing messages
            System.out.println("Too many monkeys jumping on the bed");
            System.out.println("0000000000000000000000000000000000");
            System.out.println("             THE END              ");
        }

    
        /**
        * A Java Driver/Test method that is the entry point for execution
        */
        public static void main(String[] args)  {
            Monkey monkey0 = new Monkey(new String[]{
                "ʕง ͠° ͟ل͜ ͡°)ʔ ",      //[0][0] eyes
                "  \\_⏄_/  ",      //[0][1] chin
                "  --0--   ",       //[0][2] body
                "  ⎛   ⎞   "        //[0][3] legs
            });
            Monkey monkey1 = new Monkey(new String[]{
                " ʕ༼ ◕_◕ ༽ʔ",       //[1][0]
                "  \\_⎏_/  ",
                "  ++1++  ",
                "   ⌋ ⌊   "
            });
            Monkey monkey2 = new Monkey(new String[]{
                " ʕ(▀ ⍡ ▀)ʔ",       //[2][0]
                "  \\_⎐_/ ",
                "  <-2->  ",
                "  〈  〉 "
            });
            Monkey monkey3 = new Monkey(new String[]{
                "ʕ ͡° ͜ʖ ° ͡ʔ",        //[3][0]
                "  \\_⍾_/  ",
                "  ==3==  ",
                "  _/ \\_  "
            });
            Monkey monkey4 = new Monkey(new String[]{
                "  (◕‿◕✿) ",          //[4][0]
                "  \\_⍾_/ ",          //[4][1]
                "  ==4==  ",          //[4][2]
                "  _/ \\_ "           //[4][3]
            });

            
            Monkey.printPoem();   //a new monkey list and output in one step
        }

    }

    Monkey.main(null);

# CB Unit 5: Writing Classes

* Class: blueprint used to create objects
* Instance variables/attributes (data)
* Constructors
* Methods
* Accessors/Getters
* Mutators/Setters
* Main method (tester)
* Objects: instances of a class

# CB Unit 6: Arrays

Array: 
- data structure that contains collection of data (ex. arrays, ArrayLists)
- data in java array can be primitive or referenced
    - primitive: single variable type
    - referenced data types: string, array, classes). 
- parts of array:
    - element: one value in array
    - index: position of value in array, (ex. 0 indexing
Array SYntax
- declaring away variable, not initialized

    
    int[] array = new int[10];

- specifying initial values in array
    - int[] array2 = {10, 9, 8, 7, 6};
        - note: array elements start at 0!

Traverse an Array
- traversing: accessing values inside array (using iteration/loop to traverse an array)
Enhanced For Loops: 
- basic for loop: visits all elements of an array (ex. 62 & 63)
- enchanted for loops; visits all elements of array
    - DIFFERENCE: enhanced fro loops use variable element assigned to values[0], values[1], etc.
    - basic for loop assigned as 0, 1, etc. 

Developing Algorithms using Arrays:- identifying min/max value inside array
finding sums of arrays, checking for dupes, etc. 
    - NOTE:
        - array.length returns number of values inside array
        - array[i] - access array at index i


# CB Unit 7: Array List Lesson

| Arrays | ArrayLists |
| :----: | :-----: |
| Static (fixed size) | Dynamic (can change size) |
| Fundamental java feature	Part of a framework. Someone was nice and designed this with the behind the scenes being arrays |
| An object with no methods	| A class with many methods |
| Not as flexible | Designed to be more flexible |
| Can store more primitive data	Not designed to store primitives, they store object references | Slightly slower than Arrays | Can only be used with an import statement |

Example:
- 5 players on court is an Array, ArrayList, the number of people changes depending on who comes in and/or out
Primitive Data Types:
    * boolean
    * char
    * double
    * int
Wrapper Class Data Types (Store the primitive values as objects)
    * Boolean
    * Character
    * Double
    * Integer

        import java.util.ArrayList; //you must import the java.util package

        // Instantiating: ArrayList<DataType> variableName = new ArrayList<>(n);
        //DataType must be nonprimitive data type

        public class introArrayList {
            public static void main (String[] args) {
                ArrayList<Integer> e1 = new ArrayList<Integer>(); //empty
                ArrayList<String> e2 = new ArrayList<String>(5); //5 elements
                ArrayList<Dogs> e3 = new ArrayList<Dogs>(); //you can store whatever objects you want
            }
        }

Collegeboard ArrayList Methods;
size();
    * Returns the number of elements in the list
    add(obj);
    * Adds element at the end
    add(index, object);
    * Adds element at specific index
    remove(index);
    * Removes element from specific index
    set(index, object);
    * Replaces element at index with new object
    get(index);
    * Returns element at index

Example: 

        import java.util.ArrayList; 

        public class methodsArrayList {
            public static void main (String[] args) {
                ArrayList<String> dogs = new ArrayList<String>(Arrays.asList("Sparky", "Duke", "Noodle"));
                ArrayList<String> dogs2 = new ArrayList<>(Arrays.asList("Sparky", "Duke", "Noodle"));
                System.out.println("There are " + dogs.size() + " in the ArrayList"); 
                System.out.println("There are " + dogs2.size() + " in the ArrayList");
                
                //objects you add must be of the same data type
                dogs.add("Peanut");
                System.out.println("There are now " + dogs.size() + " dogs in the ArrayList"); 

                String myDog = dogs.get(2);
                System.out.println("My dog is named " + myDog);
            }
        }

        //Note: you don't need to declare <String> again after new ArrayList

        methodsArrayList.main(null);


Hacks:
        import java.util.ArrayList;

        ArrayList<String> color = new ArrayList<String>(); 
        color.add("red apple");
        color.add("green box");
        color.add("blue water");
        color.add("red panda");

Hack:

        ArrayList<Integer> num = new ArrayList<Integer>(); 

        num.add(5);
        num.add(1);
        num.add(3);
        
        (sum = 9)

7.5 notes:
    
* When looking at int values, the == operator should be used.
* When searching for a double value, we need to make sure the value is close enough by doing some math.
* Object instances should always use the .equals(otherThing) method to check for a match
  * selection sort: identifies min/maz of compared values

Ethical Issues of data collection:
* need good practices with data security


# CB Unit 8: 2D Iterations and Repetition

2D arrays: type of multidimensional array
- type of class, name, values

Steps:
1. initialize array
        
        int[][] numbers;
        String[][] names;
        char[][] letters;
        float[][] floats;
        double[][] doubles;
        Object[][] objects;

2. Give value by initializing 2D array

        int[][] numbers1 = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};//method 1:
        int[][] numbers2 = new int[4][3]; //method 2: Creates array with four rows and 3 columns 
        String[][] names1 = {{"John","James","Jay"},{"Melissa","May","Maggie"},{"Bob","Burt","Billy"}}; //method 1
        String[][] names2 = new String[2][2]; //method2: Creates array with 2 rows and 2 columns
        char[][] letters1 = {{'a','b','c'},{'d','e','f','g','h'}}; //method 1
        char[][] letters2 = new char[2][3]; //method 2:
        
        
(Creates array with 2 rows and 3 columns)

- Use for loop to iterate a normal array
- ex:

        String[][] alphabet = {{"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="},
        {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"},
        {"a", "s", "d", "f", "g", "h", "j", "k", "l"},
        {"z", "x", "c", "v", "b", "n", "m", ",", ".", "/"}};
    for(int i = 0;i<alphabet.length;i++){
    for(int j = 0; j < alphabet[i].length;j++){ //nested for loops
            System.out.print(alphabet[i][j]+" ");
        }
        System.out.println(" ");
    }

- change elements using indexes in 2D array
- use nested for loops to initialize values per each row/column
- ex:

            int[][]products = new int [10][10]; //creating 2D Array
            for(int i = 0;i<products.length;i++){
                for(int j = 0; j < products[i].length;j++){ 
                    products[i][j] = i*j; //initializing values for array
                }
            }

        System.out.println("Printing out values in a pattern/grid design:\n");
        for(int i = 0;i<products.length;i++){
            for(int j = 0; j < products[i].length;j++){ 
                System.out.print(products[i][j]+" ");
            }
            System.out.println(" ");
        }
        System.out.println("\nPrinting out values horizontally:\n");
        for(int i = 0;i<products.length;i++){
            for(int j = 0; j < products[i].length;j++){ 
                System.out.print(products[i][j]+" ");
            }
        }
        System.out.println("\n\nPrinting out values vertically:\n");
        for(int i = 0;i<products.length;i++){
            for(int j = 0; j < products[i].length;j++){ 
                System.out.println(products[i][j]+" ");
            }
    }


# CB Unit 9: Inheritance

Inheritance: inheriting methods/attributes via special methods/attributes; extending base classes

Super class: 
- contains all generic methods all of something would have 

Overriding Methods:
- allows subclass to provide specific methods (ex: think type of car vs “car” alone!)

        // the existing method in the superclass
            public void gearShift () {
                System.out.println("Use the stick");
            }

            public void steer () {
                System.out.println("turning left...");
            }

            // We use override to change the functionality in the subclass of an existing method in the superclass
            @Override
            public void gearShift () {
                System.out.println("Use the gear selector next to the wheel");
            }
            public void steer () {
                System.out.println("turning right...");
            }

Super Keyword: uses constructors in superclass and methods ins per class in child class
public class A public class B extends A public class C extends B

Polymorphism: doing one thing through many ways (via inheritance)

Object Superclass (via notes:)
* Object class is the superclass of all other classes in Java
* Object is part of the java.lang package (know for imports)
* Important Object class methods include: boolean equals(Object x) & String toString()
* Object class' subclasses override the equals and toString methods toString Method
* Prints out the attributes of an object
* Converts string object into a string equals Method
* Compares two strings
* Returns a boolean value of true if equal, otherwise returns false


# CB Unit 10: Recursion

Recursive method: method that calls itself
Subproblem: calls itself repeatedly
Two parts: base case, recursive call
Base case reached where recursion is stopped and value is returned

Recursion:
- recursive calls part of method
    - each lead to base case being reached
- call stacks: keep track of all times recursive function is called as well as their individual parameters
- recursions: similar to loops, could be written as loops
- iteration vs recursion:
    - iteration: used when we execute set of instructions repeatedly
    - recursion: when solution to bigger problem expressed in smaller problem terms
        - recursion = function calls
        - iteration = for/while loops

Binary Search:
- data must be stored in order, halving array until value found
- think 0(log2n) than O(n); more efficient!

Linear Recursion:
- function makes single call to itself when function runs
Selection Sort
- repeatedly finding minimum element from unsorted to sorted part
Merge Sort:
- sorts ArrayList structures, “divide and conquer” algorithm
