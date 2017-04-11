#!/bin/bash

# This script tar.gz's the source dir, and backs it up with rsync:

# variables can be over-ridden:
PROGNAME=$( basename $0)
RSYNC_EXE="rsync --password-file /home/justin/.RSYNC_PASS -avz"
TARGET=${TARGET:=justin@192.168.0.41::share}
# OPTS can be set to pass options to rsync
# Not required to set as bash will auto replace with blank if var in unset:
#OPTS=${$OPTS:-''}
SOURCE=${SOURCE:=$1}

# functions
usage (){
	echo "$PROGNAME: usage: $PROGNAME [ source directory to backup ]"
	return
}


 
rbackup () {
	$RSYNC_EXE $OPTS ${SOURCE:=$1}  $TARGET/$2
}

# main

if [[ -e $1 ]]; then
	rbackup;
else usage;
fi
