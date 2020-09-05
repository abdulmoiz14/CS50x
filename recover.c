#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
int main(int argc, char *argv[])
{
    unsigned char buffer[512];
	int blocksize=512;
	char filename[8];
	int counter=0;
	FILE *input = fopen(argv[1], "r");
	if(input == NULL)
	{
	    printf("Command Line Argument Error!");
	    return 1;
	}
	while(!feof(input))
	{
		fread(buffer,512,1,input);
		if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff )
	    {
	 		sprintf(filename, "%03i.jpg", counter);
        	counter ++;
			FILE* output=fopen(filename,"wb");
			fwrite(buffer,512,1,output);
			do
			{
				fread(buffer,512,1,input);
				fwrite(buffer,512,1,output);
			}while((buffer[0] == 0xff &&
                	buffer[1] == 0xd8 &&
                	buffer[2] == 0xff &&
                   (buffer[3] & 0xf0) == 0xe0) == 0);
			fclose(output);
		}
	}
	fclose(input);
}
