// In this , we will see how pointer works on struct 
// Like arrays, pointer to a struct holds the memory address of the first 
// element in the struct 
// "->" arrow operator is used to access a value from the struct pointer 
// (*ptr).field where we first dereference the struct pointer and then 
// acess the field using the standard "." notation.
// Acessing a field from the struct pointer is so common, the "->" operator exists to make it easier  

struct person{
    int age;
    char *name;
};

#include <stdio.h>

int main(void){
    struct person first;
    struct person *ptr;
    first.age = 21;
    first.name = "sourav kumar";
    ptr = &first;
    printf("age=%d, name=%s\n", first.age, ptr->name);
    return 0;
}