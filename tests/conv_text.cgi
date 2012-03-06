#!/usr/bin/env python

import gophercgi

text_to_gm = gophercgi.gm_to_gs

text = open('/ftp/pub/users/octotep/downloads/gophercgi/tests/text_test', 'r').read()
gophermap = text_to_gm(text)
print gophermap