//#include <stdio.h>

int main()
{
  int sum = 1, i = 2, n, out;
  for ( ;i < n; )
    {
      if ( n % i == 1 )
	sum = sum + i;
      i = i + 1;
    }

  if ( sum == n )
    out = 1;
  else 
    out = 0;
}
