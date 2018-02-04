EXPECTED = {'ModuleTagsImplicit': {'extensibility-implied': False,
                        'imports': {},
                        'object-classes': {},
                        'object-sets': {},
                        'tags': 'IMPLICIT',
                        'types': {'A': {'tag': {'number': 3},
                                        'type': 'INTEGER'},
                                  'AI': {'tag': {'kind': 'IMPLICIT',
                                                 'number': 3},
                                         'type': 'INTEGER'},
                                  'BA': {'tag': {'number': 4}, 'type': 'A'},
                                  'BIA': {'tag': {'kind': 'IMPLICIT',
                                                  'number': 4},
                                          'type': 'A'},
                                  'BIAI': {'tag': {'kind': 'IMPLICIT',
                                                   'number': 4},
                                           'type': 'AI'},
                                  'C1': {'members': [{'members': [{'name': 'a',
                                                                   'tag': {'number': 0},
                                                                   'type': 'INTEGER'}],
                                                      'name': 'a',
                                                      'tag': {'number': 0},
                                                      'type': 'CHOICE'}],
                                         'type': 'CHOICE'},
                                  'CBA': {'tag': {'number': 5}, 'type': 'BA'},
                                  'CBIAI': {'tag': {'number': 5},
                                            'type': 'BIAI'},
                                  'CIBIA': {'tag': {'kind': 'IMPLICIT',
                                                    'number': 5},
                                            'type': 'BIA'},
                                  'CIBIAI': {'tag': {'kind': 'IMPLICIT',
                                                     'number': 5},
                                             'type': 'BIAI'},
                                  'S1': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'optional': True,
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'},
                                  'S2': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S3': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'tag': {'kind': 'EXPLICIT',
                                                              'number': 3},
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S4': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 1},
                                                      'type': 'C1'},
                                                     {'name': 'c',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'd',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S5': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S6': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     '...',
                                                     {'name': 'b',
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'},
                                  'S7': {'members': [{'name': 'a',
                                                      'tag': {'number': 2},
                                                      'type': 'INTEGER'},
                                                     '...',
                                                     {'name': 'b',
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'}},
                        'values': {}}}
