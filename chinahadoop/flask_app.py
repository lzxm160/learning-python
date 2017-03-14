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
    return render_template(
        'document.html')
   

### The code specific to Flask-WeasyPrint follows. Pretty simple, eh?

from flask_weasyprint import render_pdf, HTML


@app.route('/pdf')
def document_pdf():
    # HTML('http://weasyprint.org/').write_pdf('website.pdf')
    HTML(filename='/root/Newshop_International/WEB-INF/quotation_pdf.html').write_pdf('/root/go_fcgi/flask_test.pdf')
    # start=time()
    # for num in range(0,50):
    #     req = urllib2.Request("http://172.18.100.85:8088/scm_flow_no/JP/PO/day")
    #     result = urllib2.urlopen(req)
    #     print '\n'.join(result.readlines())
    # finish=time()
    
    # return (finish-start)*1000/50,"ms"
    return 'ok'
# HTML('../foo.html')  # Same as …
# HTML(filename='../foo.html')

# HTML('http://weasyprint.org')  # Same as …
# HTML(url='http://weasyprint.org')

# HTML(sys.stdin)  # Same as …
# HTML(file_obj=sys.stdin)
### End of code specific to Flask-WeasyPrint.


### The templates and static files are inlined here and served from memory.
### This is a bit unusual but allows us to keep this app in a single file.
### We could just as well use normal templates and static files.

from jinja2 import DictLoader

app.jinja_env.loader = DictLoader({
    'document.html': '''
        <!doctype html>
        <title>Test document</title>
        
        <body>
        <section>
            <nav>Get this document <a href="/pdf">as PDF</a></nav>
            
        </section>
    ''',
})




if __name__ == '__main__':
    run()