input=[0xd2d,0xdcd,0xc6c,0xe8e,0xccc,0xd4d,0xf6f,0xeee,0xcac,0xbeb,0xe8e,0xc2c,0xeae,0xcec,0xd0d,0xe8e,0xbeb,0xe8e,0xd0d,0xcac,0xdad,0xbeb,0xd0d,0xded,0xeee,0xbeb,0xe8e,0xded,0xbeb,0xc6c,0xded,0xeae,0xdcd,0xe8e,0xfaf]
a="abcdefghijklmnopqrstuvwxyz_{}"
out=[0xc2c,0xc4c,0xc6c,0xc8c,0xcac,0xccc,0xcec,0xd0d,0xd2d,0xd4d,0xd6d,0xd8d,0xdad,0xdcd,0xded,0xe0e,0xe2e,0xe4e,0xe6e,0xe8e,0xeae,0xece,0xeee,0xf0f,0xf2f,0xf4f,0xbeb,0xf6f,0xfaf]
l=""
for i in input:
	for j,k in zip(a,out):
		if i==k:
			l+=j
print l