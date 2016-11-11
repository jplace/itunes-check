#!/bin/sh

while IFS='' read -r line || [[ -n "$line" ]]; do
	filename=`basename "$line"`
	oldpath="$line"
	newpath="found/$filename"
	if [[ ! -e "$newpath" ]]; then
		echo "File $newpath does not exist!"
	fi
	cp "$newpath" "$oldpath"
done < "results"
