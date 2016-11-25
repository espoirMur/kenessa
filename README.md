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

    >>> from myrw import Province
    
All provinces
~~~~~~~~~~~~~

        >>> print Province('all').province()
    
One Province (allow province id, code or name)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        >>> print Province('1').province()
        >>> print Province('kigali').province()
        >>> print Province('01').province()
