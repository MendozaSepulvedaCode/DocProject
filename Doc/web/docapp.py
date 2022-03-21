from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.doc import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index-page.html')


@app.route('/doc-page', methods=['GET'])
def page():
    return render_template('doc-page.html')


@app.route('/doc_detail', methods=['POST'])
def document_detail():
    id_doc = request.form['id_doc']
    number_pages = request.form['number_pages']
    title = request.form['title']
    category = request.form['category']
    author = request.form['author']

    d = Document(id_doc=id_doc, number_pages=number_pages, title=title, category=category, author=author)
    model.append(d)
    return render_template('doc_detail.html', value=d)


@app.route('/document-page')
def document():
    data = [(i.id_doc, i.number_pages, i.title, i.category, i.author) for i in model]
    print(data)
    return render_template('document-page.html', value=data)


if __name__ == '__main__':
    app.run()