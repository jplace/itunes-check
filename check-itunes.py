import os
import sys
import argparse
import subprocess

# case-insensitive set of file extensions to classify as media
EXTENSIONS = set(['.wav', '.mp3', '.aif', '.m4a', '.m4v', '.m4r', '.m4p', '.aiff', '.mp4'])

# pointer to /dev/null
FNULL = None

def main():
	global FNULL

	parser = argparse.ArgumentParser(description="This script traverse a directory containing media files. It prints the name of any media file ffmpeg deems corrupt to stdout.")
	parser.add_argument("directory", help="The directory containing the media files to check.", type=str)
	args = parser.parse_args()
	directory = args.directory

	FNULL = open(os.devnull, 'w')
	
	process_path(directory)

"""
Input: A path to either a directory or file.
"""
def process_path(path):
	if os.path.isfile(path):
		process_file(path)
	elif os.path.isdir(path):
		for subpath in os.listdir(path):
			process_path(os.path.join(path, subpath))
	else:
		print_error("Path is not a file or directory: " + path)


"""
Input: A path to either a file.
"""
def process_file(path):
	# get file extension and normalize it
	_, extension = os.path.splitext(path)
	extension = extension.lower()

	# do nothing if this does not look like a media file
	if extension not in EXTENSIONS:
		return

	# check media file for integrity, ffmpeg will exit non-zero if the file is corrupt
	exit_status = subprocess.call(["ffmpeg", "-i", path, "-f", "null", "-"], stdout=FNULL, stderr=subprocess.STDOUT)
	if exit_status != 0:
		print path


def print_error(error_string):
	sys.stderr.write(error_string + "\n")

if __name__ == "__main__":
	main()
