# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

class ProductProduct(models.Model):
	_inherit = 'product.template'
	
	prix_vente_ref = fields.Float(string='Prix de vente de référence', compute='_compute_price')
	cout_achat_matmond = fields.Float(string='Cout à l\'achat', compute='_compute_cost')
	
	def _compute_cost(self):
		purchases = self.env['purchase.order.line'].search([('product_id.id','=',self.product_variant_id.id)])
		total = 0
		qty=0
		for purchase in purchases:
			qty = qty + purchase.product_qty
			total = total + purchase.price_unit
		self.cout_achat_matmond = total/qty

	def _compute_price(self):
		sales = self.env['sale.order.line'].search([('product_id.id','=',self.product_variant_id.id)])
		total = 0
		qty=0
		for sale in sales:
			qty = qty + sale.qty_to_invoice
			total = total + sale.price_unit
		self.prix_vente_ref = total/qty