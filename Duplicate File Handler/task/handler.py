import sys
import os

args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
    sys.exit(0)
req_dir = args[1]

os.chdir(req_dir)
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
