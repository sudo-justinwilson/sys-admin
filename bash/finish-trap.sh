#!/bin/bash

# This scipt executes bash "traps", see help trap for more info:
eval $1

function finish {
	/usr/bin/wall "Task finished"
}
trap finish EXIT
