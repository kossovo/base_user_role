
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License

User roles
==========

This module was written to extend the standard functionality regarding users
and groups management.
It helps creating well-defined user roles and associating them to users.

A role is just a collection of groups. When a user is associated to a role,
its groups will be identical to the ones configured in the role.
In other words, roles make the user's groups *immutable*.

Configuration
=============

To configure this module, you need to go to *Configuration / Users / Roles*,
and create a new role. From there, you can add groups to compose your role,
and then associate users to it.

Credits
=======

Contributors
------------

* Sébastien Alix <sebastien.alix@osiell.com>
