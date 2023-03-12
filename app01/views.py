from django.shortcuts import render,HttpResponse
import mistune
import requests
import json
import re
import openai

# Create your views here.

def ai(question):
    openai.api_key="your openai key"
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"user",
            "content":question,
        }
        ]
    )
    response=completion.choices[0].message
    content=response.content
    return content


def index(request):
    if request.method == "POST":
        try:
            question=request.POST.get("opt")
            data=ai(question)
            answer=mistune.html(data)
        except Exception:
            answer="抱歉：API已被停用。"
        return  HttpResponse(answer)
    return render(request,"showdown.html")

