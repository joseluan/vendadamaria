# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from fornecedor.models import *
from fornecedor.forms import *

def fornecedorlogon(request):
	user = request.user 
	try:
		fornecedores = Fornecedor.objects.get(username=user.username)
		return True
	except Exception:
		return False

def clientelogon(request):
	user = request.user 
	try:
		Cliente = Cliente.objects.get(username=user.username)
		return True
	except Exception:
		return False
	


@login_required(login_url='/entrar/')
def fornecedores(request):
	if fornecedorlogon(request):
		user = request.user 
		emails = EmailFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		documentos = DocumentoFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		enderecos = EnderecoFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		return render(request,'fornecedores.html',{
			'emails': emails,
			'documentos': documentos,
			'enderecos': enderecos,
			})
	return HttpResponseRedirect('/')



@login_required(login_url='/entrar/')
def clientes(request):
	if fornecedorlogon(request):
		user = request.user 
		emails = EmailFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		documentos = DocumentoFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		enderecos = EnderecoFornecedor.objects.filter(fornecedor=Fornecedor.objects.get(username=user.username))
		return render(request,'clientes.html',{
			'emails': emails,
			'documentos': documentos,
			'enderecos': enderecos,
			})
	if clientelogon(request):
		user = request.user 
		emails = EmailCliente.objects.filter(cliente=Cliente.objects.get(username=user.username))
		documentos = DocumentoCliente.objects.filter(cliente=Cliente.objects.get(username=user.username))
		enderecos = EnderecoCliente.objects.filter(cliente=Cliente.objects.get(username=user.username))
		return render(request,'clientes.html',{
			'emails': emails,
			'documentos': documentos,
			'enderecos': enderecos,
			})
	return HttpResponseRedirect('/')

def entrar(request):
	if clientelogon or fornecedorlogon:	
		if request.method=='POST':
			cusuario = request.POST.get("usuario")
			csenha = request.POST.get("senha")

			user = authenticate(username=cusuario, password=csenha)
			if user is not None:
				if user.is_active:
					login(request, user)
					request.session['usuario'] = cusuario
					return HttpResponseRedirect('/') 
				else:
					return HttpResponseRedirect('/') 
			else:
				
				return HttpResponseRedirect('/')   

		return render(request,'entrar.html',{
			'usuario': True,
			})
	return render(request,'entrar.html',{
			'usuario': True,
			})


def index(request):
	if request.method=='POST':
		produtos = Produto.objects.filter(nome__contains=request.POST.get("pesquisa"))
		paginator = Paginator(produtos, 20) 
	    
		page = request.GET.get('page')
		lista_produtos = []
		try:
			lista_produtos = paginator.page(page)
		except PageNotAnInteger:
			lista_produtos = paginator.page(1)
		except EmptyPage:
			lista_produtos = paginator.page(paginator.num_pages)

		return render(request,'index.html',{'produtos': lista_produtos})

	else:
		produtos = Produto.objects.all()
		paginator = Paginator(produtos, 20) 
	    
		page = request.GET.get('page')
		lista_produtos = []
		try:
			lista_produtos = paginator.page(page)
		except PageNotAnInteger:
			lista_produtos = paginator.page(1)
		except EmptyPage:
			lista_produtos = paginator.page(paginator.num_pages)

		return render(request,'index.html',{'produtos': lista_produtos})



@login_required(login_url='/entrar/')
def adicionaremail(request):
	if fornecedorlogon(request):
		if request.method == 'POST':	
			try:
				forn = Fornecedor.objects.get(username=request.user.username)
				EmailFornecedor.objects.create(descricao= request.POST.get("email"),fornecedor=forn).save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionaremail.html',{})
		return render(request,'adicionaremail.html',{})	

	if clientelogon(request):
		if request.method == 'POST':	
			try:
				EmailCliente.objects.create(descricao= request.POST.get("email"),cliente=Cliente.objects.get(username=request.user.username)).save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionaremail.html',{})
		return render(request,'adicionaremail.html',{})

	return HttpResponseRedirect('/')


@login_required(login_url='/entrar/')
def adicionardocumento(request):
	if fornecedorlogon(request):
		if request.method == 'POST':	
			try:
				forn = Fornecedor.objects.get(username=request.user.username)
				DocumentoFornecedor.objects.create(tipo= request.POST.get("tipo"), numero=request.POST.get("numero"),emissao=request.POST.get("emissao"), vencimento=request.POST.get("vencimento"), fornecedor=forn).save()
				return HttpResponseRedirect('/fornecedores/') 
			except Exception, e:
				return render(request,'adicionardocumento.html',{})
		return render(request,'adicionardocumento.html',{})	

	if clientelogon(request):
		if request.method == 'POST':	
			try:
				cliente = Cliente.objects.get(username=request.user.username)
				DocumentoCliente.objects.create(tipo= request.POST.get("tipo"), numero=request.POST.get("numero"),emissao=request.POST.get("emissao"), vencimento=request.POST.get("vencimento"), cliente=cliente).save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionardocumento.html',{})
		return render(request,'adicionardocumento.html',{})

	return HttpResponseRedirect('/')


