import os
from flask import Flask, request
from flask_weasyprint import *
from collections import namedtuple
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    params = namedtuple('params', request.get_json().keys())(**request.get_json())
    output_filepath = start(params.html_filepath, params.css_filepath, params.pdf_filename, params.data)
    if (output_filepath == False):
        return "Fail generating PDF file", 500
    else:
        return output_filepath


def start(template_file, css_file, output_file, template_vars):
    try:
        env = Environment(loader=FileSystemLoader('./templates/'))
        template = env.get_template(template_file)
        css = os.path.join('./templates/', css_file)
        html = weasyprint.HTML(string=template.render(**template_vars))
        html.write_pdf('./outputs/'+output_file, stylesheets=[css])
        return 'outputs/'+output_file
    except:
        return False
    


if __name__ == "__main__":
    app.run()