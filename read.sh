#!/bin/bash

#Move to 'chat' folder and display the files  
cd chats
ls

#Enter the chat you want to enter
echo "Enter the name of the chat you want to view."
echo "->"
read file_name
cat $file_name
