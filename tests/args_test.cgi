#!/usr/bin/env python

import gophercgi

print_line = gophercgi.print_line
print_text = gophercgi.print_text
print_error = gophercgi.print_error
print_link = gophercgi.print_link
get_arg_list = gophercgi.get_arg_list

home_dir = "/users/octotep/downloads/gophercgi/tests"
base_dir = "/users/octotep/downloads/gophercgi/"
host = "sdf.org"

print_link(1, "Back to gophercgi directory...", base_dir, host)

desc = "This test will take all the arguments supplied to the script \
(split by a colon) and print them"

print_line()
print_text(desc)

my_args_list = get_arg_list(os.environ['SELECTOR'], ":", "/users/octotep/downloads/gophercgi/tests/args_test.cgi?")

length = len(my_args_list)

print_line()
print_text("The number of arguments: %s" % (str(length)))
print_line()

counter = 0
for x in my_args_list:
    print_text("%s. %s" % (str(counter), x))
    counter += 1

print_line()
print_text("The whole list:")
print_text(str(my_args_list))
print_line()
print_link(1, "Let's try some dictionaries!", "%s/args_test2.cgi?1=a:2=b:3=c" % (home_dir), host)
print_link(1, "Back to gophercgi directory...", base_dir, host)