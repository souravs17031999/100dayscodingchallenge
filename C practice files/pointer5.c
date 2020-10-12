// We can use pointers for accessing 2d arrays in the same way as for 1-d arrays 
// nums[i][j] is equivalent to *(*(nums + i) + j)

# include <stdio.h>

int main(){
    int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int i = 0;
    int j = 0;
    for(i = 0; i <= 2; i++){
        for(j = 0; j <= 2; j++){
            printf("value at arr[%i][%i] : %i\n", i, j, arr[i][j]);
        }
    }
    printf("value of first element arr[0][0] is %i\n", *(*arr)); // this is same as arr[0][0]
    printf("value of arr[0][1] element is %i\n", *(*arr) + 1); // this is sames as arr[0][1]
    printf("value of arr[1][2] element is %i\n", *(*(arr + 1) + 2)); // this is same as arr[1][2]

    return 0;
}