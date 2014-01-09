#!/usr/bin/env python

__author__ = "Claudiu Persoiu"
__copyright__ = "Copyright 2014, Claudiu Persoiu"
__license__ = "GPL"
__email__ = "claudiu@claudiupersoiu.ro"

from unserializer.DumpPHPUnserialized import *

test_values = ['a:3:{s:3:"aaa";a:1:{s:3:"abb";s:3:"bcc";}s:2:"bb";s:3:"str";i:1;i:12;}',
               'a:1:{i:0;s:1:"a";}',
               'd:1.100000000000000088817841970012523233890533447265625;',
               'a:2:{i:0;O:8:"stdClass":1:{s:1:"a";s:1:"b";}i:1;O:8:"stdClass":1:{s:1:"b";s:1:"a";}}',
               'O:8:"stdClass":11:{s:2:"a1";i:1;s:2:"a2";i:2;s:2:"a3";i:2;s:2:"a4";i:2;s:2:"a5";i:2;s:2:"a6";i:2;s:2:"a7";i:2;s:2:"a8";i:2;s:2:"a9";i:2;s:3:"a10";i:2;s:3:"a11";i:2;}',
               'N;',
               'b:0;',
               'b:1;']

for test_string in test_values:
    print 'String: \n', test_string
    print '\nResult: \n', DumpPHPUnserialized(test_string).unserialize()
    print '--------------'


