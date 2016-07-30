from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse as hp
import utils


@api_view(['GET'])
def test_view(req):
    return Response("pong")

@api_view(['GET'])
def scrape_ques(req):
    bad_request = Response({"Error": "Bad Request !"}, status=400)
    if 'url' not in req.GET.keys() or not req.GET['url']:
        return bad_request
    res = Response(utils.scrape_web(req.GET['url']))
    return res if res else bad_request
