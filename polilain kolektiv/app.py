from flask import Flask, render_template, url_for, request
from math import ceil
import os

app = Flask(__name__)

@app.route('/')
def render_home():
    imageList = []
    for image in os.listdir('static/projects'):
        imageList.append(['projects/' + image, image.split('.')[0]])
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 6, type=int)
    pages = ceil(len(imageList) / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    return render_template('home.html', imageList=imageList[start:end], page=page, pages=pages)
    
@app.route('/project/<projectname>')
def project(projectname):
    folder_path = 'static/images/'+projectname
    image_files = os.listdir(folder_path)
    number_of_images = len(image_files)
    imageList = []
    for image in os.listdir('static/images/'+projectname):
        imageList.append(['images/'+projectname+'/' + image, image.split('.')[0]])
    return render_template('project.html', projectname=projectname, imageList=imageList, number_of_images=number_of_images, images_folder='images')


@app.route('/about-us')
def render_about():
    return render_template('about-us.html')

app.run(debug=True)
