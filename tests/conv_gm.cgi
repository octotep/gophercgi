#!/usr/bin/env python

import gophercgi

gs_to_text = gophercgi.gs_to_text

gophermap = open('/ftp/pub/users/octotep/downloads/gophercgi/tests/gm_test', 'r').read()
text = gs_to_text(gophermap)
print text


