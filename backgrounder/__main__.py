from typing import List, Optional

from os import listdir
from random import choice
import sys
import subprocess
import argparse

SET_DESKTOP_IMAGE = """/usr/bin/osascript<<END
tell application "System Events"
	set desktop_count to count of desktops
	set spaces_count to {spaces}
	set image_path to "{image_path}"

	repeat with desktop_number from 1 to spaces_count
			tell desktop desktop_count
				set picture to image_path

				if desktop_number < spaces_count then
					key code 124 using control down
					delay 1
				end if
			end tell
	end repeat
end tell
END"""


def get_image(image: str, use_random: bool) -> str:
	photos_path = "/System/Library/Desktop Pictures/"

	image_to_use = image
	if use_random:
		image_to_use = photos_path + choice(listdir(photos_path))

	return image_to_use


def set_wallpapers(spaces: int, image: str, use_random: bool) -> None:
	image_to_use = get_image(image, use_random)
	script = SET_DESKTOP_IMAGE.format(spaces=spaces, image_path=image_to_use)
	subprocess.check_call(script, shell=True)


def main(sys_args: Optional[List[str]] = None) -> int:
	if not sys_args:
		sys_args = sys.argv[1:]

	parser = argparse.ArgumentParser(
	    prog='backgrounder',
	    description='Haphazardly change desktop backgrounds.')

	parser.add_argument('-s',
	                    '--spaces',
	                    default=1,
	                    type=int,
	                    help='number of spaces to change')

	parser.add_argument('-i',
	                    '--image',
	                    action='append',
	                    help='the path to your background image')

	parser.add_argument('-r',
	                    '--random',
	                    action='store_true',
	                    help='chooses a desktop picture at random')

	args = parser.parse_args(sys_args)

	if not args.image and args.random is False:
		parser.print_help()
		sys.exit(1)

	image_path = "" if args.random else list(filter(None, args.image))[0]

	set_wallpapers(spaces=args.spaces,
	               image=image_path,
	               use_random=args.random)

	return 0


if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		pass
