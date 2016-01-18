import os
import sys
import argparse
import subprocess
import multiprocessing
import time
from contextlib import contextmanager
import itertools

# case-insensitive set of file extensions to classify as media
EXTENSIONS = set(['.wav', '.mp3', '.aif', '.m4a', '.m4v', '.m4r', '.m4p', '.aiff', '.mp4'])

# pointer to /dev/null
FNULL = None


def main():
	global FNULL

	parser = argparse.ArgumentParser(description="This script prints the names of any media file ffmpeg deems corrupt to stdout.")
	parser.add_argument("path", help="A file or directory referencing media files to check", type=str)
	args = parser.parse_args()
	path = args.path

	FNULL = open(os.devnull, 'w')

	with measureTime("file processing"):
		# if just a file path has been provided, put it in a list
		# otherwise, chain iterables
		files = None
		if os.path.isfile(path):
			files = [path]
		elif os.path.isdir(path):
			walk = os.walk(path)
			files = itertools.chain.from_iterable((os.path.join(root, file) for file in files) for root, dirs, files in walk)
		else:
			print_error("Path is not a file or directory: " + path)
			sys.exit(1)

		# process all retrieved files
		multiprocessing.Pool(5).map(process_file, files)


"""
Input: A path to a file to check for integrity
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


@contextmanager
def measureTime(title):
	t1 = time.time()
	yield
	t2 = time.time()
	sys.stderr.write('%s: %0.2f seconds elapsed\n' % (title, t2-t1))


if __name__ == "__main__":
	main()
