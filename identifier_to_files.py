import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys
from datetime import datetime


def main():

	parser = argparse.ArgumentParser(description="This adds an identifier to the name of all files in a folder")
	parser.add_argument('-x', nargs='?', type=str, help="folder with the files", required=True)
	parser.add_argument('-i', nargs='?', type=str, help="identifier", required=True)

	args = parser.parse_args()

	renameFiles(args)

def renameFiles(args):
	onlyfiles = [ f for f in listdir(args.x) if isfile(join(args.x,f)) ]

	for i in onlyfiles:
		fullPath = os.path.join(args.x, i)
		nameNoExtension = os.path.splitext(i)
		newFullPath = os.path.join(args.x, nameNoExtension[0] + '_' + args.i + nameNoExtension[1])
		
		os.rename(fullPath, newFullPath)

if __name__ == "__main__":
	main()