#include<stdio.h>

int jumpingOnClouds(int len, int arr[]) {
    int pos = 0;
    int num_jumps = 0;

    while (pos < len) {
        if (pos == len - 1) {
            break;
        }

        if (pos == len - 2) {
            if (arr[pos + 1] == 0) {
                num_jumps++;
                break;
            } else {
                break;
            }
        }

        if (arr[pos + 2] == 0) {
            pos += 2;
            num_jumps++;
        } else {
            pos += 1;
            num_jumps++;
        }

    }

    return num_jumps;
}

int main() {
    int arr1[] = {0, 1, 0, 0, 0, 1, 0};
    printf("%d\n", jumpingOnClouds(7, arr1));

    int arr2[] = {0, 0, 0, 1, 0, 0};
    printf("%d\n", jumpingOnClouds(6, arr2));

}