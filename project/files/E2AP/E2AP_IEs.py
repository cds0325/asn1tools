EXPECTED = {'E2AP-IEs': {'extensibility-implied': False,
              'imports': {'E2AP-CommonDataTypes': ['Criticality',
                                                   'Presence',
                                                   'ProcedureCode',
                                                   'ProtocolIE-ID',
                                                   'TriggeringMessage'],
                          'E2AP-Constants': ['maxProtocolIEs',
                                             'maxnoofErrors']},
              'object-classes': {},
              'object-sets': {},
              'tags': 'AUTOMATIC',
              'types': {'AMFName': {'size': [(1, 150), None],
                                    'type': 'PrintableString'},
                        'Cause': {'members': [{'name': 'ricRequest',
                                               'type': 'CauseRICrequest'},
                                              {'name': 'ricService',
                                               'type': 'CauseRICservice'},
                                              {'name': 'e2Node',
                                               'type': 'CauseE2node'},
                                              {'name': 'transport',
                                               'type': 'CauseTransport'},
                                              {'name': 'protocol',
                                               'type': 'CauseProtocol'},
                                              {'name': 'misc',
                                               'type': 'CauseMisc'},
                                              None],
                                  'type': 'CHOICE'},
                        'CauseE2node': {'type': 'ENUMERATED',
                                        'values': [('e2node-component-unknown',
                                                    0),
                                                   None]},
                        'CauseMisc': {'type': 'ENUMERATED',
                                      'values': [('control-processing-overload',
                                                  0),
                                                 ('hardware-failure', 1),
                                                 ('om-intervention', 2),
                                                 ('unspecified', 3),
                                                 None]},
                        'CauseProtocol': {'type': 'ENUMERATED',
                                          'values': [('transfer-syntax-error',
                                                      0),
                                                     ('abstract-syntax-error-reject',
                                                      1),
                                                     ('abstract-syntax-error-ignore-and-notify',
                                                      2),
                                                     ('message-not-compatible-with-receiver-state',
                                                      3),
                                                     ('semantic-error', 4),
                                                     ('abstract-syntax-error-falsely-constructed-message',
                                                      5),
                                                     ('unspecified', 6),
                                                     None]},
                        'CauseRICrequest': {'type': 'ENUMERATED',
                                            'values': [('ran-function-id-invalid',
                                                        0),
                                                       ('action-not-supported',
                                                        1),
                                                       ('excessive-actions', 2),
                                                       ('duplicate-action', 3),
                                                       ('duplicate-event-trigger',
                                                        4),
                                                       ('function-resource-limit',
                                                        5),
                                                       ('request-id-unknown',
                                                        6),
                                                       ('inconsistent-action-subsequent-action-sequence',
                                                        7),
                                                       ('control-message-invalid',
                                                        8),
                                                       ('ric-call-process-id-invalid',
                                                        9),
                                                       ('control-timer-expired',
                                                        10),
                                                       ('control-failed-to-execute',
                                                        11),
                                                       ('system-not-ready', 12),
                                                       ('unspecified', 13),
                                                       None]},
                        'CauseRICservice': {'type': 'ENUMERATED',
                                            'values': [('ran-function-not-supported',
                                                        0),
                                                       ('excessive-functions',
                                                        1),
                                                       ('ric-resource-limit',
                                                        2),
                                                       None]},
                        'CauseTransport': {'type': 'ENUMERATED',
                                           'values': [('unspecified', 0),
                                                      ('transport-resource-unavailable',
                                                       1),
                                                      None]},
                        'CriticalityDiagnostics': {'members': [{'name': 'procedureCode',
                                                                'optional': True,
                                                                'type': 'ProcedureCode'},
                                                               {'name': 'triggeringMessage',
                                                                'optional': True,
                                                                'type': 'TriggeringMessage'},
                                                               {'name': 'procedureCriticality',
                                                                'optional': True,
                                                                'type': 'Criticality'},
                                                               {'name': 'ricRequestorID',
                                                                'optional': True,
                                                                'type': 'RICrequestID'},
                                                               {'name': 'iEsCriticalityDiagnostics',
                                                                'optional': True,
                                                                'type': 'CriticalityDiagnostics-IE-List'},
                                                               None],
                                                   'type': 'SEQUENCE'},
                        'CriticalityDiagnostics-IE-Item': {'members': [{'name': 'iECriticality',
                                                                        'type': 'Criticality'},
                                                                       {'name': 'iE-ID',
                                                                        'type': 'ProtocolIE-ID'},
                                                                       {'name': 'typeOfError',
                                                                        'type': 'TypeOfError'},
                                                                       None],
                                                           'type': 'SEQUENCE'},
                        'CriticalityDiagnostics-IE-List': {'element': {'type': 'CriticalityDiagnostics-IE-Item'},
                                                           'size': [(1,
                                                                     'maxnoofErrors')],
                                                           'type': 'SEQUENCE '
                                                                   'OF'},
                        'E2nodeComponentConfiguration': {'members': [{'name': 'e2nodeComponentRequestPart',
                                                                      'type': 'OCTET '
                                                                              'STRING'},
                                                                     {'name': 'e2nodeComponentResponsePart',
                                                                      'type': 'OCTET '
                                                                              'STRING'},
                                                                     None],
                                                         'type': 'SEQUENCE'},
                        'E2nodeComponentConfigurationAck': {'members': [{'name': 'updateOutcome',
                                                                         'type': 'ENUMERATED',
                                                                         'values': [('success',
                                                                                     0),
                                                                                    ('failure',
                                                                                     1),
                                                                                    None]},
                                                                        {'name': 'failureCause',
                                                                         'optional': True,
                                                                         'type': 'Cause'},
                                                                        None],
                                                            'type': 'SEQUENCE'},
                        'E2nodeComponentID': {'members': [{'name': 'e2nodeComponentInterfaceTypeNG',
                                                           'type': 'E2nodeComponentInterfaceNG'},
                                                          {'name': 'e2nodeComponentInterfaceTypeXn',
                                                           'type': 'E2nodeComponentInterfaceXn'},
                                                          {'name': 'e2nodeComponentInterfaceTypeE1',
                                                           'type': 'E2nodeComponentInterfaceE1'},
                                                          {'name': 'e2nodeComponentInterfaceTypeF1',
                                                           'type': 'E2nodeComponentInterfaceF1'},
                                                          {'name': 'e2nodeComponentInterfaceTypeW1',
                                                           'type': 'E2nodeComponentInterfaceW1'},
                                                          {'name': 'e2nodeComponentInterfaceTypeS1',
                                                           'type': 'E2nodeComponentInterfaceS1'},
                                                          {'name': 'e2nodeComponentInterfaceTypeX2',
                                                           'type': 'E2nodeComponentInterfaceX2'},
                                                          None],
                                              'type': 'CHOICE'},
                        'E2nodeComponentInterfaceE1': {'members': [{'name': 'gNB-CU-CP-ID',
                                                                    'type': 'GNB-CU-UP-ID'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceF1': {'members': [{'name': 'gNB-DU-ID',
                                                                    'type': 'GNB-DU-ID'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceNG': {'members': [{'name': 'amf-name',
                                                                    'type': 'AMFName'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceS1': {'members': [{'name': 'mme-name',
                                                                    'type': 'MMEname'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceType': {'type': 'ENUMERATED',
                                                         'values': [('ng', 0),
                                                                    ('xn', 1),
                                                                    ('e1', 2),
                                                                    ('f1', 3),
                                                                    ('w1', 4),
                                                                    ('s1', 5),
                                                                    ('x2', 6),
                                                                    None]},
                        'E2nodeComponentInterfaceW1': {'members': [{'name': 'ng-eNB-DU-ID',
                                                                    'type': 'NGENB-DU-ID'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceX2': {'members': [{'name': 'global-eNB-ID',
                                                                    'optional': True,
                                                                    'type': 'GlobalENB-ID'},
                                                                   {'name': 'global-en-gNB-ID',
                                                                    'optional': True,
                                                                    'type': 'GlobalenGNB-ID'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'E2nodeComponentInterfaceXn': {'members': [{'name': 'global-NG-RAN-Node-ID',
                                                                    'type': 'GlobalNG-RANNode-ID'},
                                                                   None],
                                                       'type': 'SEQUENCE'},
                        'ENB-ID': {'members': [{'name': 'macro-eNB-ID',
                                                'size': [20],
                                                'type': 'BIT STRING'},
                                               {'name': 'home-eNB-ID',
                                                'size': [28],
                                                'type': 'BIT STRING'},
                                               None,
                                               {'name': 'short-Macro-eNB-ID',
                                                'size': [18],
                                                'type': 'BIT STRING'},
                                               {'name': 'long-Macro-eNB-ID',
                                                'size': [21],
                                                'type': 'BIT STRING'}],
                                   'type': 'CHOICE'},
                        'ENB-ID-Choice': {'members': [{'name': 'enb-ID-macro',
                                                       'size': [20],
                                                       'type': 'BIT STRING'},
                                                      {'name': 'enb-ID-shortmacro',
                                                       'size': [18],
                                                       'type': 'BIT STRING'},
                                                      {'name': 'enb-ID-longmacro',
                                                       'size': [21],
                                                       'type': 'BIT STRING'},
                                                      None],
                                          'type': 'CHOICE'},
                        'ENGNB-ID': {'members': [{'name': 'gNB-ID',
                                                  'size': [(22, 32)],
                                                  'type': 'BIT STRING'},
                                                 None],
                                     'type': 'CHOICE'},
                        'GNB-CU-UP-ID': {'restricted-to': [(0, 68719476735)],
                                         'type': 'INTEGER'},
                        'GNB-DU-ID': {'restricted-to': [(0, 68719476735)],
                                      'type': 'INTEGER'},
                        'GNB-ID-Choice': {'members': [{'name': 'gnb-ID',
                                                       'size': [(22, 32)],
                                                       'type': 'BIT STRING'},
                                                      None],
                                          'type': 'CHOICE'},
                        'GlobalE2node-ID': {'members': [{'name': 'gNB',
                                                         'type': 'GlobalE2node-gNB-ID'},
                                                        {'name': 'en-gNB',
                                                         'type': 'GlobalE2node-en-gNB-ID'},
                                                        {'name': 'ng-eNB',
                                                         'type': 'GlobalE2node-ng-eNB-ID'},
                                                        {'name': 'eNB',
                                                         'type': 'GlobalE2node-eNB-ID'},
                                                        None],
                                            'type': 'CHOICE'},
                        'GlobalE2node-eNB-ID': {'members': [{'name': 'global-eNB-ID',
                                                             'type': 'GlobalENB-ID'},
                                                            None],
                                                'type': 'SEQUENCE'},
                        'GlobalE2node-en-gNB-ID': {'members': [{'name': 'global-en-gNB-ID',
                                                                'type': 'GlobalenGNB-ID'},
                                                               {'name': 'en-gNB-CU-UP-ID',
                                                                'optional': True,
                                                                'type': 'GNB-CU-UP-ID'},
                                                               {'name': 'en-gNB-DU-ID',
                                                                'optional': True,
                                                                'type': 'GNB-DU-ID'},
                                                               None],
                                                   'type': 'SEQUENCE'},
                        'GlobalE2node-gNB-ID': {'members': [{'name': 'global-gNB-ID',
                                                             'type': 'GlobalgNB-ID'},
                                                            {'name': 'global-en-gNB-ID',
                                                             'optional': True,
                                                             'type': 'GlobalenGNB-ID'},
                                                            {'name': 'gNB-CU-UP-ID',
                                                             'optional': True,
                                                             'type': 'GNB-CU-UP-ID'},
                                                            {'name': 'gNB-DU-ID',
                                                             'optional': True,
                                                             'type': 'GNB-DU-ID'},
                                                            None],
                                                'type': 'SEQUENCE'},
                        'GlobalE2node-ng-eNB-ID': {'members': [{'name': 'global-ng-eNB-ID',
                                                                'type': 'GlobalngeNB-ID'},
                                                               {'name': 'global-eNB-ID',
                                                                'optional': True,
                                                                'type': 'GlobalENB-ID'},
                                                               {'name': 'ngENB-DU-ID',
                                                                'optional': True,
                                                                'type': 'NGENB-DU-ID'},
                                                               None],
                                                   'type': 'SEQUENCE'},
                        'GlobalENB-ID': {'members': [{'name': 'pLMN-Identity',
                                                      'type': 'PLMN-Identity'},
                                                     {'name': 'eNB-ID',
                                                      'type': 'ENB-ID'},
                                                     None],
                                         'type': 'SEQUENCE'},
                        'GlobalNG-RANNode-ID': {'members': [{'name': 'gNB',
                                                             'type': 'GlobalgNB-ID'},
                                                            {'name': 'ng-eNB',
                                                             'type': 'GlobalngeNB-ID'},
                                                            None],
                                                'type': 'CHOICE'},
                        'GlobalRIC-ID': {'members': [{'name': 'pLMN-Identity',
                                                      'type': 'PLMN-Identity'},
                                                     {'name': 'ric-ID',
                                                      'size': [20],
                                                      'type': 'BIT STRING'},
                                                     None],
                                         'type': 'SEQUENCE'},
                        'GlobalenGNB-ID': {'members': [{'name': 'pLMN-Identity',
                                                        'type': 'PLMN-Identity'},
                                                       {'name': 'gNB-ID',
                                                        'type': 'ENGNB-ID'},
                                                       None],
                                           'type': 'SEQUENCE'},
                        'GlobalgNB-ID': {'members': [{'name': 'plmn-id',
                                                      'type': 'PLMN-Identity'},
                                                     {'name': 'gnb-id',
                                                      'type': 'GNB-ID-Choice'},
                                                     None],
                                         'type': 'SEQUENCE'},
                        'GlobalngeNB-ID': {'members': [{'name': 'plmn-id',
                                                        'type': 'PLMN-Identity'},
                                                       {'name': 'enb-id',
                                                        'type': 'ENB-ID-Choice'},
                                                       None],
                                           'type': 'SEQUENCE'},
                        'MMEname': {'size': [(1, 150), None],
                                    'type': 'PrintableString'},
                        'NGENB-DU-ID': {'restricted-to': [(0, 68719476735)],
                                        'type': 'INTEGER'},
                        'PLMN-Identity': {'size': [3], 'type': 'OCTET STRING'},
                        'RANfunctionDefinition': {'type': 'OCTET STRING'},
                        'RANfunctionID': {'restricted-to': [(0, 4095)],
                                          'type': 'INTEGER'},
                        'RANfunctionOID': {'size': [(1, 1000), None],
                                           'type': 'PrintableString'},
                        'RANfunctionRevision': {'restricted-to': [(0, 4095)],
                                                'type': 'INTEGER'},
                        'RICactionDefinition': {'type': 'OCTET STRING'},
                        'RICactionID': {'restricted-to': [(0, 255)],
                                        'type': 'INTEGER'},
                        'RICactionType': {'type': 'ENUMERATED',
                                          'values': [('report', 0),
                                                     ('insert', 1),
                                                     ('policy', 2),
                                                     None]},
                        'RICcallProcessID': {'type': 'OCTET STRING'},
                        'RICcontrolAckRequest': {'type': 'ENUMERATED',
                                                 'values': [('noAck', 0),
                                                            ('ack', 1),
                                                            None]},
                        'RICcontrolHeader': {'type': 'OCTET STRING'},
                        'RICcontrolMessage': {'type': 'OCTET STRING'},
                        'RICcontrolOutcome': {'type': 'OCTET STRING'},
                        'RICeventTriggerDefinition': {'type': 'OCTET STRING'},
                        'RICindicationHeader': {'type': 'OCTET STRING'},
                        'RICindicationMessage': {'type': 'OCTET STRING'},
                        'RICindicationSN': {'restricted-to': [(0, 65535)],
                                            'type': 'INTEGER'},
                        'RICindicationType': {'type': 'ENUMERATED',
                                              'values': [('report', 0),
                                                         ('insert', 1),
                                                         None]},
                        'RICrequestID': {'members': [{'name': 'ricRequestorID',
                                                      'restricted-to': [(0,
                                                                         65535)],
                                                      'type': 'INTEGER'},
                                                     {'name': 'ricInstanceID',
                                                      'restricted-to': [(0,
                                                                         65535)],
                                                      'type': 'INTEGER'},
                                                     None],
                                         'type': 'SEQUENCE'},
                        'RICsubsequentAction': {'members': [{'name': 'ricSubsequentActionType',
                                                             'type': 'RICsubsequentActionType'},
                                                            {'name': 'ricTimeToWait',
                                                             'type': 'RICtimeToWait'},
                                                            None],
                                                'type': 'SEQUENCE'},
                        'RICsubsequentActionType': {'type': 'ENUMERATED',
                                                    'values': [('continue', 0),
                                                               ('wait', 1),
                                                               None]},
                        'RICtimeToWait': {'type': 'ENUMERATED',
                                          'values': [('w1ms', 0),
                                                     ('w2ms', 1),
                                                     ('w5ms', 2),
                                                     ('w10ms', 3),
                                                     ('w20ms', 4),
                                                     ('w30ms', 5),
                                                     ('w40ms', 6),
                                                     ('w50ms', 7),
                                                     ('w100ms', 8),
                                                     ('w200ms', 9),
                                                     ('w500ms', 10),
                                                     ('w1s', 11),
                                                     ('w2s', 12),
                                                     ('w5s', 13),
                                                     ('w10s', 14),
                                                     ('w20s', 15),
                                                     ('w60s', 16),
                                                     None]},
                        'TNLinformation': {'members': [{'name': 'tnlAddress',
                                                        'size': [(1, 160),
                                                                 None],
                                                        'type': 'BIT STRING'},
                                                       {'name': 'tnlPort',
                                                        'optional': True,
                                                        'size': [16],
                                                        'type': 'BIT STRING'},
                                                       None],
                                           'type': 'SEQUENCE'},
                        'TNLusage': {'type': 'ENUMERATED',
                                     'values': [('ric-service', 0),
                                                ('support-function', 1),
                                                ('both', 2),
                                                None]},
                        'TimeToWait': {'type': 'ENUMERATED',
                                       'values': [('v1s', 0),
                                                  ('v2s', 1),
                                                  ('v5s', 2),
                                                  ('v10s', 3),
                                                  ('v20s', 4),
                                                  ('v60s', 5),
                                                  None]},
                        'TransactionID': {'restricted-to': [(0, 255), None],
                                          'type': 'INTEGER'},
                        'TypeOfError': {'type': 'ENUMERATED',
                                        'values': [('not-understood', 0),
                                                   ('missing', 1),
                                                   None]}},
              'values': {}}}