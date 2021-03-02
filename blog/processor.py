from blog.models import Category, Article

def get_categorias(request):
    ids = Article.objects.filter(public=True).values_list('categories',flat=True)
    categorias = Category.objects.filter(id__in=ids).values_list('id', 'name')
    return {
        'categorias':categorias,
        'ids': ids
    }