#include<stdio.h>
int is_prime(int n)
{
  if(n <=1)
  {
    return 0;
  }
  for(int i=2;i<=n/2;i++)
  {
    if(n % i == 0)
    {
      return 0;
    }
  }
  return 1;
}
int nth_prime(int n)
{
  int count=0,i=2;
  while(count<n)
  {
    if(is_prime(i))
    {
      count++;
    }
    if(count == n)
    {
      printf("%d\n",i);
    }
    i++;
  }
  return 0;
}
int main()
{
  nth_prime(10000);
  return 0;
}
