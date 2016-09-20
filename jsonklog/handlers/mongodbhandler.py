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

import logging
import pymongo
import anyjson as json

from jsonklog.handlers.basehandler import RequireJSONFormatter


class MongoDBHandler(RequireJSONFormatter):

    def __init__(self, host="localhost", db="logs", port=27017,
                 collection="logs"):

        logging.Handler.__init__(self)
        self.connection = pymongo.MongoClient(host, port)
        self.db = self.connection[db]
        self.collection = self.db[collection]

    def emit(self, record):

        """ pymongo expects a dict """
        msg = self.format(record)

        if not isinstance(msg, dict):
            msg = json.loads(msg)

        self.collection.insert(msg)
