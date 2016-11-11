#!/bin/sh

while IFS='' read -r line || [[ -n "$line" ]]; do
	newpath=`echo "$line" | sed -e 's|BAYSIDE|THEMAX/BAYSIDE|g'`
	if [[ ! -e "$newpath" ]]; then
		echo "File $newpath does not exist!"
	fi
	cp "$newpath" found/
done < "results"
