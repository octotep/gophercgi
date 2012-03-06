#!/usr/bin/env python

import gophercgi

print_text = gophercgi.print_text
print_error = gophercgi.print_error
print_link = gophercgi.print_link
print_special = gophercgi.print_special
print_telnet = gophercgi.print_telnet
blank_line = gophercgi.print_line

home_dir = "/users/octotep/downloads/gophercgi"
base_dir = "/users/octotep/downloads"
host = "sdf.org"

please_stay = "...but please don't leave yet, we have an excellent \
demonstration lined up for you."

welcome = "Hello and welcome to the gophercgi demonstration. Please \
have a seat, the show will be starting shortly..."

print_link(1, "Back to gophercgi directory...", home_dir, host)
print_text(please_stay)
blank_line()
print_text(welcome)
blank_line()

thanks = "Ah. You've made a wise decision to stay. You're going to have \
a _great_ time here. Now as a little warm-up act, here's some links to \
keep you occupied."

print_text(thanks)
blank_line()
print_link(0, "0. Documetation, anyone?", "%s/documentation.txt" % (home_dir), host)
print_link(1, "1. Floodgap systems", "", "gopher.floodgap.com")
print_link(2, "2. CSO at ns.uic.edu", "", "ns.uic.edu", 105)
print_link(3, "3. Holy schmoley! It's an error!", "", "error.host")
print_link(4, "4. Macintosh binhex (just a binary file)", "%s/gophercgi.py" % (home_dir), host) 
print_link(5, "5. PC Binary (just a binary file)", "%s/gophercgi.py" % (home_dir), host)
print_link(6, "6. Uuencoded binary (binary file)", "%s/gophercgi.py" % (home_dir), host)
print_link(7, "7. Search gopher with Veronica search engine", "/v2/vs", "gopher.floodgap.com")
print_link(8, "8. Connect to SDF public access unix system (telnet)", "", "sdf.org", "23")
print_link(9, "9. A _real_ binary file", "%s/gophercgi.py" % (home_dir), host)
blank_line()

cool = "Cool, right? You can print any link you want! All you need to do \
is fill in all appropriate fields, and *BAM*, you got yourself a link to \
anything."

print_text(cool)
blank_line()

special = "Now, how about some special links. Instead of print_link(),\
these links use print_telnet() and print_special()."

print_text(special)
blank_line()

print_telnet("Connect to SDF (again)", "sdf.org", "23")
print_special("Check out my webspace", "http://octotep.sdf.org")
print_special("Securely browse with DuckDuckGo", "https://duckduckgo.com")
print_special("SSH to SDF (browser must know how to handle ssh://)", "ssh://sdf.org")
print_special("Even a mailto link", "mailto:octotep+gophcgiex@sdf.lonestar.org")
print_error("There's even print_error() !")
blank_line()

inter = "Fantastic! Now, our portion of the show is finished, \
but please feel free to stay and watch the other acts lined up for you!"
print_text(inter)

print_link(1, "load_args() test", "%s/tests/args_test.cgi?ha:he:hi:ho:hu" % (home_dir), host)
print_link(1, "Conversion test", "%s/tests/conv_test.cgi" % (home_dir), host)
