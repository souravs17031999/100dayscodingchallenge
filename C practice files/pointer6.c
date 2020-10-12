// playing with 2d pointers arrays (matrices)

# include <stdio.h>

int main(){
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int i = 0;
    int j = 0;
    int *ptr1 = arr[0];
    int *ptr2 = arr[1];

    for(i = 0; i <= 2; i++){
        for(j = 0; j <= 2; j++){
            printf("value at arr[%i][%i] : %i\n", i, j, *ptr1);
            printf("value at arr[%i][%i] : %i\n", i, j, *ptr2);
        }
        ptr1 += 1;
        ptr2 += 1;
    }
    return 0;

}