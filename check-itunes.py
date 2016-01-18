import os
import sys
import argparse

EXTENSIONS = set()

def main():
	parser = argparse.ArgumentParser(description="This script traverse a directory containing media files. It prints the name of any media file ffmpeg deems corrupt to stdout.")
	parser.add_argument("directory", help="The directory containing the media files to check.", type=str)
	args = parser.parse_args()
	directory = args.directory
	
	process_path(directory)
	print EXTENSIONS

"""
Input: A path to either a directory or file.
"""
def process_path(path):
	if os.path.isfile(path):
		_, extension = os.path.splitext(path)
		EXTENSIONS.add(extension)
	elif os.path.isdir(path):
		for subpath in os.listdir(path):
			process_path(subpath)
	else:
		print >> sys.stderr "Path is not a file or directory: " + path

if __name__ == "__main__":
	main()
