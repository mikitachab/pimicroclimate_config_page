#!/bin/bash

#user input for SSID
#echo "Enter a SSID for wifi"
#read SSID
#echo "Enter a password for $SSID network"
#read -s PASSWORD
SSID=$1
PASSWORD=$2
#creating a config file for network
if [ ${#PASSWORD} -lt 8 ] || [ ${#PASSWORD} -gt 64 ]
then
	echo "Bad password lenght"
else
	if [ -f /etc/wpa_supplicant/wpa_supplicant.conf ]
	then
		wpa_passphrase $SSID $PASSWORD | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf >>/dev/null
	else
		wpa_passphrase $SSID $PASSWORD | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null
	fi
	#inteface set up and start
	INTERFACE=`iw dev | grep -o "Interface.*"| cut -d' ' -f2`
	sudo ip link set $INTERFACE up
	sudo wpa_cli -i $INTERFACE reconfigure
	sudo dhclient $INTERFACE
	STATUS=`iw $INTERFACE link | grep -o "Connected"`
	#connection status
	if [ $STATUS != "Connected" ]
	then
		echo "Error. Not connected."
	else
		echo "Success."
	fi

fi

