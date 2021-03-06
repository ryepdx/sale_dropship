# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 RyePDX LLC (<http://www.ryepdx.com>).
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
#
{"name": "Simple Dropshipping",
 "version": "0.1",
 "author": "RyePDX LLC",
 "website": "http://www.ryepdx.com",
 "category": "Generic Modules/Purchase",
 "depends": ["purchase", "sale_stock", "mrp"],
 "description": "Allows drop-shipping products from suppliers to customers.",
 "data": ["product_view.xml", "sale_view.xml"],
 "test": ['test/setup.xml', 'test/product.yml', 'test/sale_line.yml', 'test/no_suppliers.yml'],
 'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
