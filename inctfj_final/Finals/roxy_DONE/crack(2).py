from itertools import cycle

def xor(a,b):
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))
pc="0123456789"
pt="2d2d426567696e2d2d0a0d".decode('hex')
ct="c065c9a77e54ac8101343ea5417ae57ada7abcf62013f29d26335afa173ab626961abb9a6062f3df737d41ed043ae013bf7bfdf16b4ef1d126131ed13a0afd61".decode('hex')
for i in pc:
	for j in pc:
		for k in pc:
			for l in pc:
				for m in pc:
					x=pt+i+j+k+l+m
					key= xor(ct,x)[:16]
					flag=xor(ct,key)
					if "inctfj" in flag:
						print flag
						print i+j+k+l+m
						exit()


