from __future__ import print_function

import sys
import asn1tools
from copy import deepcopy
from binascii import hexlify
import os

sys.path.append('project/files')
sys.path.append('project/files/F1AP')
sys.path.append('project/files/E2AP')

from F1AP_IEs import EXPECTED as F1AP_IEs

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
F1AP_IEs_PATH = os.path.realpath(os.path.join(SCRIPT_DIR,
                                                   '..',
                                                   'project',
                                                   'files',
                                                   'F1AP',
                                                   'F1AP_IEs.asn'))

pre_proc_dict=asn1tools.pre_process_dict(deepcopy(F1AP_IEs))

print("Parsing and compiling '{}' from file... ".format(F1AP_IEs_PATH),
    end='',
    flush=True)

compiled=asn1tools.compile_files(F1AP_IEs_PATH,'uper')

print('done.')

Message =3

object='ProcedureCode'

encoded = compiled.encode(object,Message)
decoded = compiled.decode(object,encoded)

print(object,Message)
print('Encoded:', hexlify(encoded).decode('ascii'))
print('Decoded:', decoded)