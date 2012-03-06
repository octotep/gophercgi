#!/usr/bin/env python

# The Gopher CGI Library v0.2
# Provides functions for creating moles for the gopher protocol in python
#
# Copyright (c) 2011 by Christopher Yealy (octotep at sdf.lonestar.org)
# Permission is granted for the user to use, modify, copy, and publish 
# any modifications however they like.
# Note that the software is provided "as is" with no warranty whatsoever;
# implied or otherwise.
#
# Documentation can be found at:
# gopher://sdf.org/1/users/octotep/downloads/gophercgi

import textwrap
import re

def print_text(text, line_length=67):
    """
    Prints a line of text by formatting it as a gopher selector and 
    word-wrapping the text to the 'line_length' variable.
    """
    
    string = textwrap.fill(text, line_length)
    for line in string.split('\n'):
        print "i%s\t\terror.host\t0" % (line)

def print_para(text, line_length=67):
    """
    Prints a paragraph(s) of text by word-wrapping each paragraph, while 
    preserving any newline characters. Word-wraps to the 'line_length'
    variable.
    """    
    for para in text.split("\n"):
        print_text(para, line_length)

def print_error(text, line_length=67):
    """
    Prints a string as an itemtype-3 gopher selector (error), while
    wrapping the text to the 'line_length' variable.
    """
    string = textwrap.fill(text, line_length)
    for line in string.split('\n'):
        print "3%s\t\terror.host\t0" % (line)

def print_link(link_type, link_text, dir_path, host, port=70):
    """
    Prints a gopher selector link using the arguments provided.
    """ 
    print "%s%s\t%s\t%s\t%s" % (link_type, link_text, dir_path,
                                host, port)

def print_telnet(link_text, host, port=23):
    """
    Prints a telnet link, using the arguments provided.
    """
    print "8%s\t\t%s\t%s" % (link_text, host, port)

def print_special(link_text, special_url):
    """
    Prints an external link to any url, not just gopher.
    """
    print "h%s\tURL:%s\tspecial.link\t70" % (link_text, special_url)

def print_line():
    """
    Prints a blank line.
    """
    print "i		error.host	0"

def get_arg_list(args_str, separator, prefix):
    """
    Converts a string containing arguments given to the mole
    into a list for easy use.
    
    'args_str' is a string contaning the arguments.
    'seperator' is the character that separates each argument
    'prefix' is a part at the beginning of the string which contains
        no arguments and will be removed from the results.

    Returns a list of the arguments from the string.
    """
    if args_str.startswith(prefix):
        pre_len = len(prefix)
        args = args_str[pre_len:]
        args_list = args.split(separator)
    else:
        args = args_str
        args_list = args.split(separator)
    return args_list

def get_arg_dict(args_str, separator, prefix, dict_separator="="):
    """
    Converts a string containing key-value pairs given to the mole
    into a dictionary for easy use.

    'args_str' is a string containing the arguments. 
    'seperator' is the character which separates the pairs
        from each other.
    'prefix' is a part at the beginning of the string which contains
        no arguments and will be removed from the results.
    'dict_separator' is the character which separates each key from its 
        respective value

    Returns a dictionary of the arguments from the string.
    """
    if args_str.startswith(prefix):
        pre_len = len(prefix)
        args = args_str[pre_len:]
        args_list = args.split(separator)
    else:
        args = args_str
        args_list = args.split(separator)
    args_dict = {}
    for part in args_list:
        key, value = part.split(dict_separator)
        args_dict[key] = value
    return args_dict


def tabs_to_spaces(text, tab_size=8):
    """
    Converts all the tab characters in 'text' to spaces.
    
    'tab_size' indicates the size of the tab stops.
    
    Returns the converted string.
    """
    text_arr = []
    for line in text.split("\n"):
        string = ""
        counter = 0
        for letter in line:
            if (letter != "\t"):
                string = "%s%s" % (string, letter)
                counter += 1
            else:
                indent = tab_size - (counter % tab_size)
                space = " " * indent
                string = "%s%s" % (string, space)
                counter += indent
        text_arr.append(string)
    return "\n".join(text_arr)

