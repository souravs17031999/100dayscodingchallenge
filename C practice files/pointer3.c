// understanding pointer arithmetic 
// Pointers can be incremented, decremented , 
// and a integer may be added or subtracted using += , -=}

#include <stdio.h>

int main(){
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // array declaration in c 
    int n = sizeof(arr)/sizeof(arr[0]); // finding the size of array 
    int i = 0;  // for loop variables outside the loop 
    int *ptr; // declaring the pointer variable 
    ptr = arr;  // pointing this will make ptr to point to first allocated space 
    for (i = 0; i <= n - 1; i++){ // iterable loop
        printf("value at arr[%i] = %i at %p\n", i, *ptr, ptr);  
        ptr += 1;  // incrementing the pointer will point to next contigous location 
    }
    return 0;
}