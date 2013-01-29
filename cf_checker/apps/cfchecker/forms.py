from django import forms


class CFForm(forms.Form):
    ''' 
    Simple form class for NetCDF file uploading with associated options
    
    '''
    
    # list of available cf versions to run the check against
    Versions = (
               ('1.0', '1.0'),
               ('1.1', '1.1'),
               ('1.2', '1.2'),
               ('1.3', '1.3'),
               ('1.4', '1.4'),
               ('1.5', '1.5'),
               )
    
    # the actual cf file
    cffile = forms.FileField(required=False)
    # CF version to check against
    cfversion = forms.FloatField(widget=forms.Select(choices=Versions, attrs={'size':'1', 'class':'input-xlarge'}))
    # only using the header info for cf checker
    headeronly = forms.BooleanField(required=False)
