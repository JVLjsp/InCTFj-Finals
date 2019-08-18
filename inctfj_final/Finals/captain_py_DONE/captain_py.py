import string	
import random

def checky(st1,st2):
	print(((st1[::-1]+st2[::-1]).center(80,'*')))


def func1(s,t):
	k=[88, 22, 68, 87, 106, 89, 115, 22, 92, 96, 111, 107, 89, 104, 115, 110, 98, 115, 21, 88, 25, 106, 88, 68, 94, 94, 95, 25, 113, 68, 25, 68]
	s1=''
	s2=''
	for i in range(len(s)):
		s1=s1+chr(ord(s[i])^16) 					
	for i in range(len(t)):
		s2=s2+chr(ord(t[i])^16) 					

	 			
	p=s1+s2
	
	
	if(len(p)==32 and ''.join(sorted(p))==" !!$$$OOOObcccddgiijkmsuuvyz|~~~"):		
		
		i=0
		while(i>=0 and i<32):
			if(k[i]==ord(p[i])-11):
				i=i+1
			else:
				i=i-1
		if(i==32):
			checky(s,t)
		else:
			print("Try Again!!")	
	else:
		print("N0p....Try harder!!")	
		
		

st1=input()	
st2=input()	
func1(st1,st2)


	

	
	

	