@login_required(login_url='/entrar/')
def adicionarendereco(request):
	if fornecedorlogon(request):
		if request.method == 'POST':	
			try:
				forn = Fornecedor.objects.get(username=request.user.username)
				EnderecoFornecedor.objects.create(cep= request.POST.get("cep"), tipo=request.POST.get("tipo"),descricao=request.POST.get("descricao"), complemento=request.POST.get("complemento"), numero=request.POST.get("numero"), fornecedor=forn).save()
				return HttpResponseRedirect('/fornecedores/') 
			except Exception, e:
				return render(request,'adicionarendereco.html',{})
		return render(request,'adicionarendereco.html',{})	

	if clientelogon(request):
		if request.method == 'POST':	
			try:
				cliente = Cliente.objects.get(username=request.user.username)
				EnderecoCliente.objects.create(cep= request.POST.get("cep"), tipo=request.POST.get("tipo"),descricao=request.POST.get("descricao"), complemento=request.POST.get("complemento"), numero=request.POST.get("numero"), cliente=cliente).save()
				return HttpResponseRedirect('/fornecedores/') 
			except Exception, e:
				return render(request,'adicionarendereco.html',{})
		return render(request,'adicionarendereco.html',{})

	return HttpResponseRedirect('/')



@login_required(login_url='/entrar/')
def adicionarfornecedor(request):
	if request.method == 'POST':
		criar = True
		for user in User.objects.all():
			if user.username == request.POST.get("username"):
				criar = False
		if criar:	
			try:
				user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
				user.is_superuser = True
				user.is_active = True
				user.is_staff = True
				user.is_admin = True
				user.save()
				fornecedor = Fornecedor.objects.create(username=request.POST.get("username"),nome=request.POST.get("nome"))
				fornecedor.save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return HttpResponseRedirect('/vendas/')
	return render(request,'adicionarfornecedor.html',{})


@login_required(login_url='/entrar/')
def adicionarcliente(request):
	if request.method == 'POST':
		criar = True
		for user in User.objects.all():
			if user.username == request.POST.get("username"):
				criar = False
		if criar:	
			try:
				user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
				user.is_superuser = True
				user.is_active = True
				user.save()
				cliente = Cliente.objects.create(username=request.POST.get("username"),nome=request.POST.get("nome"))
				cliente.save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionarcliente.html',{})
	return render(request,'adicionarcliente.html',{})


@login_required(login_url='/entrar/')
def vendas(request):
	if request.method == 'POST':
		if fornecedorlogon(request):
			
			vendas = VendaProduto.objects.filter(produto__nome__contains=request.POST.get("pesquisa"),username=request.user.username)
			paginator = Paginator(vendas,20) 
		    
			page = request.GET.get('page')
			lista_vendas = []
			try:
				lista_vendas = paginator.page(page)
			except PageNotAnInteger:
				lista_vendas = paginator.page(1)
			except EmptyPage:
				lista_vendas = paginator.page(paginator.num_pages)

			return render(request,'vendas.html',{'vendas': lista_vendas})

		if clientelogon(request):
			
			vendas = VendaProduto.objects.filter(produto__nome__contains=request.POST.get("pesquisa"),username=request.user.username)
			paginator = Paginator(vendas,20) 
		    
			page = request.GET.get('page')
			lista_vendas = []
			try:
				lista_vendas = paginator.page(page)
			except PageNotAnInteger:
				lista_vendas = paginator.page(1)
			except EmptyPage:
				lista_vendas = paginator.page(paginator.num_pages)

			return render(request,'vendas.html',{'vendas': lista_vendas})

		return HttpResponseRedirect('/') 
	vendas = VendaProduto.objects.filter(username=request.user.username)
	paginator = Paginator(vendas,20) 
		    
	page = request.GET.get('page')
	lista_vendas = []
	try:
		lista_vendas = paginator.page(page)
	except PageNotAnInteger:
		lista_vendas = paginator.page(1)
	except EmptyPage:
		lista_vendas = paginator.page(paginator.num_pages)
	return render(request,'vendas.html',{'vendas': lista_vendas})


