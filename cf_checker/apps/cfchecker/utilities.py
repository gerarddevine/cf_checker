from django.core.urlresolvers import reverse


# set up generic urls
def genurls():
    '''Creates a dictionary of general URL reversals
    
    '''
    
    urls = {}
    urls['home'] = reverse('home', args=())
    urls['about'] = reverse('about', args=())
    urls['news'] = reverse('news', args=())
    
    return urls
  