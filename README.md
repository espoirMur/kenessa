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

    pip install kenessa
    
Usage
=====
    
    from kenessa import Province
    
Provinces
=========
        
    >>> print Province('all').province()
    >>> print Province('1').province()
    >>> print Province('kigali').province()
    >>> print Province('01').province()
    
District
========
    
    >>> print Province('all').district()
    >>> print Province('kigali').district()
    >>> print Province('1').district()
    >>> print Province('01').district()
    
