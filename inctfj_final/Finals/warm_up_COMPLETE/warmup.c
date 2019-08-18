#include<stdio.h>
#include<stdlib.h>
#include<stdio.h>
#include <unistd.h>

void win () { 
  puts("Great work");
  system("/bin/cat /home/warmup/flag.txt");
}

void initialize()
{
  alarm(30);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}


int main()
{
  initialize();
  unsigned int secret = 0xdeadbeef;
  char arr[0x500];
  scanf("%s",arr);
  if(secret!=0xdeadbeef)
    {
      win();
      exit(0);
    }
  exit(0);
}
