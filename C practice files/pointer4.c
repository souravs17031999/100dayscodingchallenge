// we can see from below that arrays are basically pointers in c 
// as declaring arrays similar to declare pointer , as we can access 
// the element using pointer[i] using array indexing 

# include <stdio.h>

int main(){
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int *ptr;
    ptr = arr;
    int i = 0;
    for (i = 0; i <= 9; i++){
        printf("value at arr[%i] : %i\n", i, ptr[i]); // here we use ptr[i] instead of arr[i] to access the element
    }
}