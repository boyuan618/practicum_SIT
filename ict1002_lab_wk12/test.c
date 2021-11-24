#include <stdio.h>
#include <stdlib.h>

FILE *f1;
char * buffer1;
long lSize1;
int main() {
    f1 = fopen("Result.tar", "rb");
    fseek (f1, 0, SEEK_END);
    lSize1 = ftell (f1);
    fseek (f1, 0, SEEK_SET);
    buffer1 = malloc(lSize1 + 1);
    if (buffer1)
    {
      fread(buffer1, 1, lSize1, f1);
    }
    printf("%s", buffer1);
    fclose(f1);
    return 0;
}