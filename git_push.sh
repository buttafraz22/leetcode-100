#!/bin/bash

# Check if the commit message is empty,
# Do NOT execute the script. Simply return.

if [ -z "$1" ]; then
   echo "Please provide a clear message of commit. Exiting with code 1."
   exit 1
fi


# There was a message, execute the script.
git add .
git commit -m "$1"
git push origin main
