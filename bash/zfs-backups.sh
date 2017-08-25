#!/bin/bash

# Author: Justin Wilson
# Date: 2017-08-25
# Description: This is just a little script that backups all the zfs filesystems, and creates a tar file with the same name as the mount-point (but replaces the '/' with '-').

if [[ -z $1 ]]; then
    echo
    echo "zfs-backups:";
    echo " Usage: zfs-backup.sh [PATH TO STORE TAR BACKUP FILES ]";
    echo
else
    export TARGET=$1;
    for DIR in `zfs list | awk '{ print $5 }' | grep -v none | grep -v MOUNTPOINT`; do echo "tar cvfz /${TARGET}/$(echo $DIR | replace '/' '-').tgz $DIR"; done;
    #for DIR in `zfs list | awk '{ print $5 }' | grep -v none | grep -v MOUNTPOINT`; do tar cvfz /zfs-backups/$(echo $DIR | replace '/' '-').tgz $DIR; done;
    #echo $DIR;
fi

#    for DIR in `zfs list | awk '{ print $5 }' | grep -v none | grep -v MOUNTPOINT`; do tar cvfz /zfs-backups/$(echo $DIR | replace '/' '-').tgz $DIR; done
#     for DIR in `zfs list | awk '{ print $5 }' | grep -v none | grep -v MOUNTPOINT`; do tar cvfz /zfs-backups/$(echo $DIR | replace '/' '-').tgz $DIR; done
#fi
#
# for DIR in `zfs list | awk '{ print $5 }' | grep -v none | grep -v MOUNTPOINT`; do tar cvfz /zfs-backups/$(echo $DIR | replace '/' '-').tgz $DIR; done
