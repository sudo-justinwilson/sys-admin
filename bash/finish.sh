#!/bin/bash

# This scipt executes bash "traps", see help trap for more info:
eval $1

function finish {
# you can put any arbitrary code in the following line, that you want to be executed when the process exits. Here I send a message to wall:
	/usr/bin/wall "Task finished"
}
trap finish EXIT
