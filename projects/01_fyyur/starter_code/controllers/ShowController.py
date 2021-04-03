from flask import render_template, flash

from app import app
from data_access import db
from data_access.repositories.ShowsRepository import ShowsRepository
from forms.ShowForm import ShowForm


@app.route('/shows')
def shows():
    all_shows = ShowsRepository(db).get_all_shows()
    return render_template('pages/shows.html', shows=all_shows)


@app.route('/shows/create')
def create_shows():
    # renders form. do not touch.
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    form = ShowForm()
    if form.validate():
        ShowsRepository(db).create_show(form)
        flash('Show was successfully listed!')
        return render_template('pages/home.html')
    flash('An error occurred. Show could not be listed.')
    return render_template('forms/new_show.html', form=form)
