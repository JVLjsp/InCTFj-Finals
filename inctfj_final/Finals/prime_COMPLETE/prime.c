#include<stdio.h>
#include <stdbool.h>
#include<math.h>
#include<string.h>

bool func(int a){

	int i,f=0;
    for(i=2;i <= a/2;i++)
    {
        if(a%i == 0)
        {
            f=1;
            break;
         } 
    }
    if(f==0){
		return true;
		}
	else return false;
}
void fail(){
	printf("Try again!\n");
	return;
}

void win(char str1[],int n){
	int l3[]={61, 101, 177, 111, 240, 239, 142, 79, 173, 89, 249, 102, 27, 208, 64, 158, 237, 46, 162, 15, 190, 26, 119, 94, 14};
	int i=0,square;
	while(i<25){
			if (func(n)){
				square=pow((n),2);
				str1[i]=(((str1[i]*square)&0xff)^(l3[i]));
				i++;
				n++;
				}
			else
				n++;
			}
		str1[25]='\0';
		printf("flag is: %s\n",str1);
}

int main(){
	int list1[]={344, 1040, 1183, 2196, 9253, 10856, 17884, 38173, 52922, 42729, 48873, 82876, 259213, 250236, 366424, 427130, 112650, 114332, 125963, 851993, 0, 214813, 184720, 16942, 1929106, 205620, 90873, 148298, 394125, 187738};

	int n=2,i=0,square,cube,flag=0,j;
	char str1[30],str2[25];
	printf("Enter a string: ");
	scanf("%s",str1);
	if (strlen(str1)==30){
		while(str1[i]!='\0'){
			if (func(n)){
				square=n*n;
				cube=n*n*n;
				if (((str1[i]*square)^cube)!=list1[i]){
					flag=1;
					}
				i++;
				n++;
			}
			else
				n++;
		}	
		
		if (flag!=0){
			fail();
			return 0;
		}

		else {

			win(str1,n++);
			}
	}
	else
		printf("Try Again!\n");
	return 0;
}
		

