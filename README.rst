humanize-api
============

|pythonversion| |githubrepo| |version|

This is an API that can make various values more human readable.

Documentation
-------------

The API documentation is generated dynamically and can be found at :code:`http://localhost:8080/api/v1/docs`.

Setup for development
---------------------

I assume you are using pyenv with the pyenv-virtualenv plugin to be able to create virtualenvs.

Run the following commands to get started:

To create and activate the virtualenv:

.. code:: bash

  pyenv virtualenv humanize-api-3.7.7
  pyenv local humanize-api-3.7.7

To install the requirements for development:

.. code:: bash

  pip install -r requirements-dev.txt

For version bumps uses the following alias:

.. code:: bash

  alias pup='punch --action mbuild'

Testing, running
----------------

To test, run:

.. code:: bash

  pytest

To run locally, in the virtualenv defined above, you can run:

.. code:: bash

  ./run_api.sh

You can also run it in docker-compose using the following command:

.. code:: bash

  docker-compose up -d

.. |pythonversion| image:: https://img.shields.io/badge/python-3.7-blue.svg
   :target: https://www.python.org/
   :alt: Supported Python Versions
.. |version| image:: https://img.shields.io/badge/calver-2021.04.4-blue.svg
   :alt: CalVer format
.. |githubrepo| image:: https://img.shields.io/badge/GitHub-Repo-green.svg?longCache=true&style=flat
   :target: https://github.com/Atheuz/humanize-api
   :alt: Github Repo
