EXPECTED = {'E2AP-PDU-Descriptions': {'extensibility-implied': False,
                           'imports': {'E2AP-CommonDataTypes': ['Criticality',
                                                                'ProcedureCode'],
                                       'E2AP-Constants': ['id-E2connectionUpdate',
                                                          'id-E2nodeConfigurationUpdate',
                                                          'id-E2removal',
                                                          'id-E2setup',
                                                          'id-ErrorIndication',
                                                          'id-RICcontrol',
                                                          'id-RICindication',
                                                          'id-RICserviceQuery',
                                                          'id-RICserviceUpdate',
                                                          'id-RICsubscription',
                                                          'id-RICsubscriptionDelete',
                                                          'id-RICsubscriptionDeleteRequired',
                                                          'id-Reset'],
                                       'E2AP-PDU-Contents': ['E2RemovalFailure',
                                                             'E2RemovalRequest',
                                                             'E2RemovalResponse',
                                                             'E2connectionUpdate',
                                                             'E2connectionUpdateAcknowledge',
                                                             'E2connectionUpdateFailure',
                                                             'E2nodeConfigurationUpdate',
                                                             'E2nodeConfigurationUpdateAcknowledge',
                                                             'E2nodeConfigurationUpdateFailure',
                                                             'E2setupFailure',
                                                             'E2setupRequest',
                                                             'E2setupResponse',
                                                             'ErrorIndication',
                                                             'RICcontrolAcknowledge',
                                                             'RICcontrolFailure',
                                                             'RICcontrolRequest',
                                                             'RICindication',
                                                             'RICserviceQuery',
                                                             'RICserviceUpdate',
                                                             'RICserviceUpdateAcknowledge',
                                                             'RICserviceUpdateFailure',
                                                             'RICsubscriptionDeleteFailure',
                                                             'RICsubscriptionDeleteRequest',
                                                             'RICsubscriptionDeleteRequired',
                                                             'RICsubscriptionDeleteResponse',
                                                             'RICsubscriptionFailure',
                                                             'RICsubscriptionRequest',
                                                             'RICsubscriptionResponse',
                                                             'ResetRequest',
                                                             'ResetResponse']},
                           'object-classes': {'E2AP-ELEMENTARY-PROCEDURE': {'members': [{'name': '&InitiatingMessage',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&SuccessfulOutcome',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&UnsuccessfulOutcome',
                                                                                         'type': 'OpenType'},
                                                                                        {'name': '&procedureCode',
                                                                                         'type': 'ProcedureCode'},
                                                                                        {'name': '&criticality',
                                                                                         'type': 'Criticality'}]}},
                           'object-sets': {'E2AP-ELEMENTARY-PROCEDURES': {'class': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                          'members': []},
                                           'E2AP-ELEMENTARY-PROCEDURES-CLASS-1': {'class': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                                  'members': ['ricSubscription',
                                                                                              'ricSubscriptionDelete',
                                                                                              'ricServiceUpdate',
                                                                                              'ricControl',
                                                                                              'e2setup',
                                                                                              'e2nodeConfigurationUpdate',
                                                                                              'e2connectionUpdate',
                                                                                              'reset',
                                                                                              'e2removal',
                                                                                              ',',
                                                                                              '.']},
                                           'E2AP-ELEMENTARY-PROCEDURES-CLASS-2': {'class': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                                  'members': ['ricIndication',
                                                                                              'ricServiceQuery',
                                                                                              'errorIndication',
                                                                                              'ricSubscriptionDeleteRequired',
                                                                                              ',',
                                                                                              '.']}},
                           'tags': 'AUTOMATIC',
                           'types': {'E2AP-PDU': {'members': [{'name': 'initiatingMessage',
                                                               'type': 'InitiatingMessage'},
                                                              {'name': 'successfulOutcome',
                                                               'type': 'SuccessfulOutcome'},
                                                              {'name': 'unsuccessfulOutcome',
                                                               'type': 'UnsuccessfulOutcome'},
                                                              None],
                                                  'type': 'CHOICE'},
                                     'InitiatingMessage': {'members': [{'name': 'procedureCode',
                                                                        'table': {'type': 'E2AP-ELEMENTARY-PROCEDURES'},
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                       {'name': 'criticality',
                                                                        'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                       {'name': 'value',
                                                                        'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&InitiatingMessage'}],
                                                           'type': 'SEQUENCE'},
                                     'SuccessfulOutcome': {'members': [{'name': 'procedureCode',
                                                                        'table': {'type': 'E2AP-ELEMENTARY-PROCEDURES'},
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                       {'name': 'criticality',
                                                                        'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                       {'name': 'value',
                                                                        'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                  ['procedureCode']],
                                                                        'type': 'E2AP-ELEMENTARY-PROCEDURE.&SuccessfulOutcome'}],
                                                           'type': 'SEQUENCE'},
                                     'UnsuccessfulOutcome': {'members': [{'name': 'procedureCode',
                                                                          'table': {'type': 'E2AP-ELEMENTARY-PROCEDURES'},
                                                                          'type': 'E2AP-ELEMENTARY-PROCEDURE.&procedureCode'},
                                                                         {'name': 'criticality',
                                                                          'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                    ['procedureCode']],
                                                                          'type': 'E2AP-ELEMENTARY-PROCEDURE.&criticality'},
                                                                         {'name': 'value',
                                                                          'table': ['E2AP-ELEMENTARY-PROCEDURES',
                                                                                    ['procedureCode']],
                                                                          'type': 'E2AP-ELEMENTARY-PROCEDURE.&UnsuccessfulOutcome'}],
                                                             'type': 'SEQUENCE'}},
                           'values': {'e2connectionUpdate': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                             'value': None},
                                      'e2nodeConfigurationUpdate': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                    'value': None},
                                      'e2removal': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                    'value': None},
                                      'e2setup': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                  'value': None},
                                      'errorIndication': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                          'value': None},
                                      'reset': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                'value': None},
                                      'ricControl': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                     'value': None},
                                      'ricIndication': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                        'value': None},
                                      'ricServiceQuery': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                          'value': None},
                                      'ricServiceUpdate': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                           'value': None},
                                      'ricSubscription': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                          'value': None},
                                      'ricSubscriptionDelete': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                'value': None},
                                      'ricSubscriptionDeleteRequired': {'type': 'E2AP-ELEMENTARY-PROCEDURE',
                                                                        'value': None}}}}