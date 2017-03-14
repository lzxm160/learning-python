# coding: utf8
"""
    flask_weasyprint.test_app
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    Demonstration and testing application for Flask-WeasyPrint.
    :copyright: (c) 2012 by Simon Sapin.
    :license: BSD, see LICENSE for more details.
"""

from flask import (Flask, render_template, request, abort, redirect, url_for,
                   Response)

try:
    unicode
except NameError:  # Python 3
    unicode = str


def run():
    """A more involved application, with a dynamic SVG graph.
    Run it with ``python -m flask_weasyprint.test_app`` or have a look
    at the source code.
    """
    app.run(host='0.0.0.0', port=80,debug=True)
# This function exits mostly to make a "view source" link in the docs.


# Disable the Flask’s default static file handling. (See below.)
app = Flask(__name__, static_folder=None)


### This is a pretty standard Flask app with a dynamic SVG graph.
### Of course the data here is always the same, but in a real app
### it could come from a database or be computed on the fly.
### We could also make prettier graphs with Pygal: http://pygal.org/


@app.config.from_object
class Config:
    GRAPH_COLORS = ['#0C3795', '#752641', '#E47F00']


@app.route('/')
def index():
    return redirect(url_for('document_html'))


@app.route('/foo/')
def document_html():
    return render_template(
        'document.html', data=[42, 27.3, 63], labels=['Lorem', 'ipsum', 'sit'])

### The code specific to Flask-WeasyPrint follows. Pretty simple, eh?

from flask_weasyprint import render_pdf, HTML


@app.route('/foo.pdf')
def document_pdf():
    return render_pdf(url_for('index'))


### End of code specific to Flask-WeasyPrint.


### The templates and static files are inlined here and served from memory.
### This is a bit unusual but allows us to keep this app in a single file.
### We could just as well use normal templates and static files.

from jinja2 import DictLoader

app.jinja_env.loader = DictLoader({
    'document.html': '''
        <!doctype html>
        <title>Test document</title>
        <link rel=stylesheet href="{{ url_for('static',
                                              filename='style.css') }}" />
        <body>
        <section>
            <nav>Get this document <a href="/pdf">as PDF</a></nav>
            
        </section>
    ''',
})


STATIC_FILES = {'style.css': ('text/css', '''
    html { font-family: Fontin Sans, sans-serif }
    section { width: 80%; margin: 2em auto }
    a { color: inherit }
    img { width: 100%; max-width: 600px; box-sizing: border-box;
         border: 1px solid #888; }
    /* Print-specific styles, ignored when rendering to screen: */
    @page { size: A5; margin: 1cm }
    @media print { nav { display: none } }
''')}


@app.route('/static/<path:filename>')
def static(filename):
    if filename in STATIC_FILES:
        content_type, body = STATIC_FILES[filename]
        return body, 200, {'Content-Type': content_type}
    else:
        abort(404)


@app.route(u'/Unïĉodé/<stuff>')
@app.route(u'/foo bar/<stuff>')
def funky_urls(stuff):
    return unicode(stuff)


if __name__ == '__main__':
    run()