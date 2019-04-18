#!/bin/bash
for IP in 10 20 30 40 50
do
	ping -c2 192.168.99.$IP &> /dev/null && echo "SHAZAM!" || echo "BLAM!"
done 
