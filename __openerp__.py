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
    'description': """This module was written to extend the standard
functionality regarding users and groups management.
It helps creating well-defined user roles and associating them to users.

A role is just a collection of groups. When a user is associated to a role,
its groups will be replaced to the ones configured in the role.
In other words, roles make the user's groups *immutable*.
    """,
    'author': 'ABF OSIELL',
    'maintainer': 'ABF OSIELL',
    'website': 'http://www.osiell.com',
    'depends': [
        'base',
    ],
    'data': [
        'views/role.xml',
        'views/user.xml',
    ],
    'installable': True,
    'auto_install': False,
}
