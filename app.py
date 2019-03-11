from flask import Flask, render_template, request, redirect, url_for
from models import update, select, get_count
from create_db import app, db
from forms import HelloFrom


@app.route('/', methods=['GET', "POST"])
def index():
    form = HelloFrom()
    if request.method == "GET":
        count = get_count()
        messages = select()
        return render_template('sayhello.html', messages=messages, count=count, form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            name = request.form.get('name')
            body = request.form.get('message')
            msg = update(name=name, body=body)
            messages = select()
            count = get_count()
            return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run()
