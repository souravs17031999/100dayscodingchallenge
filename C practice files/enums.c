// In this we will see uses of enum keywords in C 
// It is a user defined data type in C, used to mainly assign names to integral
// constants, the names make a program easy to read and maintain.
// enum is used to declare new declare new enumeration types, 
// name of enumeration is "flag" and constant are the values of the flag 
// constant1 = 0, constant2 = 1, ...etc.
// enum flag{constant1, constant2....}
// Compiler assigns values starting from 0.
// All enum constants must be unique in their scope
// Following fails : 
// enum state {working, failed};
// enum result {failed, passed};
// Macros can also be defined for assigning constant values, but enums differ and have advantages 
// * enums follow scope rules
// * enum variables are automatically assigned values.

# include <stdio.h>

enum week{Mon, Tue, Wed, Thur, Fri, Sat, Sun}; 
enum year{Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec};
// we can also initialize values from user defined constants : 
// enum week{Mon = 1, Tue, Wed, Thur, Fri, Sat, Sun}; this will start counting from 1..



int main(void){
    enum week day;
    day  = Wed;  // This shows Wed is a constant defined now 
    printf("value of wed : %d\n", day);
    int i = 0;
    printf("Value of constants Jan to Dec: \n");
    for(i = Jan; i <= Dec; i++){
        printf("%d ", i);
    }

    return 0;

}