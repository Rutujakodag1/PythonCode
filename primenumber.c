include <stdio.h>
//Prime number between 1 to n:
int main(void)
{
int i,j,count,a;
printf("Enter the number:");
scanf("%d",&a);
printf("\n\tPrime numbers between 1 to %d",a);
printf("\n");
  for(i=1;i<=a;i++)
    {
      count=0;
      for(j=1;j<=i;j++)
        {
          if(i%j==0)
          {
            count++;
          }
        }
    if(count==2)
    {
      printf("\n%d",i);
    }
    }
  return 0;
}
