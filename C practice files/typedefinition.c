// typedef is used to give data type a new name.
// #define in C is a derivative which is used to #define alias 
// typedef is limited to giving symbolic names to types only, whereas 
// #define can be used to define an alias for values as well , #define 3.14 PI etc.
// typedef interpretation is performed by compiler where #define statements 
// are performed by preprocessor
// #define should not be terminated with a semicolon, but typedef should be terminated with semicolon
// #define will just copy-paste the definition values at the point of use, while 
// typedef is the actual definition of a new type 
// typedef follows the scope rule which means if a new type is defined in a scope
// then the new type name will only be visible till the scope is there.
// typedefs can be also applied to structs to avoid writing structs everytime we declare them


#include <stdio.h>

typedef struct Books{
    char title[50];
    char author[50];
    char subject[100];
    int book_id;
} BOOK;

// After this line HYD is replaced with "Hyderabad"
#define HYD "Hyderabad"

// This line BYTE can be in place of unsigned char 
typedef unsigned char BYTE;

int main(void){
    BYTE b1, b2;
    b1 = 'c';
    printf("%c ", b1);
    return 0;

    Book book;
    // used can be : book.title, book.author etc..
}