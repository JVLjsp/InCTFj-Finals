echo -n "Pass= "
strings challenge.zip | tail -n 1 | cut -d":" -f2 
unzip challenge.zip
spek file.wav
