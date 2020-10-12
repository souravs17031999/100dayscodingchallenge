// NULL pointers 
// It is different from uninitialised and dangling pointer.
// It's a specific valid "invalid" pointer in C standard 
// An integer constant expression with the value 0, or such an expression cast to type void *, is called a null pointer constant. \
// If a null pointer constant is converted to a pointer type, the resulting pointer, called a null pointer, is guaranteed to compare unequal to a pointer to any object or function.”
// NULL is basically 0 but not in integer context , it's in pointer context
// Sizeof() is valid and is of pointer's normal size

# include <stdio.h>

int main(){
    int *ptr = NULL; // it is perfectly valid to be written as int *ptr = 0;
    printf("value of ptr : %p\n", ptr);
    printf("sizeof of ptr : %i\n", sizeof(ptr));
    // we can also dereference the NULL pointer
    printf("value of dereference : %d", *ptr);
}