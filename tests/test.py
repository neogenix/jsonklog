# -*- coding: utf-8 -*-
#
#   Copyright [2012] [Patrick Ancillotti]
#   Copyright [2011] [Jason Kölker]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

try:
    import cStringIO
    StringIO = cStringIO
except ImportError:
    import StringIO

import logging
import unittest

import anyjson as json

from jsonklog import formatter


class JSONFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.log = logging.getLogger('JSONFormatterTestCase')
        self.stream = StringIO.StringIO()

        handler = logging.StreamHandler(self.stream)
        handler.setFormatter(formatter.JSONFormatter())

        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)

    def tearDown(self):
        self.log = None

    def test_json(self):
        test_msg = 'This is a %(test)s line'
        test_data = {'test': 'log'}
        self.log.debug(test_msg, test_data)
        data = json.loads(self.stream.getvalue())

        self.assertTrue(data)
        self.assertTrue('extra' not in data)
        self.assertEqual(self.log.name, data['name'])

        self.assertEqual(test_msg % test_data, data['message'])
        self.assertEqual(test_msg, data['msg'])
        self.assertEqual(test_data, data['args'])

        self.assertEqual('test.py', data['filename'])
        self.assertEqual('test_json', data['funcname'])
        self.assertEqual('DEBUG', data['levelname'])

        self.assertEqual(logging.DEBUG, data['levelno'])
        self.assertFalse(data['traceback'])

    def test_json_exception(self):
        test_msg = 'This is %s'
        test_data = 'exceptional'
        try:
            raise Exception('This is exceptional')
        except Exception:
            self.log.exception(test_msg, test_data)

        data = json.loads(self.stream.getvalue())

        self.assertEqual([test_data], data['args'])

        self.assertEqual('ERROR', data['levelname'])
        self.assertEqual(logging.ERROR, data['levelno'])
        self.assertTrue(data['traceback'])


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter.JSONFormatter())
    log.addHandler(handler)
    log.debug('All systems operational')
    log.info('Airspeed 300 knots')
    log.warn('Low on fuel')
    log.error('No fuel. Trying to glide.')
    log.critical('Glide attempt failed. About to crash.')
