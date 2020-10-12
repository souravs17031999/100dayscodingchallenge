// Dangling pointer
// It is different from NULL whereas NULL is specific but dangling is not
// There is also concept of wild pointers which is basically those ppinters 
// which are not initialized to anywhere
// Void pointers are a type pointer, they are basically pointing to some valid storage but 
// type of data is not clear 
// Pointer arithmetic can't be done on Void pointers but it can typecasted in some known data type 


# include <stdio.h>
# include <stdlib.h>

// this function is returning address of variable so we use int * as return type 

int *fun()
{
    int x = 5;
    return &x;
}

int *fun1()
{
    static int x = 5;
    return &x;
}


int main(){
    // Ist case
    // dynamic memory allocation in C 
    int *ptr = (int *)malloc(sizeof(int));
    free(ptr);  // freeing the memory

    // ptr is now dangling as we don't know where it is pointing to

    printf("value of ptr : %p\n", ptr);

    ptr = NULL;

    printf("value of ptr : %p\n", ptr);

    // 2nd case 
    // when the local variable goes out of x after execution of fun() is over 
    int *p = fun();
    fflush(stdin);
    printf("%d\n", *p);

    // when we declare static keyword infront of local variable then it is known to the whole 
    // program and becomes global in the sense 

    int *p1 = fun1();
    fflush(stdin);
    printf("%d\n", *p1);

    return 0;


}