@login_required(login_url='/entrar/')
def vendaspagar(request,pk):
	venda = VendaProduto.objects.get(id=pk)
	if request.method == 'POST':
		venda.valor_pago += venda.valorparcela
		venda.parcela -= 1
		venda.save()
		if venda.valor_pago >= venda.produto.valor or venda.parcela <= 0:
			venda.delete()
		return HttpResponseRedirect('/vendas/')
	return render(request,'pagarvenda.html',{'venda': venda})


@login_required(login_url='/entrar/')
def emailexcluir(request,pk):
	if fornecedorlogon(request):
		EmailFornecedor.objects.get(id=pk).delete()
	return HttpResponseRedirect('/fornecedores/')


@login_required(login_url='/entrar/')
def documentoexcluir(request,pk):
	if fornecedorlogon(request):
		DocumentoFornecedor.objects.get(id=pk).delete()
	return HttpResponseRedirect('/fornecedores/')


@login_required(login_url='/entrar/')
def enderecoexcluir(request,pk):
	if fornecedorlogon(request):
		EnderecoFornecedor.objects.get(id=pk).delete()
	return HttpResponseRedirect('/fornecedores/')


@login_required(login_url='/entrar/')
def vendasexcluir(request,pk):
	if fornecedorlogon(request):
		VendaProduto.objects.get(id=pk).delete()
	return HttpResponseRedirect('/vendas/')

@login_required(login_url='/entrar/')
def produtoexcluir(request,pk):
	Produto.objects.get(id=pk).delete()
	return HttpResponseRedirect('/vendas/')


@login_required(login_url='/entrar/')
def comprar(request,pk):
	
	if fornecedorlogon(request):
		user = request.user
		fornecedor = Fornecedor.objects.get(username=user.username)
		if request.method == 'POST':
			
			prodt = Produto.objects.get(id=pk)
			prodt.valor = request.POST.get("totalfinal")
			prodt.save()
			VendaProduto.objects.create(produto = prodt,username=fornecedor.username, quantidade=request.POST.get("quantidade"), valorparcela=request.POST.get("total"), parcela=request.POST.get("parcelas")).save()
			prodt = Produto.objects.get(id=pk)
			prodt.estoque -= int(request.POST.get("quantidade"))
			prodt.save()
			if prodt.estoque <= 0:
				prodt.delete()
			return HttpResponseRedirect('/')

		else:
			return render(request,'comprar.html',{
				'produto': Produto.objects.get(id=pk),
				'fornecedor':fornecedor,
				})
	if clientelogon(request):
		user = request.user
		cliente = Cliente.objects.get(username=user.username)
		if request.method == 'POST':
			
			prodt = Produto.objects.get(id=pk)
			prodt.valor = request.POST.get("totalfinal")
			prodt.save()
			VendaProduto.objects.create(produto = prodt,username=cliente.username, quantidade=request.POST.get("quantidade"), valorparcela=request.POST.get("total"), parcela=request.POST.get("parcelas")).save()
			prodt = Produto.objects.get(id=pk)
			prodt.estoque -= int(request.POST.get("quantidade"))
			prodt.save()
			if prodt.estoque <=0:
				prodt.delete()
			return HttpResponseRedirect('/')

		else:
			return render(request,'comprar.html',{
				'produto': Produto.objects.get(id=pk),
				'fornecedor':cliente,
				})
	return HttpResponseRedirect('/')


def editarproduto(request,pk):
	if fornecedorlogon(request):
		if request.method == 'POST':
			p = Produto.objects.get(id=pk)
			p.valor = request.POST.get("valor")
			p.nome = request.POST.get("nome")
			p.descricao = request.POST.get("descricao")
			p.estoque = request.POST.get("estoque")
			p.save()
		produto = Produto.objects.get(id=pk)
		return render(request,'editarproduto.html',{'produto':produto})
	else:
		produto = Produto.objects.get(id=pk)
		return render(request,'editarproduto.html',{'produto':produto})


@login_required(login_url='/entrar/')
def adicionarproduto(request):
	if fornecedorlogon(request):
	    if request.method == 'POST':
	        form = ImageUploadForm(request.POST, request.FILES)
	        if form.is_valid():
			    p = Produto.objects.create(foto=form.cleaned_data['image'])
			    p.valor = request.POST.get("valor")
			    p.nome = request.POST.get("nome")
			    p.descricao = request.POST.get("descricao")
			    p.estoque = request.POST.get("estoque")
			    p.save()
                return HttpResponseRedirect('/') 	
        return render(request,'adicionarproduto.html',{})
	return HttpResponseRedirect('/') 

def sair(request):
	logout(request)
	return HttpResponseRedirect('/') 