Kenessa
=======
The [kenessa](https://pypi.python.org/pypi/kenessa/0.1.4) Python Library help discover Rwanda Administrative Location [
It supports Python 2.7

Original Python code is Copyright (C) 2016 Remy Muhire.


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

Sector
========
    
    >>> print Province('all').sector()
    >>> print Province('kigali').sector()
    >>> print Province('1').sector()
    >>> print Province('01').sector()

    
