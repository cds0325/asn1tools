from __future__ import print_function

import os
import sys
from binascii import hexlify
from copy import deepcopy

import asn1tools

sys.path.append('tests/files')
sys.path.append('tests/files/ietf')
sys.path.append('tests/files/3gpp')

from rrc_8_6_0 import EXPECTED as RRC_8_6_0

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RRC_8_6_0_PATH = os.path.realpath(os.path.join(SCRIPT_DIR,
                                                   '..',
                                                   'tests',
                                                   'files',
                                                   '3gpp',
                                                   'rrc_8_6_0.asn'))

pre_proc_dict=asn1tools.pre_process_dict(deepcopy(RRC_8_6_0))

print("Parsing and compiling '{}' from file... ".format(RRC_8_6_0_PATH),
    end='',
    flush=True)

compiled=asn1tools.compile_files(RRC_8_6_0_PATH,'uper')

print('done.')

DRB_CountInfo = {'drb-Identity':1,'count-Uplink':3,'count-Downlink':5 }

encoded = compiled.encode('DRB-CountInfo',DRB_CountInfo)
decoded = compiled.decode('DRB-CountInfo',encoded)

print('DRB-CountInfo',DRB_CountInfo)
print('Encoded:', hexlify(encoded).decode('ascii'))
print('Decoded:', decoded)

