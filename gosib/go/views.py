from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from models import Noun

@require_http_methods(['GET', 'POST'])
def handle_home(request):
    if request.method == 'GET':
        return render_home(request)
    elif request.method == 'POST':
        return shorten_url(request)

def render_home(request):
    return render_to_response('index.html')

def shorten_url(request):
    if 'url' not in request.POST:
        return HttpResponse(status=400)
    noun = Noun.objects.shorten(request.POST['url'])
    return HttpResponse(content=reverse(follow_redirect, args=(noun.noun,)),
                        content_type='text/plain')

@require_POST
def handle_shorten(request):
    if 'url' not in request.POST:
        redirect(reverse(handle_home))
    noun = Noun.objects.shorten(request.POST['url'])
    display_noun = '/{}/'.format(noun.noun)
    return render_to_response('index.html', {'noun': display_noun})


@require_GET
def follow_redirect(request, word):
    noun = get_object_or_404(Noun, noun=word, active=True)
    url = noun.url
    noun.follow()

    return redirect(url)
     
    
      

