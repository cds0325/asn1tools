from __future__ import print_function

import os
import sys
from binascii import hexlify
from copy import deepcopy

import asn1tools

sys.path.append('project')


from parsed import EXPECTED as PARSED

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROTOCOL_PATH = os.path.realpath(os.path.join(SCRIPT_DIR,
                                                   'protocol.asn'))

pre_proc_dict=asn1tools.pre_process_dict(deepcopy(PARSED))

print("Parsing and compiling '{}' from file... ".format(PROTOCOL_PATH),
    end='',
    flush=True)

compiled=asn1tools.compile_files(PROTOCOL_PATH,'uper')

print('done.')

Message ={}

object='ProcedureCode'

encoded = compiled.encode(object,Message)
decoded = compiled.decode(object,encoded)

print(object,Message)
print('Encoded:', hexlify(encoded).decode('ascii'))
print('Decoded:', decoded)