from glob import *
from pathlib import Path
import re

regexSlash = "([^\/]+$)"

filesCnt = 0

def movePic(fileLoc, imf):
    targetLoc = next(_imf for _imf in location_map if _imf['type'] == imf)['targetLoc']
    name = re.search(regexSlash, fileLoc)[0]
    targetLoc = targetLoc + '/{}'.format(name)
    Path(fileLoc).rename(targetLoc)
    global filesCnt
    filesCnt += 1


location_map = [
            # Downloaded Pictures
            {'type': 'png', 'targetLoc': '/home/martin/Pictures/random'},
            {'type': 'jpg', 'targetLoc': '/home/martin/Pictures/random'},
            {'type': 'jpeg', 'targetLoc': '/home/martin/Pictures/random'},

            {'type': 'pdf', 'targetLoc': '/home/martin/pdfs'},
            {'type': 'zip', 'targetLoc': '/home/martin/zips'},

            {'type': 'epub', 'targetLoc': '/home/martin/books'},

            {'type': 'doc', 'targetLoc': '/home/martin/docs'},
            {'type': 'csv', 'targetLoc': '/home/martin/docs'},
            {'type': 'xlsx', 'targetLoc': '/home/martin/docs'},
        ]

# grab 'type' values from location_map
file_formats = [_type['type'] for _type in location_map]


for imf in file_formats:
    query = '/home/martin/Downloads/*.{}'.format(imf)
    res = glob(query)
    print('Searching for *.{}, found: {}'.format(imf, len(res)))
    for fileLoc in res:
        movePic(fileLoc, imf)


print('Total files moved: {}'.format(filesCnt))
