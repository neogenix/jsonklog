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


import logging
import traceback
import itertools

import anyjson as json


class JSONFormatter(logging.Formatter):

    def __init__(self, fmt=None, datefmt=None, dump_json=True):
        self.datefmt = datefmt
        self.dump_json = dump_json

    def formatException(self, ei, strip_newlines=True):
        lines = traceback.format_exception(*ei)
        if strip_newlines:
            lines = [itertools.ifilter(lambda x: x, line.rstrip().splitlines())
                     for line in lines]
            lines = list(itertools.chain(*lines))
        return lines

    def format(self, record):
        msg = {'message': record.getMessage(),
               'asctime': self.formatTime(record, self.datefmt),
               'name': record.name,
               'msg': record.msg,
               'args': record.args,
               'levelname': record.levelname,
               'levelno': record.levelno,
               'pathname': record.pathname,
               'filename': record.filename,
               'module': record.module,
               'lineno': record.lineno,
               'funcname': record.funcName,
               'created': record.created,
               'msecs': record.msecs,
               'relative_created': record.relativeCreated,
               'thread': record.thread,
               'thread_name': record.threadName,
               'process_name': record.processName,
               'process': record.process,
               'traceback': None}

        if hasattr(record, 'extra'):
            msg['extra'] = record.extra

        if record.exc_info:
            msg['traceback'] = self.formatException(record.exc_info)

        if not self.dump_json:
            return msg

        return json.dumps(msg)


class JSONFormatterSimple(JSONFormatter):

    def format(self, record):
        msg = {'message': record.getMessage(),
               'asctime': self.formatTime(record, self.datefmt),
               'levelname': record.levelname,
               'traceback': None}

        if hasattr(record, 'extra'):
            msg['extra'] = record.extra

        if record.exc_info:
            msg['traceback'] = self.formatException(record.exc_info)

        if not self.dump_json:
            return msg

        return json.dumps(msg)
