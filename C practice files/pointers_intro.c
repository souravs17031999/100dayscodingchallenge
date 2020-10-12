// Pointers are basically used to reference any type of variable by storing the address of the variable
// that is it points to the specific memory address of the variable with which it is associated
// "*" operator is used when declaring a pointer and when dereferencing the pointer.
// dereferencing the pointer means getting the value stored at that address
// Size of the operator depends on architechture, for 32 bit systems : 4 bytes or 32 bits, for 64 bit systems : 8 bytes or 64 bits
// "&" operator is used to get the address of another variable , used to assign a value to a pointer
// "*" operator can also be used to assign a value to pointer address 
// Pointers declared will be of the same type as the initialised value 
// we can't tell compiler to assign a pointer of type "x" to some another variable of type "y"
// It should be always same type
// Ex. int ival = 1; int *iptr = &ival; 
// float fval = 1.0f; float *fptr = &fval;
// we can't do this : iptr = &fval;


// Pointers to arrays
// Arrays are basically valid pointers in C 
// When array is created, compiler allocates memory for the entire arrays and then assigns 
// a pointer to the arrays variable 
// we can do this : int *ptr = myarray where int myarrays[4] = {1, 2, 3, 4};
// We can't do this : myarray = ptr; myarray = myarray2; myarray = &myarray2[0] 

#include <stdio.h>

int main(void){

    return 0;
}