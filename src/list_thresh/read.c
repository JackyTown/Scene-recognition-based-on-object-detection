#include <stdio.h>
#include <stdlib.h>

int readFile(double* thresh,FILE *fp)
{
	char line[100];
	if(!fp)
	{
		printf("can not load file!");
		return 0;
	}
    int count = 0;
	while(!feof(fp))
	{
		fgets(line,1000,fp);
        thresh[count] =  atof(line);
        printf("%d",count);
        printf("%f\n",thresh[count]);
        count++;
    }
    return 1;
	fclose(fp);
}

int main(){
    double thresh[80];
    FILE* fp = fopen("c.txt","r");
    int result = readFile(thresh,fp);
    return 0;
}