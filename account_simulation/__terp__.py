# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Accounting simulation journal",
    "version" : "1.0",
    "depends" : ["account"],
    "author" : "Tiny",
    "description": """Accounting simulation plan.""",
    "website" : "http://tinyerp.com/module_account.html",
    "category" : "Generic Modules/Accounting",
    "init_xml" : [
    ],
    "demo_xml" : [
        "account_simulation_demo.xml"
    ],
    "update_xml" : [
        "security/ir.model.access.csv",
        "account_simulation_view.xml"
    ],
#   "translations" : {
#       "fr": "i18n/french_fr.csv"
#   },
    "active": False,
    "installable": True,
    "certificate": "1004751193784519293"
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

