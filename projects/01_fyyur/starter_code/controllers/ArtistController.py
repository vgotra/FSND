from flask import render_template, request, redirect, url_for, flash
from werkzeug.datastructures import MultiDict

from app import app
from data_access import db
from data_access.repositories.ArtistsRepository import ArtistsRepository
from forms.ArtistForm import ArtistForm


@app.route('/artists')
def artists():
    all_artists = ArtistsRepository(db).get_all_artists()
    return render_template('pages/artists.html', artists=all_artists)


@app.route('/artists/search', methods=['POST'])
def search_artists():
    search_term = request.form.get('search_term', '')
    results = ArtistsRepository(db).search_artists(search_term)
    return render_template('pages/search_artists.html', results=results, search_term=search_term)


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    artist = ArtistsRepository(db).get_artist_with_shows_by_id(artist_id)
    return render_template('pages/show_artist.html', artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    artist = ArtistsRepository(db).get_artist_by_id(artist_id)
    form = ArtistForm(MultiDict(artist))
    return render_template('forms/edit_artist.html', form=form)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    form = ArtistForm()
    if form.validate():
        ArtistsRepository(db).save_artist(artist_id, form)
        return redirect(url_for('show_artist', artist_id=artist_id))
    return render_template('forms/edit_artist.html', form=form)


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    form = ArtistForm()
    if form.validate():
        ArtistsRepository(db).create_artist(form)
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
        return redirect(url_for('index'))
    flash('An error occurred. Artist ' + form.name.data + ' could not be listed.')
    return render_template('forms/new_artist.html', form=form)
