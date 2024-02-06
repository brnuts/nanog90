#include <stdio.h>
#include <time.h>

int main() {
    int start = 1000000000;

    clock_t start_time = clock();

    while (start > 0) {
        start--;
    }

    clock_t end_time = clock();
    double elapsed_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Blast off! Elapsed time: %f seconds\n", elapsed_time);

    return 0;
}

