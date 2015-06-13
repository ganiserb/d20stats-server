from django.shortcuts import render
from django.http.response import HttpResponse, FileResponse


# Create your views here.
def test(request):
    return HttpResponse('test ok!')


def crossdomain(request):
    response = FileResponse("""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE cross-domain-policy
  SYSTEM 'http://www.adobe.com/xml/dtds/cross-domain-policy.dtd'>
<cross-domain-policy>
	<allow-access-from domain="d20s.herokuapp.com"/>
	<allow-http-request-headers-from domain="d20s.herokuapp.com" headers="Authorization"/>
</cross-domain-policy>
""")
    response['Content-Type'] = "text/x-cross-domain-policy; charset=utf-8"
    return response