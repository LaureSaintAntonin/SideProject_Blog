from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here
def index(request):
	# Exemple de données à transmettre au modèle
	#context = {
		#'titre': 'Mon Blog',
		#'articles': ['Article 1', 'Article 2', 'Article 3']
		# Vous pouvez remplacer ceci par les vraies données de votre blog
	#}
	#return render(request, "blog/index.html", context)
	return render(request, "blog/index.html")

def article(request, numero_article):
	article = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[numero_article - 1]
	return render(request, f"blog/article_{numero_article}.html", {'article': article})
