#!/usr/bin/env python

import gophercgi

blank_line = gophercgi.print_line
print_text = gophercgi.print_text
print_link = gophercgi.print_link
get_arg_dict = gophercgi.get_arg_dict

home_dir = "/users/octotep/downloads/gophercgi"
host = "sdf.org"

print_link(1, "Back to gophercgi directory...", home_dir, host)

desc = "This test will take all the key/value pairs supplied to the script \
(split by a colon) and print them (the key and value are separated by a \"=\")"

blank_line()
print_text(desc)

args_dict = get_arg_dict(os.environ['SELECTOR'], ":", "/users/octotep/downloads/gophercgi/tests/args_test2.cgi?")

length = len(args_dict)

blank_line()
print_text("The number of pairs: %s" % (str(length)))
blank_line()

counter = 0
for x, y in args_dict.items():
    print_text("%s. %s -> %s" % (str(counter), x, y))
    counter += 1

blank_line()
print_text("The whole dictionary:")
print_text(str(args_dict))
blank_line()
print_link(1, "Conversion functions", "%s/tests/conv_test.cgi" % (home_dir), host)
print_link(1, "Back to gophercgi directory...", home_dir, host)