// In this , we will learn about a custom data type that is union, which is 
// similar to struct data structure which is used to define custom data types.
// There are differences in terms of memory sharing :
// Unions have shared memory location so all the variables declared will be holding 
// same memory location whereas in struct every variable will own it's own location.
// Total memory allocated for union will be memory used for biggest data type variable
// whereas in struct memory is sum of individual storage required by variables. 
// Mostly useful in binary trees

# include <stdio.h>

union test {
    int x, y;
};
union test1 {
    int x, y;

} Test1;
union test2 {
    int x, y;

} Test2;
union test3 {
    int arr[10];
    char y;
} Test3;

union check{
    short int n;
    char ch[2];
};
// Here in the above union "check", since memory sharing will be there but since array is also involved
// so, now if we assign ch[0] = 2, ch[1] = 3.
// and then check value of n, then it will come out to be decimal form of binary 
// repr of "2""3" => since char takes 2 byte : 8 bits.
// so 8 bit repr of "2""3".

int main(){
    union test t;  // initializing the union variable 
    t.x = 2;   // here we set x part = 2
    printf("t.x = %d, t.y = %d\n", t.x, t.y);
    t.y = 10;   // even if we just change y part =10, x part will change
    printf("t.x = %d, t.y = %d", t.x, t.y);

    printf("SIZEOF(test1) : %lu, SIZEOF(test2) : %lu, SIZEOF(test1) : %lu, SIZEOF(test2) : %lu", 
    sizeof(Test1), sizeof(Test2), sizeof(Test3));

    union test p1;
    p1.x = 65;
    union test* p2 = &p1;
    printf("%d %c\n", p2->x, p2->y); 
    return 0;
    printf("\n");
    union check c1;
    c1.ch[0] = 2;
    c1.ch[1] = 3;
    printf("a : %d", c1.n);
}