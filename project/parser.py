
import asn1tools
import os
 
file = open( '../ASN1TOOLS/project/protocol.asn','w')
file.close()

txt =open('../ASN1TOOLS/project/protocol.txt')
for line in txt.readlines():  
    with open("../ASN1TOOLS/project/protocol.asn","a") as asn:  
        asn.write(line) 

asn_path = '../ASN1TOOLS/project/protocol.asn'
parsed = asn1tools.parse_files(asn_path)

from pprint import pformat
py_path = '../ASN1TOOLS/project/parsed.py'
with open(py_path, 'w') as fout:
    fout.write('EXPECTED = ' + pformat(parsed))

