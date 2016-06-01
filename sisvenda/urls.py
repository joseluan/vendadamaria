# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': './static/',}),
    url(r'^$', 'fornecedor.views.index', name='index'),
    url(r'^entrar/','fornecedor.views.entrar',name='entrar'),
    url(r'^sair/','fornecedor.views.sair',name='sair'),
    url(r'^adicionar_fornecedor/', 'fornecedor.views.adicionarfornecedor', name='adicionar_fornecedor'),
    url(r'^adicionar_cliente/', 'fornecedor.views.adicionarcliente', name='adicionar_cliente'),
    url(r'^fornecedores/', 'fornecedor.views.fornecedores', name='fornecedores'),
    url(r'^clientes/', 'fornecedor.views.clientes', name='clientes'),
    url(r'^adicionar_produto/', 'fornecedor.views.adicionarproduto', name='adicionar_produto'),
    url(r'^editarproduto/(?P<pk>[0-9]+)/$', 'fornecedor.views.editarproduto', name='editar_produto'),
    url(r'^adicionar_email/', 'fornecedor.views.adicionaremail', name='adicionar_email'),
    url(r'^adicionar_documento/', 'fornecedor.views.adicionardocumento', name='adicionar_documento'),
    url(r'^adicionar_endereco/', 'fornecedor.views.adicionarendereco', name='adicionar_endereco'),
    url(r'^vendas/', 'fornecedor.views.vendas', name='vendas'),
    url(r'^vendasexcluir/(?P<pk>[0-9]+)/$', 'fornecedor.views.vendasexcluir', name='vendas_excluir'),
    url(r'^emailexcluir/(?P<pk>[0-9]+)/$', 'fornecedor.views.emailexcluir', name='email_excluir'),
    url(r'^documentoexcluir/(?P<pk>[0-9]+)/$', 'fornecedor.views.documentoexcluir', name='documento_excluir'),
    url(r'^enderecoexcluir/(?P<pk>[0-9]+)/$', 'fornecedor.views.enderecoexcluir', name='endereco_excluir'),
    url(r'^comprar/(?P<pk>[0-9]+)/$', 'fornecedor.views.comprar', name='comprar'),
    url(r'^vendaspagar/(?P<pk>[0-9]+)/$', 'fornecedor.views.vendaspagar',name='vendas_pagar'),
]

