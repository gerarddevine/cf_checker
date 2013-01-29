from django import forms


class CFForm(forms.Form):
    ''' simple form class for NetCDF file uploading
    
    '''
    Versions = (('--------------','-------------'),
               ('10','1.0'),
               ('11','1.1'),
               ('12','1.2'),
               ('13','1.3'),
               ('14','1.4'),
               ('15','1.5'),)
    
    cffile = forms.FileField(required=False)
    cfversion = forms.CharField(widget=forms.Select(choices=Versions, attrs={'size':'1', 'class':'input-xlarge'}))
    igWarnings = forms.BooleanField(required=False)
