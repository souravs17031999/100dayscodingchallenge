// Initialising the pointer with a unary pointer "*" before its name
// "*" before a name makes it a pointer variable which stores address of 
// another variable 

// Another use of * operator is to dereferencing that is 
// getting the actual value stored in pointer.
// Pointer points to the value and stores the address of that value.

#include <stdio.h>
int main(){
    int x = 5;
    int *ptr;
    ptr = &x;

    printf("value Of x = %i : and stored at  = %p\n", *ptr, ptr);

    // we can change the value stored at the address this pointer points to
    *ptr = 20;
    printf("value Of x = %i : and stored at  = %p", *ptr, ptr);
    return 0;
}

