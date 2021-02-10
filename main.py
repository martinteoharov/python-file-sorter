import glob
import re
from pathlib import Path

regexSlash = "([^\/]+$)"

filesCnt = 0

# args: fileLoc: location of file to move, imf: image format
def movePic(fileLoc, imf):
    target = next(_imf for _imf in location_map if _imf['type'] == imf)

    # targetLoc by default set to targetLoc
    targetLoc = target['targetLoc']

    # parse filename
    name = re.search(regexSlash, fileLoc)[0]

    # if fileLoc contains keyword in target['contains'] then redirect targetLoc to containsLoc
    if 'contains' in target:
        if name.find(target['contains']) != -1:
            targetLoc = target['containsLoc']
            print(targetLoc)
            
    # append filename to targetLoc
    targetLoc = targetLoc + '/{}'.format(name)

    # move file
    Path(fileLoc).rename(targetLoc)

    # add to total files moved
    global filesCnt
    filesCnt += 1

# maps type & keywords to targetLocations
location_map = [
            # Downloaded Pictures
            {'type': 'png', 'targetLoc': '/home/martin/Pictures/random', 'contains': 'scrot', 'containsLoc': '/home/martin/Pictures/screenshots' },
            {'type': 'jpg', 'targetLoc': '/home/martin/Pictures/random', 'contains': 'scrot', 'containsLoc': '/home/martin/Pictures/screenshots' },
            {'type': 'jpeg', 'targetLoc': '/home/martin/Pictures/random', 'contains': 'scrot', 'containsLoc': '/home/martin/Pictures/screenshots' },

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
    res = glob.glob(query)
    print('Searching for *.{}, found: {}'.format(imf, len(res)))
    for fileLoc in res:
        movePic(fileLoc, imf)

print('Total files moved: {}'.format(filesCnt))
