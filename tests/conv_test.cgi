#!/usr/bin/env python

import gophercgi

blank_line = gophercgi.print_line
print_text = gophercgi.print_text
print_link = gophercgi.print_link

home_dir = "/users/octotep/downloads/gophercgi/tests"
base_dir = "/users/octotep/downloads/gophercgi"
host = "sdf.org"

print_link(1, "Back to gophercgi directory...", base_dir, host)

desc = "This script will demonstrate the two conversion functions capabilities."

gm2text_desc = "First, the gs_to_text() function will be demonstrated. This \
will take a string formatted as gopher selectors and print it as text."

blank_line()
print_text(desc)
blank_line()
print_text(gm2text_desc)
print_link(0, "The gopher selectors to be converted", "%s/gm_test" % (home_dir), host)
print_link(0, "See the conversion", "%s/conv_gm.cgi" % (home_dir), host)


text2gm_desc = "Next, the text_to_gm() function will be demonstrated. This \
will take a string formatted as text (with gophermap-style links) and \
print it as gopher selectors."

blank_line()
print_text(text2gm_desc)
print_link(0, "The text file to be converted", "%s/text_test" % (home_dir), host)
print_link(1, "See the conversion", "%s/conv_text.cgi" % (home_dir), host)


blank_line()
print_link(1, "Back to gophercgi directory...", base_dir, host)



