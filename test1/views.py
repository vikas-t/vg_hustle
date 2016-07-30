from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse as hp
import utils


@api_view(['GET'])
def test_view(req):
	return Response("hello")

def test_view2(req):
	return hp('okay this is working')

@api_view(['GET'])
def scrape_ques(req):
	return Response(utils.scrap_web())
