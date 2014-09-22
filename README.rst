Django MSSQL Database Backend
=============================

`django_pytds`_ provies a Django database backend for Microsoft SQL Server.

It is based on django-mssql but replaces the ADO component with the PyTDS component. No PyODBC of FreeTDS required.

Documentation is available at `django-mssql.readthedocs.org`_.

Requirements
------------

    * Python 2.7
    * PyTDS  (https://github.com/denisenkom/pytds)

Not required but good to have as PyTDS claims that it makes it faster:
    * bitarray


SQL Server Versions
-------------------

Supported Versions:
    * 2008
    * 2008r2
    * 2012

The SQL Server version will be detected upon initial connection.

Django Version
--------------

I haven't tested much. This is still work in progress but it seems to work pretty fine so far. The original project django-mssql works on the following:

	* Django 1.6
	* Django 1.7 (schema migrations may not be fully supported)


django-mssql 1.4 supports Django 1.4 and 1.5. 
(so I suppose we do, too.)


Django Setup
------------
In Django Settings, use::

	'default': {
		'ENGINE': 'django_pytds',
		'NAME': 'DBNAME',
		'HOST': 'DBHOST',
		'USER': 'USERNAME',
		'PASSWORD': 'PASSWORD',
		'OPTIONS': {
			'autocommit': True/False   (Default: False)
			'use_mars':  True/False    (Default: False)
			'readonly':  True/False    (Default: False)
		},
	}

The options part is optional.

Notes
-----

I honestly don't have time to maintain this project. If you feel like you want to help, please go ahead. This was just implemented to get a project moving and it fulfils the needs perfectly at this point, so I don't think I'll be adding more to it. It's very easy to fix issues on this project than to setup PyODBC and FreeTDS and PyTDS is alive and gets updated regularly. Patch/Fix this instead of wasting time on the ODBC driver.

References
----------

    * PyTDS on github: https://github.com/denisenkom/pytds
    * Django-mssql on PyPi: http://pypi.python.org/pypi/django-mssql
    * DB-API 2.0 specification: http://www.python.org/dev/peps/pep-0249/

.. _`PyTDS`: https://github.com/denisenkom/pytds
.. _`Django-mssql`: https://bitbucket.org/Manfre/django-mssql
.. _django-mssql.readthedocs.org: http://django-mssql.readthedocs.org/
.. _PyWin32: http://sourceforge.net/projects/pywin32/
