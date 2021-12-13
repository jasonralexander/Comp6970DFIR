'''12-2-2021 copyright Jason Alexander and Jennifer Johnson
Project 2 COMP 6350
Professor Jason Cuneo
Auburn University
'''

#imports
import re
import hashlib

#Opening the project file
dd_file = 'Project2.dd'

#reading project file as into a python object for further manipulation
with open(dd_file, "rb") as f:
    content = f.read()
    f.close()

#Signature for BMP
BMP_SOF = b'\x42\x4D'

#creating a list of matches for Start of file signature so further work can be done to deduce if its an actual file
SOF_list = [match.start() for match in re.finditer(re.escape(BMP_SOF), content)]
EOF_list = []


if len(SOF_list) == 0:
    print("no bmp files found")
    exit()

i = 0 #counter instantiation making sure its set to 0

'''For every object in the list, we're going to be calculating the file size in little endian order and qualify it
 as a valid BMP file, '''
for index, header in enumerate(SOF_list):
    byte_offset = int(header)
    size_start = byte_offset + 2
    size_end = size_start + 4
    size_bytes = content[size_start:size_end]
    size_int = int.from_bytes(size_bytes, "little")

    reserved_section_start = byte_offset + 6
    reserved_section_end = reserved_section_start + 4
    reserved_section = int.from_bytes(content[reserved_section_start:reserved_section_end], "little")
    if (reserved_section != 0):
        continue

    file_end = byte_offset + size_int
    subdata = content[byte_offset:file_end]
    carve_filename = str(byte_offset)+""+str(file_end)+".bmp"
    carve_obj = open(carve_filename, 'wb')
    carve_obj.write(subdata)
    carve_obj.close()
    i += 1
    print("Found an bmp and carving it to " + carve_filename)

    '''
    This section will return the SHA256 hash value of the recovered file. 
    '''
    with open(carve_filename, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print("SHA256:", readable_hash,"\n")