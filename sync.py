#!/usr/bin/env python3
import argparse

from livesync import Folder, sync  # type: ignore
from livesync.run_subprocess import run_subprocess  # type: ignore

parser = argparse.ArgumentParser(description='Sync local code with robot.')
parser.add_argument('robot', help='Robot hostname')
parser.add_argument('--rosys', action='store_true', default=False, help='Sync rosys')

args = parser.parse_args()
touch = 'touch ~/test_brain/main.py'
folders = [Folder('.', f'{args.robot}:~/test_brain', on_change=touch)]
if args.rosys:
    folders.append(Folder('../rosys/rosys', f'{args.robot}:~/test_brain/rosys', on_change=touch))
else:
    print('Ensuring we have no local rosys on the robot')
    run_subprocess(f'ssh {args.robot} "rm -rf ~/test_brain/rosys"')

sync(*folders)
