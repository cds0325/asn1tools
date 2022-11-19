EXPECTED = {'F1AP-Containers': {'extensibility-implied': False,
                     'imports': {'F1AP-CommonDataTypes': ['Criticality',
                                                          'Presence',
                                                          'PrivateIE-ID',
                                                          'ProtocolExtensionID',
                                                          'ProtocolIE-ID'],
                                 'F1AP-Constants': ['maxPrivateIEs',
                                                    'maxProtocolExtensions',
                                                    'maxProtocolIEs']},
                     'object-classes': {'F1AP-PRIVATE-IES': {'members': [{'name': '&id',
                                                                          'type': 'PrivateIE-ID'},
                                                                         {'name': '&criticality',
                                                                          'type': 'Criticality'},
                                                                         {'name': '&Value',
                                                                          'type': 'OpenType'},
                                                                         {'name': '&presence',
                                                                          'type': 'Presence'}]},
                                        'F1AP-PROTOCOL-EXTENSION': {'members': [{'name': '&id',
                                                                                 'type': 'ProtocolExtensionID'},
                                                                                {'name': '&criticality',
                                                                                 'type': 'Criticality'},
                                                                                {'name': '&Extension',
                                                                                 'type': 'OpenType'},
                                                                                {'name': '&presence',
                                                                                 'type': 'Presence'}]},
                                        'F1AP-PROTOCOL-IES': {'members': [{'name': '&id',
                                                                           'type': 'ProtocolIE-ID'},
                                                                          {'name': '&criticality',
                                                                           'type': 'Criticality'},
                                                                          {'name': '&Value',
                                                                           'type': 'OpenType'},
                                                                          {'name': '&presence',
                                                                           'type': 'Presence'}]},
                                        'F1AP-PROTOCOL-IES-PAIR': {'members': [{'name': '&id',
                                                                                'type': 'ProtocolIE-ID'},
                                                                               {'name': '&firstCriticality',
                                                                                'type': 'Criticality'},
                                                                               {'name': '&FirstValue',
                                                                                'type': 'OpenType'},
                                                                               {'name': '&secondCriticality',
                                                                                'type': 'Criticality'},
                                                                               {'name': '&SecondValue',
                                                                                'type': 'OpenType'},
                                                                               {'name': '&presence',
                                                                                'type': 'Presence'}]}},
                     'object-sets': {},
                     'tags': 'AUTOMATIC',
                     'types': {'PrivateIE-Container': {'element': {'actual-parameters': ['{'],
                                                                   'type': 'PrivateIE-Field'},
                                                       'parameters': ['IEsSetParam'],
                                                       'size': [(1,
                                                                 'maxPrivateIEs')],
                                                       'type': 'SEQUENCE OF'},
                               'PrivateIE-Field': {'members': [{'name': 'id',
                                                                'table': {'type': 'IEsSetParam'},
                                                                'type': 'F1AP-PRIVATE-IES.&id'},
                                                               {'name': 'criticality',
                                                                'table': ['IEsSetParam',
                                                                          ['id']],
                                                                'type': 'F1AP-PRIVATE-IES.&criticality'},
                                                               {'name': 'value',
                                                                'table': ['IEsSetParam',
                                                                          ['id']],
                                                                'type': 'F1AP-PRIVATE-IES.&Value'}],
                                                   'parameters': ['IEsSetParam'],
                                                   'type': 'SEQUENCE'},
                               'ProtocolExtensionContainer': {'element': {'actual-parameters': ['{'],
                                                                          'type': 'ProtocolExtensionField'},
                                                              'parameters': ['ExtensionSetParam'],
                                                              'size': [(1,
                                                                        'maxProtocolExtensions')],
                                                              'type': 'SEQUENCE '
                                                                      'OF'},
                               'ProtocolExtensionField': {'members': [{'name': 'id',
                                                                       'table': {'type': 'ExtensionSetParam'},
                                                                       'type': 'F1AP-PROTOCOL-EXTENSION.&id'},
                                                                      {'name': 'criticality',
                                                                       'table': ['ExtensionSetParam',
                                                                                 ['id']],
                                                                       'type': 'F1AP-PROTOCOL-EXTENSION.&criticality'},
                                                                      {'name': 'extensionValue',
                                                                       'table': ['ExtensionSetParam',
                                                                                 ['id']],
                                                                       'type': 'F1AP-PROTOCOL-EXTENSION.&Extension'}],
                                                          'parameters': ['ExtensionSetParam'],
                                                          'type': 'SEQUENCE'},
                               'ProtocolIE-Container': {'element': {'actual-parameters': ['{'],
                                                                    'type': 'ProtocolIE-Field'},
                                                        'parameters': ['IEsSetParam'],
                                                        'size': [(0,
                                                                  'maxProtocolIEs')],
                                                        'type': 'SEQUENCE OF'},
                               'ProtocolIE-ContainerPair': {'element': {'actual-parameters': ['{'],
                                                                        'type': 'ProtocolIE-FieldPair'},
                                                            'parameters': ['IEsSetParam'],
                                                            'size': [(0,
                                                                      'maxProtocolIEs')],
                                                            'type': 'SEQUENCE '
                                                                    'OF'},
                               'ProtocolIE-Field': {'members': [{'name': 'id',
                                                                 'table': {'type': 'IEsSetParam'},
                                                                 'type': 'F1AP-PROTOCOL-IES.&id'},
                                                                {'name': 'criticality',
                                                                 'table': ['IEsSetParam',
                                                                           ['id']],
                                                                 'type': 'F1AP-PROTOCOL-IES.&criticality'},
                                                                {'name': 'value',
                                                                 'table': ['IEsSetParam',
                                                                           ['id']],
                                                                 'type': 'F1AP-PROTOCOL-IES.&Value'}],
                                                    'parameters': ['IEsSetParam'],
                                                    'type': 'SEQUENCE'},
                               'ProtocolIE-FieldPair': {'members': [{'name': 'id',
                                                                     'table': {'type': 'IEsSetParam'},
                                                                     'type': 'F1AP-PROTOCOL-IES-PAIR.&id'},
                                                                    {'name': 'firstCriticality',
                                                                     'table': ['IEsSetParam',
                                                                               ['id']],
                                                                     'type': 'F1AP-PROTOCOL-IES-PAIR.&firstCriticality'},
                                                                    {'name': 'firstValue',
                                                                     'table': ['IEsSetParam',
                                                                               ['id']],
                                                                     'type': 'F1AP-PROTOCOL-IES-PAIR.&FirstValue'},
                                                                    {'name': 'secondCriticality',
                                                                     'table': ['IEsSetParam',
                                                                               ['id']],
                                                                     'type': 'F1AP-PROTOCOL-IES-PAIR.&secondCriticality'},
                                                                    {'name': 'secondValue',
                                                                     'table': ['IEsSetParam',
                                                                               ['id']],
                                                                     'type': 'F1AP-PROTOCOL-IES-PAIR.&SecondValue'}],
                                                        'parameters': ['IEsSetParam'],
                                                        'type': 'SEQUENCE'},
                               'ProtocolIE-SingleContainer': {'actual-parameters': ['{'],
                                                              'parameters': ['IEsSetParam'],
                                                              'type': 'ProtocolIE-Field'}},
                     'values': {}}}