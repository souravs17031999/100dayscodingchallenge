// understanding chain of pointers
// level of pointer is determined by number os asterisk preceding it *p is one level, **p is second level and so on 
// here, we use three level of declaration chained pointers : ptr1 is pointing to variable x, ptr2 is pointing to ptr1, ptr3 is pointing to ptr2
// dereferencing the level of pointers according to asterisk will return the same old value stored at first level of pointers unless we explicitly change it 
// if we explicitly modify the values using dereferencing , then we will get to modify the old value at the first level itself as all are chained and dereferecning 
// will take us to start level

# include <stdio.h>

int main(){
    int x = 10;
    int *ptr1 = &x;  // first level declaration 
    int **ptr2 = &ptr1; // second level declaration 
    int ***ptr3 = &ptr2; // third level declaration 
    printf("value of x  : %i\n", x);
    printf("address of x  : %p\n", &x);
    printf("value of ptr1 : %i\n", *ptr1);
    printf("value of ptr1 : %p\n", ptr1);
    printf("address of ptr1 : %p\n", &ptr1);
    printf("value of ptr2 : %p\n", ptr2);
    printf("value of ptr3 : %p\n", ptr3);

    printf("value of ptr2 : %i\n", **ptr2);
    printf("value of ptr3 : %i\n", ***ptr3);

    // now we modify one of the level's pointers -> last level 
    ***ptr3 = 50; // can also do **ptr2 = 50 will result in same effect 
    printf("value of ptr1 : %i\n", *ptr1);
    printf("value of ptr2 : %i\n", **ptr2);
    printf("value of ptr3 : %i\n", ***ptr3);
    return 0;
}