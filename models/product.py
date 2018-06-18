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
		min = None
		moyenne = 0
		for purchase in purchases:
			if min==None or min>purchase.price_unit:
				min=purchase.price_unit
			qty = qty + purchase.product_qty
			total = total + purchase.price_unit
		if qty == 0:
			self.cout_achat_matmond = 0
		else:
			moyenne = total/qty
			self.cout_achat_matmond = (0.85*(moyenne+min)/2)*0.5
		
	def _compute_price(self):
		purchases = self.env['purchase.order.line'].search([('product_id.id','=',self.product_variant_id.id)])
		total = 0
		qty=0
		min = None
		moyenne = 0
		for purchase in purchases:
			if min==None or min>purchase.price_unit:
				min=purchase.price_unit
			qty = qty + purchase.product_qty
			total = total + purchase.price_unit
		if qty == 0:
			self.prix_vente_ref = 0
		else:
			moyenne = total/qty
			self.prix_vente_ref = 0.85*(moyenne+min)/2
