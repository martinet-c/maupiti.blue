#!/usr/bin/python3
page = "tendances"
import util
util.header(page)
cpt = util.print_nights(page)
util.footer(page, cpt)
