#include<stdio.h>
#include<stdlib.h>
#include<stdio.h>

void win () { 
	puts("Great work");
	system("/bin/cat /home/gift/flag.txt");
 	puts("HO HO HO !!!");
}
void initialize()
{
  alarm(30);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){
	initialize();
	char gift[50];
 	puts("HO HO HO !!!");
	puts("Merry Christmas Losers !!!");
	gets(gift);

	return 0;
}


