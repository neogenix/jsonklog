Project JSONkLog
================

The goal of this library is to provide a simple formatter, and handlers for
standard python logging libraries to deal with JSON output in a sort of
"set it and forget it" methodology that python logging currently provides.

Currently there are two formatters:

        * JSONFormatter
        * JSONFormatterSimple

Each of the formatters processes the standard python logging messages into JSON
however the "Simple" library provides a limited output including only 3 key elements
and the mysterious 4th element "Extras"

Please note that "extras" as a dictionary requires the content to be nested under
the "extra" key within the dictionary

For examples, please see example_formatter.py within the source tree at:

        * http://www.github.com/neogenix/jsonklog

To format your JSON into "human readable whatsits" ensure your handler outputs
to stdout, and then pipe through the node-json library ('json'), installed as per:

        * npm install -g json

This is not a requirement, but rather what I'm using to do my testing ;)
