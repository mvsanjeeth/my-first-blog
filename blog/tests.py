from django.test import TestCase

# Create your tests here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
