#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
int main(int argc, char *argv[])
{
    unsigned char buffer[512];
	int blocksize=512;
	char filename[8];
	int counter=0;
	bool jpeg_found = false;
	FILE* output=NULL;
	FILE *input = fopen(argv[1], "r");
	if(input == NULL)
	{
	    printf("Command Line Argument Error!");
	    return 1;
	}
	while(fread(buffer,512,1,input))
	{
		if(buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff )
	    {
	    	if(jpeg_found==true)
	    	{
	    		fclose(output);
	    	}
	    	else
	    	{
	    		jpeg_found=true;
	    	}
	 		sprintf(filename, "%03i.jpg", counter);
        	counter ++;
			output=fopen(filename,"w");
			fwrite(buffer,512,1,output);
		}
		else if(jpeg_found==true)
		{
			fwrite(buffer,512,1,output);
		}
	}
	fclose(input);
}
