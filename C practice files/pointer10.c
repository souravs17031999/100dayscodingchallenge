// understanding Function pointers 
// function pointers don't point to data, but only to code  
// This can be also be used in place of switch case - point 1
// This can be also be passed as argument in function and returned from function - point 2
//

# include <stdio.h>

void fun(int a){
    printf("Value of a is %d\n", a);
}

int main(){
    void (*fun_ptr)(int) = &fun;  // here fun_ptr is a pointer to function fun()

    (*fun_ptr)(10);  // extra brackets is required to call this function 
     
    // can also be written as with removing & operator and calling funtion withut * operator 

    void (*fun_ptr1)(int) = fun;

    fun_ptr1(10);

    return 0;

    // point - 1

    // creating a array of pointers using function pointers 

    void (*fun_ptr_arr[])(int, int) = {add, subtract, multiply};
    // here add, subtract and multiply are all different functions 
}