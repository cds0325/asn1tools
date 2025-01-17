EXPECTED = {'F1AP-PDU-Descriptions': {'extensibility-implied': False,
                           'imports': {'F1AP-CommonDataTypes': ['Criticality',
                                                                'ProcedureCode'],
                                       'F1AP-Constants': ['id-DLRRCMessageTransfer',
                                                          'id-ErrorIndication',
                                                          'id-F1Setup',
                                                          'id-GNBDUResourceCoordination',
                                                          'id-GNBDUStatusIndication',
                                                          'id-InitialULRRCMessageTransfer',
                                                          'id-Notify',
                                                          'id-PWSCancel',
                                                          'id-PWSFailureIndication',
                                                          'id-PWSRestartIndication',
                                                          'id-Paging',
                                                          'id-Reset',
                                                          'id-SystemInformationDeliveryCommand',
                                                          'id-UEContextModification',
                                                          'id-UEContextModificationRequired',
                                                          'id-UEContextRelease',
                                                          'id-UEContextReleaseRequest',
                                                          'id-UEContextSetup',
                                                          'id-UEInactivityNotification',
                                                          'id-ULRRCMessageTransfer',
                                                          'id-WriteReplaceWarning',
                                                          'id-gNBCUConfigurationUpdate',
                                                          'id-gNBDUConfigurationUpdate',
                                                          'id-privateMessage'],
                                       'F1AP-Containers': ['F1AP-PROTOCOL-IES',
                                                           'ProtocolIE-SingleContainer',
                                                           '{',
                                                           '}'],
                                       'F1AP-PDU-Contents': ['DLRRCMessageTransfer',
                                                             'ErrorIndication',
                                                             'F1SetupFailure',
                                                             'F1SetupRequest',
                                                             'F1SetupResponse',
                                                             'GNBCUConfigurationUpdate',
                                                             'GNBCUConfigurationUpdateAcknowledge',
                                                             'GNBCUConfigurationUpdateFailure',
                                                             'GNBDUConfigurationUpdate',
                                                             'GNBDUConfigurationUpdateAcknowledge',
                                                             'GNBDUConfigurationUpdateFailure',
                                                             'GNBDUResourceCoordinationRequest',
                                                             'GNBDUResourceCoordinationResponse',
                                                             'GNBDUStatusIndication',
                                                             'InitialULRRCMessageTransfer',
                                                             'Notify',
                                                             'PWSCancelRequest',
                                                             'PWSCancelResponse',
                                                             'PWSFailureIndication',
                                                             'PWSRestartIndication',
                                                             'Paging',
                                                             'PrivateMessage',
                                                             'Reset',
                                                             'ResetAcknowledge',
                                                             'SystemInformationDeliveryCommand',
                                                             'UEContextModificationConfirm',
                                                             'UEContextModificationFailure',
                                                             'UEContextModificationRequest',
                                                             'UEContextModificationRequired',
                                                             'UEContextModificationResponse',
                                                             'UEContextReleaseCommand',
                                                             'UEContextReleaseComplete',
                                                             'UEContextReleaseRequest',
                                                             'UEContextSetupFailure',
                                                             'UEContextSetupRequest',
                                                             'UEContextSetupResponse',
                                                             'UEInactivityNotification',
                                                             'ULRRCMessageTransfer',
                                                             'WriteReplaceWarningRequest',
                                                             'WriteReplaceWarningResponse']},
                           'object-classes': {'F1AP-ELEMENTARY-PROCEDURE': {'members': [{'name': '&InitiatingMessage',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&SuccessfulOutcome',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&UnsuccessfulOutcome',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&procedureCode',
                                                                                         'type': 'ProcedureCode'},
                                                                                        {'name': '&criticality',
                                                                                         'type': 'Criticality'}]}},
                           'object-sets': {'F1AP-ELEMENTARY-PROCEDURES': {'class': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                          'members': []},
                                           'F1AP-ELEMENTARY-PROCEDURES-CLASS-1': {'class': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                                  'members': ['reset',
                                                                                              'f1Setup',
                                                                                              'gNBDUConfigurationUpdate',
                                                                                              'gNBCUConfigurationUpdate',
                                                                                              'uEContextSetup',
                                                                                              'uEContextRelease',
                                                                                              'uEContextModification',
                                                                                              'uEContextModificationRequired',
                                                                                              'writeReplaceWarning',
                                                                                              'pWSCancel',
                                                                                              'gNBDUResourceCoordination',
                                                                                              ',',
                                                                                              '.']},
                                           'F1AP-ELEMENTARY-PROCEDURES-CLASS-2': {'class': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                                  'members': ['errorIndication',
                                                                                              'uEContextReleaseRequest',
                                                                                              'dLRRCMessageTransfer',
                                                                                              'uLRRCMessageTransfer',
                                                                                              'uEInactivityNotification',
                                                                                              'privateMessage',
                                                                                              'initialULRRCMessageTransfer',
                                                                                              'systemInformationDelivery',
                                                                                              'paging',
                                                                                              'notify',
                                                                                              'pWSRestartIndication',
                                                                                              'pWSFailureIndication',
                                                                                              'gNBDUStatusIndication',
                                                                                              ',',
                                                                                              '.']},
                                           'F1AP-PDU-ExtIEs': {'class': 'F1AP-PROTOCOL-IES',
                                                               'members': ['.']}},
                           'tags': 'AUTOMATIC',
                           'types': {'F1AP-PDU': {'members': [{'name': 'initiatingMessage',
                                                               'type': 'InitiatingMessage'},
                                                              {'name': 'successfulOutcome',
                                                               'type': 'SuccessfulOutcome'},
                                                              {'name': 'unsuccessfulOutcome',
                                                               'type': 'UnsuccessfulOutcome'},
                                                              {'actual-parameters': ['{'],
                                                               'name': 'choice-extension',
                                                               'type': 'ProtocolIE-SingleContainer'}],
                                                  'type': 'CHOICE'},
                                     'InitiatingMessage': {'members': [{'name': 'procedureCode',
                                                                        'table': {'type': 'F1AP-ELEMENTARY-PROCEDURES'},
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                       {'name': 'criticality',
                                                                        'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                       {'name': 'value',
                                                                        'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&InitiatingMessage'}],
                                                           'type': 'SEQUENCE'},
                                     'SuccessfulOutcome': {'members': [{'name': 'procedureCode',
                                                                        'table': {'type': 'F1AP-ELEMENTARY-PROCEDURES'},
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                       {'name': 'criticality',
                                                                        'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                       {'name': 'value',
                                                                        'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'F1AP-ELEMENTARY-PROCEDURE.&SuccessfulOutcome'}],
                                                           'type': 'SEQUENCE'},
                                     'UnsuccessfulOutcome': {'members': [{'name': 'procedureCode',
                                                                          'table': {'type': 'F1AP-ELEMENTARY-PROCEDURES'},
                                                                          'type': 'F1AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                         {'name': 'criticality',
                                                                          'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                    ['procedureCode']],
                                                                          'type': 'F1AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                         {'name': 'value',
                                                                          'table': ['F1AP-ELEMENTARY-PROCEDURES',
                                                                                    ['procedureCode']],
                                                                          'type': 'F1AP-ELEMENTARY-PROCEDURE.&UnsuccessfulOutcome'}],
                                                             'type': 'SEQUENCE'}},
                           'values': {'dLRRCMessageTransfer': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                               'value': None},
                                      'errorIndication': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                          'value': None},
                                      'f1Setup': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                  'value': None},
                                      'gNBCUConfigurationUpdate': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                   'value': None},
                                      'gNBDUConfigurationUpdate': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                   'value': None},
                                      'gNBDUResourceCoordination': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                    'value': None},
                                      'gNBDUStatusIndication': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                'value': None},
                                      'initialULRRCMessageTransfer': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                      'value': None},
                                      'notify': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                 'value': None},
                                      'pWSCancel': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                    'value': None},
                                      'pWSFailureIndication': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                               'value': None},
                                      'pWSRestartIndication': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                               'value': None},
                                      'paging': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                 'value': None},
                                      'privateMessage': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                         'value': None},
                                      'reset': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                'value': None},
                                      'systemInformationDelivery': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                    'value': None},
                                      'uEContextModification': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                'value': None},
                                      'uEContextModificationRequired': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                        'value': None},
                                      'uEContextRelease': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                           'value': None},
                                      'uEContextReleaseRequest': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                  'value': None},
                                      'uEContextSetup': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                         'value': None},
                                      'uEInactivityNotification': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                                   'value': None},
                                      'uLRRCMessageTransfer': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                               'value': None},
                                      'writeReplaceWarning': {'type': 'F1AP-ELEMENTARY-PROCEDURE',
                                                              'value': None}}}}