// gcc -m32 -no-pie -fno-stack-protector -fno-pic chall.c -o chall

#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

void win() {
	puts("\t\tGreat work");
	system("/bin/cat /home/balls/flag.txt");
}

int get_inp(char *buffer, unsigned int len) {
	puts("Enter Your Input");
	int ret=0;
	for(int i=0; i<len; i++) {
		read(0,&buffer[i],1);
		if(buffer[i]=='\n') {
			buffer[i]='\0';
			break;
		}
		ret++;
	}
	return ret;
}

void initialize()
{
  alarm(30);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
  
  initialize();
  int size=0;
  char input[100];
  puts("\t\tStorage Device");
  puts("Enter the size of input(less than 100)");
  scanf("%d",&size);
  if(size>=100) {
    puts("Wrong size");
    exit(0);
  }
   get_inp(input,size);
   return 0;
}
