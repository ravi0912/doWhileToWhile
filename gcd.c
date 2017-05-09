#include <stdio.h>

int main(void)
{
	int y1, y2, res, yout, i;
	y1 = 10;
	y2 = 545;
	res=1;
	for(i=0;y1!=y2;i++)
	{
		if(y1%2==0)
			if(y2%2==0)
			{
				res=res*2;
				y1=y1/2;
				y2=y2/2;
			}		 
		    else
				y1=y1/2;
		else if(y2%2==0)
         		y2=y2/2;
			 else if(y1>y2)
					y1=y1-y2;
				  else
					y2=y2-y1;
	}
	res=res*y1;
	yout=res;
	printf("value of a: %d\n", yout);
	return 0;

}



	
