#!/bin/bash

# Check to make sure that user has entered exactly two arguments
if [ $# -ne 2 ]
then
	echo "Usage: backup.sh <source_directory> <target_directory>"
	echo "Please try again."
	exit 1
fi

# Check to see if rsync is installed.
if ! command -v rsync > /dev/null 2>&1
then
	echo "This script requires rsync to be installed."
	echo "Please use your distribution's package manager to install rsync and try again"
	exit 2
fi

# Capture the current date, and store it in the format YYYY-MM-DD
current_date=$(date +%Y-%m-%d)

# a is archive mode contains the metadata of file that is to be copied
# v is verboser to see output as stdout
# we would not have file replace the existing file in backup directory
# b is for creating the version of file rather than repalcing it in target directory
# --backup-dir is used to specify the backup dir which we copy file to to keep in different version in <target_dir>/<current_time>
# --delete flag is  used to make sure the clone is deleted if the file is deleted in main server to keep it sync
# --dry-run is for demo mode and remove it to run for real in production
rsync_options="-avb --backup-dir $2/$current_date --delete --dry-run"

$(which rsync) $rsync_options $1 $2/current >> backup_$current_date.log
