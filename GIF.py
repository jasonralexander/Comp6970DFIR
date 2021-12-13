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

#Signatures
GIF_SOF = b'\x47\x49\x46\x38\x39\x61'
GIF_EOF = b'\x00\x3B\x00\x00\x00'

#finding sigs and eof in content, which is the Project2 file read in via python.
SOF_list = [match.start() for match in re.finditer(re.escape(GIF_SOF), content)]
EOF_list = [match.start() for match in re.finditer(re.escape(GIF_EOF), content)]

'''This code validates that the start of a file should be less than the end of a file. EG: a file can't start at byte 100
and end at byte 98 that would be impossible. It also validates if there are more objects in the SOF list than the EOF 
list it will delete the extra false positive start of file signatures in the list'''
if len(SOF_list) != len(EOF_list):
    i = 0
    j = 0
    while i<len(EOF_list):
        if SOF_list[j] > EOF_list[i]:
            del EOF_list[i]

        if SOF_list[j] < EOF_list[i]:
            j = j+1

        i = i + 1
concat_list = []
concat_list = concat_list.append(b'x/555')

#file carving
i=0
for SOF in SOF_list:
    subdata = content[SOF:EOF_list[i]+2]
    carve_filename=str(SOF)+"_"+str(EOF_list[i])+".gif"
    print("Found GIF starting offset", str(SOF),"End offset",str(EOF_list[i]))
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    i = i + 1
    print("carving it to " + carve_filename)

#sha256 sum
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:",readable_hash,"\n")
