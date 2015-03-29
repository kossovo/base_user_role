# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 ABF OSIELL SARL (http://osiell.com).
#                       Sebastien Alix <contact@osiell.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'User roles',
    'version': '1.0',
    'category': 'Tools',
    'description': """
User roles
==========

This module was written to extend the standard functionality regarding users
and groups management.
It helps creating well-defined user roles and associating them to users.

It can become very hard to maintain a large number of user profiles over time,
juggling with many technical groups. For this purpose, this module will help
you to:

  * defining functional roles by aggregating low-level groups,
  * setting user accounts with the predefined roles (roles are cumulative),
  * updating groups of all relevant user accounts (all at once),
  * ensuring that user accounts will have the groups defined in their roles
    (nothing more, nothing less). In other words, you can not set groups
    manually on a user as long as there is roles configured on it,
  * getting a quick overview of roles and the related user accounts.

That way you make clear the different responsabilities within a company, and
are able to add and update user accounts in a scalable and reliable way.
    """,
    'author': 'ABF OSIELL',
    'maintainer': 'ABF OSIELL',
    'website': 'http://www.osiell.com',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/role.xml',
        'views/user.xml',
    ],
    'installable': True,
    'auto_install': False,
}
