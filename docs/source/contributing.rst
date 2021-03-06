Contributing to plone.restapi
=============================

Generating documentation examples
---------------------------------

This documentation includes examples of requests and responses (http, curl, httpie and python-requests).
These examples are generated by the documentation tests in ``test_documentation.py``.
To generate a new example, add a new test case to `test_documentation.py` - for example ``test_documentation_search_fullobjects``, and run the test:

``./bin/test -t test_documentation_search_fullobjects``

This generates the request and the response files in ``tests/http-examples/``.

Include them in the documentation like this:

.. code-block:: ReST

    ..  http:example:: curl httpie python-requests
        :request: ../../src/plone/restapi/tests/http-examples/search_fullobjects.req

    .. literalinclude:: ../../src/plone/restapi/tests/http-examples/search_fullobjects.resp
       :language: http


Build the sphinx docs locally to test the rendering by running ``./bin/sphinxbuilder``.

Make sure you add and commit the generated files in ``http-examples``.
