# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Fornecedor(models.Model):
	class Meta:
		verbose_name_plural = 'Fornecedores'
		verbose_name = 'Fornecedor'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	username = models.CharField(verbose_name = 'username', max_length = 100)

	def __unicode__(self):
		return self.nome

class Cliente(models.Model):
	class Meta:
		verbose_name_plural = 'Clientes'
		verbose_name = 'Cliente'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	username = models.CharField(verbose_name = 'username', max_length = 100)

	def __unicode__(self):
		return self.nome

class DocumentoFornecedor(models.Model):
	class Meta:
		verbose_name_plural = 'Documentos'
		verbose_name = 'Documento'

	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 25, decimal_places = 0, default=0 ) 
	emissao = models.DateTimeField(verbose_name = 'Emissao',auto_now = False, auto_now_add = True)
	vencimento = models.DateTimeField(verbose_name = 'Vencimento',auto_now = False, auto_now_add = True)
	fornecedor = models.ForeignKey(Fornecedor)

	def __unicode__(self):
		return self.tipo

class EnderecoFornecedor(models.Model):
	class Meta:
		verbose_name_plural = 'Enderecos'
		verbose_name = 'Endereco'

	cep = models.DecimalField(verbose_name = 'Cep', max_digits = 15, decimal_places = 0, default=0 ) 
	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	descricao = models.CharField(verbose_name = 'Descricao', max_length = 2048, default="nulo")
	complemento = models.CharField(verbose_name = 'Complemento', max_length = 2048, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 10, decimal_places = 0, default=0 ) 
	fornecedor = models.ForeignKey(Fornecedor)

	def __unicode__(self):
		return self.tipo


class EmailFornecedor(models.Model):
	class Meta:
		verbose_name_plural = 'Emails'
		verbose_name = 'Email'

	descricao = models.EmailField()
	fornecedor = models.ForeignKey(Fornecedor)

	def __unicode__(self):
		return self.descricao


class DocumentoCliente(models.Model):
	class Meta:
		verbose_name_plural = 'Documentos'
		verbose_name = 'Documento'

	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 25, decimal_places = 0, default=0 ) 
	emissao = models.DateTimeField(verbose_name = 'Emissao',auto_now = False, auto_now_add = True)
	vencimento = models.DateTimeField(verbose_name = 'Vencimento',auto_now = False, auto_now_add = True)
	ativo = models.BooleanField(verbose_name='Ativo')
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.tipo

class EnderecoCliente(models.Model):
	class Meta:
		verbose_name_plural = 'Enderecos'
		verbose_name = 'Endereco'

	cep = models.DecimalField(verbose_name = 'Cep', max_digits = 15, decimal_places = 0, default=0 ) 
	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	descricao = models.CharField(verbose_name = 'Descricao', max_length = 2048, default="nulo")
	complemento = models.CharField(verbose_name = 'Complemento', max_length = 2048, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 10, decimal_places = 0, default=0 ) 
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.tipo


class EmailCliente(models.Model):
	class Meta:
		verbose_name_plural = 'Emails'
		verbose_name = 'Email'

	descricao = models.EmailField()
	cliente = models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.descricao

class Financeiro(models.Model):
	class Meta:
		verbose_name_plural = 'Finaceiros'
		verbose_name = 'Financeiro'

	parcela = models.DecimalField(verbose_name = 'Parcela', max_digits = 3, decimal_places = 0, default=1 ) 
	valorparcela = models.DecimalField(verbose_name = 'ValorParcela', max_digits = 10, decimal_places = 0, default=0 ) 
	quantidade = models.DecimalField(verbose_name = 'Quantidade', max_digits = 10, decimal_places = 0, default=1 ) 
	valor_pago = models.DecimalField(verbose_name = 'Valor_pago', max_digits = 10, decimal_places = 0, default=0 ) 
	
	def __unicode__(self):
		return self.valorparcela

class Produto(models.Model):
	class Meta:
		verbose_name_plural = 'Produtos'
		verbose_name = 'Produto'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	valor = models.DecimalField(verbose_name = 'Valor', max_digits = 100000000000, decimal_places = 0, default=0)
	foto = models.ImageField(upload_to='produto/', height_field=None, width_field=None, max_length=100000,blank=True,null=True, default = "fornecedor/static/imagens/default.jpg")
	descricao = models.CharField(verbose_name = 'Descricao', max_length = 500, default="nulo") 
	estoque = models.DecimalField(verbose_name = 'Estoque', max_digits = 100000000000, decimal_places = 0, default=0 ) 
	def __unicode__(self):
		return self.nome

class VendaProduto(models.Model):
	class Meta:
		verbose_name_plural = 'Vendas'
		verbose_name = 'Venda'

	produto = models.ForeignKey(Produto)
	username = models.CharField(verbose_name = 'username', max_length = 100,default="nulo") 
	parcela = models.DecimalField(verbose_name = 'Parcela', max_digits = 3, decimal_places = 0, default=1 ) 
	valorparcela = models.DecimalField(verbose_name = 'ValorParcela', max_digits = 100000000000, decimal_places = 0, default=0 ) 
	quantidade = models.DecimalField(verbose_name = 'Quantidade', max_digits = 100000000000, decimal_places = 0, default=1 ) 
	valor_pago = models.DecimalField(verbose_name = 'Valor_pago', max_digits = 100000000000, decimal_places = 0, default=0 ) 
	
	def __unicode__(self):
		return self.produto.nome