def gs_to_text(gm_text, show_prefixes=True, show_links=True):
    """
    Converts text formatted as a gopher selectors into plain text.
    Bears similarities to `lynx -dump`
    
    'show_prefixes' controls whether each selector that isn't
        text gets a label to identify what type of link it is.
    'show_links' controls whether a list of URL's is printed
        at the bottom of the output.
    
    Returns the converted text.
    """
    final_list = []
    link_list = []
    counter = 0
    gm_lines = gm_text.splitlines()
    for line in gm_lines:
        if len(line) == "":
            line = "i\t\terror.host\t0"
        itemtype = line[:1]
        prefix = ""
        suffix = ""
        tabs = line.split("\t")
        text = tabs.pop(0)
        if show_links:
            if (itemtype != 'i') and (itemtype != '3'):
                counter += 1
                suffix = " [%s]" % (str(counter))
                path = tabs.pop(0)
                host = tabs.pop(0)
                port = tabs.pop(0)
                url = _return_url(itemtype, host, path, port)
                link_list.append("%s. %s" % (suffix, url))
        if show_prefixes:
            prefix = _return_prefix(itemtype)
        final_list.append("%s\t%s%s" % (prefix, text[1:], suffix))
    final_str = "\n".join(final_list)
    if show_links:
        link_str = "\n".join(link_list)
        final_str = "%s\n\n%s" % (final_str, link_str)
    return final_str

def gm_to_gs(menu_text):
    """
    Converts text formatted as a gophermap into gopher selectors.

    Returns the converted text.
    """
    regex = re.compile('[\w\+].*?\t.*?\t.*?\t\d.*')
    final_list = []
    text_lines = menu_text.splitlines()
    for line in text_lines:
        match = regex.match(line)
        if match:
            final_list.append(line)
        else:
            new_line = "i%s\t\terror.host\t0" % (line)
            final_list.append(new_line)
    return "\n".join(final_list)

def _return_url(itemtype, host, path, port):
    """
    Takes parameters and creates a URL based on the 
    itemtype.

    Used internally by the library.

    Returns the URL string.
    """
    if len(path) != 0: 
        if path[0] == '/':
            tmp_path = path[1:]
            path = tmp_path
    if str(itemtype) == '8':
        return "telnet://%s:%s/%s" % (host, port, path)
    elif str(itemtype) == 'h':
        # Check for URL:
        if path[:4] == 'URL:':
            return path[4:]
        else:
            return "gopher://%s:%s/%s/%s" % (host, port,
                                             itemtype, path)
    else:
        return "gopher://%s:%s/%s/%s" % (host, port, itemtype, path)

def _return_prefix(itemtype):
    """
    Returns a text label based on itemtype.

    Used internally by the library.
    """
    if itemtype == 'i':
        return ""
    elif itemtype == '0':
        return "Text:"
    elif itemtype == '1':
        return "Dir:"
    elif itemtype == '2':
        return "CSO:"
    elif itemtype == '3':
        return "!!!:"
    elif itemtype == '4':
        return "File:"
    elif itemtype == '5':
        return "File:"
    elif itemtype == '6':
        return "File:"
    elif itemtype == '7':
        return "?:"
    elif itemtype == '8':
        return "Tel:"
    elif itemtype == '9':
        return "File:"
    elif itemtype == 'g':
        return "GIF:"
    elif itemtype == 'I':
        return "Image:"
    elif itemtype == 'T':
        return "Tel:"
    elif itemtype == 's':
        return "Snd:"
    elif itemtype == 'p':
        return "PNG:"
    elif itemtype == 'd':
        return "PDF:"
    elif itemtype == 'x':
        return "XML:"
    elif itemtype == 'c':
        return "CSS:"
    elif itemtype == 'h':
        return "HTML:"
    else:
        return "UnKN:"
