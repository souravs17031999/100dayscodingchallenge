// In this we will see dereference operators "*", prefix (++p) and postfix operators (p++) precedence
// precedence of prefix ++ and * is same , associativity is right to left 
// precedence of postfix ++ is higher than * , associativity is left to right  

#include <stdio.h>

int main(void){
    int arr[] = {10, 20};
    int *p = arr;
    ++*p;  // here compiler compiles in the following way : ++(*p) so *p is 10 and ++*p will be *p = *p + 1 => 10 + 1 => 11
    printf("arr[0] = %d, arr[1] = %d, *p = %d", arr[0], arr[1], *p);

    int s[] = {10, 20};
    int *r = s;
    *r++; // here compiler compiles in the following way : *(r++) so r++ is r = r + 1, which will point to address of 20, so now *r will be 20
    printf("\ns[0] = %d, s[1] = %d, *r = %d", s[0], s[1], *r);

    return 0;
}