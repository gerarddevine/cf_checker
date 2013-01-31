from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext

from cf_checker.apps.cfchecker.forms import CFForm
from cf_checker.apps.cfchecker.utilities import genurls
from cf_checker.apps.cfchecker.cfmanager import checkCF, translateMM
from cf_checker.apps.cfchecker.cfchecker_dummy import CFChecker


def home(request):
    '''Controller for app home page
    
    Acts as the cf file upload page. 
    '''
  
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
      
    if request.method == 'POST':
        cfform = CFForm(request.POST, request.FILES)
        if cfform.is_valid():
            # Grab the uploaded netcdf file
            cffile = request.FILES['uploadedfile']
            # Which version does the user want to check against?
            cfversion = cfform.cleaned_data['cfversion']
            # Is it only header data to be used?
            headeronly = cfform.cleaned_data['headeronly']
            # Pass the file and options to the checking script  
            inst = CFChecker(version=cfversion)
            report = inst.checker(cffile)
                        
            return render_to_response('page/report.html', {'urls': urls, 'report': report, }, 
                                       context_instance=RequestContext(request))
                             
        else:
            # TODO: Need to put in better handling here
            return HttpResponseRedirect(urls['home'])
    else:
        cfform = CFForm()      
    
    return render_to_response('page/home.html', {'urls': urls, 'cfform': cfform},
                              context_instance=RequestContext(request))


def about(request):
    '''Controller for app about page
    
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
      
    return render_to_response('page/about.html', {'urls': urls},
                              context_instance=RequestContext(request))


def news(request):
    '''Controller for app news page
    
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
      
    return render_to_response('page/news.html', {'urls': urls},
                              context_instance=RequestContext(request))
