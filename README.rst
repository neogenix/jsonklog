Project JSONkLog
================

The goal of this library is to provide a simple formatter, and handlers for
standard python logging libraries to deal with JSON output in a sort of
"set it and forget it" methodology that python logging currently provides.

Formatters :
++++++++++++

Currently there are two formatters:

        * JSONFormatter
        * JSONFormatterSimple

Each of the formatters processes the standard python logging messages into JSON
however the "Simple" library provides a limited output including only 3 key elements
and the mysterious 4th element "Extras"

Please note that "extras" as a dictionary requires the content to be nested under
the "extra" key within the dictionary

For examples, please see example_formatter.py within the source tree at:

        * https://github.com/neogenix/jsonklog/tree/master/examples

Handlers :
++++++++++

Currently there are two handlers, which require JSONFormatter, or JSONFormatterSimple
to have been used :

    * MongoDBHandler
    * ElasticSearchHandler

Each of the handlers can process the standard JSON messages from the included JSON
formatting libraries, and can have different destinations specified as follows:

MongoDBHandler :
----------------

This handler speaks MongoDB (using 'pymongo'), and can take the following arguments:

    * host - The destination host / ip of the MongoDB server
    * port - The destination port of the MongoDB server
    * db - The destination database to send messages to
    * collection - The destination collection to send messages to

* for more on MongoDB see the following URL: http://www.mongodb.org/

ElasticSearchHandler :
----------------------

This handler speaks ElasticSearch (using 'requests'), and can take the following arguments:

    * host - The destination host / ip of the ElasticSearch server
    * port - The destination port of the ElasticSearch server
    * index - The destination index to send messages to
    * doc_type - The destination doc_type to send messages to

* for more on ElasticSearch see the following URL: http://www.elasticsearch.org/

Note :
++++++

To format your JSON into "human readable whatsits" ensure your handler outputs
to stdout, and then pipe through the node-json library ('json'), installed as per:

    * npm install -g json

This is not a requirement, but rather what I'm using to do my testing ;)
