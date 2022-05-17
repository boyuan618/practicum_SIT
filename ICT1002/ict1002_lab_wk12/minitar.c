#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *f1;
FILE *f2;
FILE *tar_file;

#define  RECORDSIZE  512 
#define  NAMSIZ      100 
#define  TUNMLEN      32 
#define  TGNMLEN      32 

struct header {     
    char    name[NAMSIZ];     
    char    mode[8];     
    char    uid[8];     
    char    gid[8];     
    char    size[12];    
    char    mtime[12];     
    char    chksum[8];     
    char    linkflag;     
    char    linkname[NAMSIZ];     
    char    magic[8];     
    char    uname[TUNMLEN];     
    char    gname[TGNMLEN];     
    char    devmajor[8]; 
    char    devminor[8]; 
};

typedef struct header HEADER;


int main(int argc, char **argv) {
    long lSize1, lSize2, total;
    char * buffer1;
    char * buffer2;
    size_t result1; 
    size_t result2;   
    HEADER header1, header2;
    
    //File1
    f1 = fopen(argv[1], "rb");
    fseek (f1, 0, SEEK_END);
    lSize1 = ftell (f1);
    fseek (f1, 0, SEEK_SET);
    buffer1 = malloc(lSize1 + 1);
    if (buffer1)
    {
      result1 = fread(buffer1, 1, lSize1, f1);
    }
    fclose(f1);
    buffer1[lSize1] = '\0';
    //printf("File1: %s\n", buffer1);
    
    //File2
    f2 = fopen(argv[2], "rb");
    fseek (f2, 0, SEEK_END);
    lSize2 = ftell (f2);
    fseek (f2, 0, SEEK_SET);
    buffer2 = malloc(lSize2 + 1);
    if (buffer2)
    {
      result1 = fread(buffer2, 1, lSize2, f2);
    }
    fclose(f2);
    buffer1[lSize2] = '\0';
    //printf("File2: %s", buffer2);
    
    //Setting the headers
    sprintf(header1.size, "%ld", lSize1+1);
    sprintf(header2.size, "%ld", lSize2+1);
    strcpy(header1.name, argv[1]);
    strcpy(header2.name, argv[2]);

    //Writing to .tar file
    tar_file = fopen("Result.tar", "wb");

    fwrite(&header1, sizeof(struct header), 1, tar_file);
    fwrite(buffer1, strlen(buffer1), 1, tar_file);

    fwrite(&header2, sizeof(struct header), 1, tar_file);
    fwrite(buffer2, strlen(buffer2), 1, tar_file);

    fclose(tar_file);
    return 0;
}