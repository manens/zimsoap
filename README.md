ZimSOAP : a programmatic python interface to zimbra
===================================================

ZimSOAP allows to access the [SOAP Zimbra API] through a programmatic,
data-type-aware  interface high-level. It also handle  authentification,
sessions, pre-authentication and delegated authentication.

Not all methods are covered, but you're welcome to wrap the ones you need and
pull-request !

If you are looking at a lower-level lib, you better look to [python-zimbra]

Allows accessing zimbraAdmin and zimbraAccount SOAP APIs

 - handle authentification
 - handle pre-authentification admin->admin and admin->Account
 - presents the request results as nice Python objects
 - all requests are tested with 8.0.4 and 8.0.5

[SOAP Zimbra API]:
http://files.zimbra.com/docs/soap_api/8.0.4/soap-docs-804/api-reference/index.html
[python-zimbra]:https://github.com/Zimbra-Community/python-zimbra/

Installing
----------

**Till [this PR](https://github.com/Zimbra-Community/python-zimbra/pull/16) is
  worked out and released, requires a patched version of python-zimbra**.

Install it with :

    pip install git+https://github.com/oasiswork/python-zimbra.git@utf-encoding-requests

Simple:

    pip install zimsoap

Or if you fetch it from git:

    ./setup.py install

API
---

API is accessible through the ZimbraAdminClient() method. Example :

    zc = ZimbraAdminClient('myserver.example.tld')
    zc.login('username@domain.tld', 'mypassword')

    print("Domains on that zimbra instance :")
    for domain in zc.get_all_domains():
        # Each domain is a zobject.Domain instance
        print('  - %s' % domain.name)

You can also access raw SOAP methods:

    zc = ZimbraAdminClient()
    zc.login('username@domain.tld', 'mypassword')
    xml_response = self.zc.GetAllDomainsRequest()


If you want up-to-date code example, look at unit tests...


Testing
-------

### Setting your environment for tests ###


#### Dependencies ####

The first time you want to run tests, you have to grab submodules:

    $ git submodule update --init

The SOAP API tests are ran against a reference machine, so you have to grab,
provision and run it, thanks to vagrant, it's pretty straightforward (but a bit
of download time the first time) :

    $ sudo apt-get install vagrant
    $ cd zimsoap/tests/machines/
    $ vagrant up 8.0.5
    $ vagrant provision 8.0.5

You have several zimbra versions available as VMs for testing (see vagrant
status).

*Warning*: the test VM requires 2GB RAM to function properly.


### Testing ###

Make sure your vagrant vm is running `vagrant status`.

Code is covered by unit tests, you can run them (only Python needed):

    $ python -m unittest discover

To run only some tests, for example :

    $ python -m unittest test.test_zobjects
    $ python -m unittest test.test_zobjects.ZObjectTests
    $ python -m unittest test.test_zobjects.ZObjectTests.testDomainSelector
