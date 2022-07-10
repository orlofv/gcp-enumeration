#! /bin/bash

if [ "$1" == "" ] 
then 
echo "Please enter IP/Network" 

else 
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d ":" -f 1 | tr -d "64 bytes from " &
done 
fi