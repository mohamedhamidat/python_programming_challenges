#!/usr/bin/env python

'''je suis un module'''


def table_de_multiplication(nombre):
	for i in xrange(nombre):
		print "{0} * {1} = {2}".format(i, nombre, i*nombre)



table_de_multiplication(3)