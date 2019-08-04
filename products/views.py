from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product

# Create your views here.
def home(request):
	products = Product.objects
	return render(request, 'products/home.html', {'products':products})

@login_required(login_url='/accounts/signup')
def create(request):
	if request.method == 'POST':
		file = request.FILES
		docs = request.POST
		if file.get('myimage', False) and file.get('myicon', False) and docs['title'] and docs['body'] and docs['url']:
			
			product = Product();
			product.title = docs['title']
			product.body = docs['body']
			product.icon = file.get('myicon', False)
			product.image = file.get('myimage', False)

			if docs['url'].startswith('http://') or docs['url'].startswith('https://'):
				product.url = docs['url']
			else:
				product.url = "http://" + docs['url']

			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			
			return redirect('/products/' + str(product.id))
		else:
			return render(request, 'products/create.html', {'error':'All fields are required'})
	else:
		return render(request, 'products/create.html')


def details(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/details.html', {'product':product})

@login_required(login_url='/accounts/signup')
def upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect('/products/' + str(product.id))
