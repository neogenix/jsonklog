# -*- coding: utf-8 -*-
#
#   Copyright [2012] [Patrick Ancillotti]
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

import sys
import logging
from jsonklog import formatter


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # Standard JSON Formatter

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter.JSONFormatter())
    log.addHandler(handler)

    # Simple JSON Formatter

    handler_simple = logging.StreamHandler(sys.stdout)
    handler_simple.setFormatter(formatter.JSONFormatterSimple())
    log.addHandler(handler_simple)

    # Generating regular plain vanilla logs

    log.debug('All systems operational')
    log.info('Airspeed 300 knots')
    log.warn('Low on fuel')
    log.error('No fuel. Trying to glide.')
    log.critical('Glide attempt failed. About to crash.')

    # Generating 'extra' nested dictionary logs

    d = {'extra': {'some': '1', 'extras': '2', 'here': '3'}}
    log.info('Extra records here', extra=d)

    # Generating Exceptions

    test_msg = 'This is %s'
    test_data = 'exceptional'

    try:
        raise Exception('This is exceptional')
    except Exception:
        log.exception(test_msg, test_data)
