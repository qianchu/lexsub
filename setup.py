#!/usr/bin/env python

from distutils.core import setup

setup(name='lexsub',
      version='1.0',
      description='lex sub evaluation',
      author='Oren Melamud',
      url='https://www.github.com/orenmel/lexsub/',
      packages=['jcs','jcs.evaluation','jcs.evaluation.measures','jcs.evaluation.measures.generalized_average_precision'],
      license=' Apache 2.0'
     )
