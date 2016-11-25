Kenessa
====
This is a Python Library [myrw](https://github.com/rmuhire/kenessa)
It supports Python 2.7

Original Python code is Copyright (C) 2016 The myrw Author.


Requirements
============

-  Python 2.7

Installation
============

Using PIP via PyPI

    pip install myrw
    
Usage
=====
    
   from myrw import Province
    all Province
    >>> print Province('all').province()
    #One Province
    #Province ID
    >>> print Province('1').province()
    #Province Name
    >>> print Province('kigali').province()
    #Province Code
    >>> print Province('01').province()
