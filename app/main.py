from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from PIL import Image
import matplotlib.pyplot as plt
import io

from . import githubApi
# from tkinter import *

app = FastAPI()


@app.get('/')
def index():
    return {"data": "Hello FastAPI"}


@app.get('/bar')
def barPlot():
    return Response(content=githubApi.bar_plot(), media_type='image/png')
