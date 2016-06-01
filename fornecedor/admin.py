# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

admin.site.register(DocumentoFornecedor)
admin.site.register(EnderecoFornecedor)
admin.site.register(EmailFornecedor)
admin.site.register(DocumentoCliente)
admin.site.register(EnderecoCliente)
admin.site.register(EmailCliente)
admin.site.register(Produto)
admin.site.register(Financeiro)
admin.site.register(VendaProduto)
admin.site.register(Fornecedor)
admin.site.register(Cliente)