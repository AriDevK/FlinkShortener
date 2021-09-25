from flask import render_template, flash, redirect, abort

from . import app, db
from .forms import UrlForm
from .models import Links
from .utils import select_phrase, select_anime_girl, short_link


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    shorted_link = None
    anime_pic = select_anime_girl()
    author, phrase = select_phrase()

    if form.validate_on_submit():
        long_url = form.url.data
        short_url = short_link(form.url.data)
        link = Links.query.filter_by(long_url=long_url).first()
        host = app.config['PREFERRED_URL_SCHEME'] + '://' + app.config['SERVER_NAME']

        if long_url.startswith(host):
            flash('This is already a Flinked Link.', 'danger')
            return render_template('index.html', anime_pic=anime_pic, author=author, phrase=phrase, form=form, shortedlink=long_url)

        elif link:
            shorted_link = host + '/' + link.short_url

        else:
            new_link = Links(long_url, short_url)
            db.session.add(new_link)
            db.session.commit()
            shorted_link = host + '/' + short_url

        flash('Succesfully flinked, just copy and enjoy. 😊', 'primary')

    return render_template('index.html', anime_pic=anime_pic, author=author, phrase=phrase, form=form, shortedlink=shorted_link)


@app.route('/<url>')
def open_url(url):
    link = Links.query.filter_by(short_url=url).first()

    if not link:
        abort(404)

    return redirect(link.long_url)
