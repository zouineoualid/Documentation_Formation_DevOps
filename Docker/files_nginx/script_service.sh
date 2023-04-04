#!/bin/bash

# Start the first process
./nginx &
  
# Start the second process
./fcgiwrap.socket &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?
