'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''


import re
import hashlib

dd_file = 'Project2.dd'
#read file as python object
with open(dd_file, "rb") as f:
    content = f.read()
    f.close()
#signatures
PNG_SOF = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
PNG_EOF = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF_list = [match.start() for match in re.finditer(re.escape(PNG_SOF), content)]
EOF_list = [match.start() for match in re.finditer(re.escape(PNG_EOF), content)]
#getting length to do checks for out of bounds and empty files
header_count = len(SOF_list)
footer_count = len(EOF_list)

if header_count == 0:
    exit()
#makes sure png file is of correct size/formatting
for index in range(header_count):
    if (SOF_list[index] % 512 > 0):
        continue

    file_start = int(SOF_list[index])

    footer_iterator = 0
    while EOF_list[footer_iterator] < SOF_list[index]:
        footer_iterator += 1
    file_end = int(EOF_list[footer_iterator]) + 8

    subdata = content[file_start:file_end]
    carve_filename=str(file_start)+""+str(file_end)+".png"
    print("Found PNG starting offset", str(file_start),"End offset",str(file_end))
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()

    print("carving it to " + carve_filename)
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        print("SHA256:",readable_hash,"\n")

