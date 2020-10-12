// In this, we will learn about malloc, calloc and free methods usage
// malloc() and calloc() are library functions that allocate memory dynamically
// It means that memory is allocated during runtime from the heap segment 
// malloc() doesn't initialize the allocated memory
// if we try to access the content of memroy block, then we will get segmentation error (or maybe garbage values)
// calloc() allocates the memory and also initialises the allocated memory block to zero.
// void* malloc(size_t size);
// void* calloc(size_t num, size_t size);
// NOTE : malloc is faster and better to use than calloc
// if memory is not allocated succesfully, then it fails and returns NULL pointer
// When memory allocation is done, the actual heap space allocated is one word 
// larger than the requested memory. The extra word is used to store the 
// sze of the allocation and is later used by free().
// realloc() is used to dynamically change the memory allocation of previously 
// allocated memory. if previous memory is unsufficient, realloc can be dynamically re-allocate 
// memory , it maintains the already present value and new blocks will be initialized
// with default garbage value.

#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *arr;

    // malloc() allocate the memory for 5 integers 
    // containing garbage values
    arr = (int*)malloc(5 * sizeof(int)); // 5 * 4 = 20bytes
    // deallocates the memory previously allocated by malloc() function
    printf("first block : %d, second block : %d, third block : %d, fourth block : %d, fifth block : %d", arr[0], arr[1], arr[2], arr[3], arr[4]);

    free(arr);
    // calloc() allocate the memory for 5 integers and 
    // set 0 to all of them 
    arr = (int*)calloc(5, sizeof(int));
    free(arr);

    return 0;
}