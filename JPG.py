'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''

import re
import hashlib

dd_file = 'Project2.dd'

with open(dd_file, "rb") as f:
    content = f.read()
    f.close()

#signatures
JPEG_SOF = b'\xFF\xD8\xFF\xE0' #or b'\xFF\xD8\xFF\xDB'
JPEG_SOF2 = b'\xFF\xD8\xFF\xDB'
JPEG_EOF = b'\xFF\xD9\x00\x00\x00'

#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF1_list = [match.start() for match in re.finditer(re.escape(JPEG_SOF), content)]
SOF2_list =[match.start() for match in re.finditer(re.escape(JPEG_SOF2), content)]
EOF_list = [match.start() for match in re.finditer(re.escape(JPEG_EOF), content)]

SOF_list = []
i=0
while(i<len(SOF1_list)):
    SOF_list.append(SOF1_list[i])
    i+=1

i=0
while(i<len(SOF2_list)):
    if SOF1_list.__contains__(SOF2_list[i]):
        continue
    else:
            SOF_list.append(SOF2_list[i])
    i+=1

#sorting the file to prepare it like all the others, to make sure offsets aren't out of bounds with each other.
SOF_list.sort()
EOF_list.sort()


'''This code validates that the start of a file should be less than the end of a file. EG: a file can't start at byte 100
and end at byte 98 that would be impossible. It also validates if there are more objects in the SOF list than the EOF 
list it will delete the extra false positive start of file signatures in the list'''

if len(SOF_list) != len(EOF_list):
    i = 0
    while i<len(EOF_list):
        if SOF_list[i]>EOF_list[i]:
            del EOF_list[i]
        i = i + 1

#file carving
i = 0
for SOF in SOF_list:
    subdata=content[SOF:EOF_list[i]+2]
    carve_filename=str(SOF)+"_"+str(EOF_list[i])+".jpg"
    print("Found JPG starting offset", str(SOF), "End offset", str(EOF_list[i]))
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    i = i + 1
    print("carving it to " + carve_filename)
#sha256 sum
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:", readable_hash,"\n")
