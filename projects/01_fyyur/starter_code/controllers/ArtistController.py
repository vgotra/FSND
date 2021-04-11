from flask import render_template, request, redirect, url_for, flash, session

from app import app
from data_access import db
from data_access.repositories.ArtistsRepository import ArtistsRepository
from forms.ArtistForm import ArtistForm
from helpers import get_form_validation_errors, build_form_from_session


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
    form = build_form_from_session(ArtistForm, 'artist_edit_form_data', artist)
    return render_template('forms/edit_artist.html', form=form)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    form = ArtistForm()
    if form.validate():
        try:
            ArtistsRepository(db).save_artist(artist_id, form)
            flash('Artist was successfully updated!')
            return redirect(url_for('show_artist', artist_id=artist_id))
        except Exception as ex:
            print(str(ex))
            flash('An error occurred. Artist could not be listed.')
            session['artist_edit_form_data'] = request.form
            return redirect(url_for('edit_artist', artist_id=artist_id))
    error_message = get_form_validation_errors(form)
    flash('An error occurred. Artist {} could not be saved. Errors: {}'.format(form.name.data, error_message))
    session['artist_edit_form_data'] = request.form
    return redirect(url_for('edit_artist', artist_id = artist_id))


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = build_form_from_session(ArtistForm, 'artist_create_form_data')
    return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    form = ArtistForm()
    if form.validate():
        try:
            ArtistsRepository(db).create_artist(form)
            flash('Artist {} was successfully listed!'.format(request.form['name']))
            return redirect(url_for('index'))
        except Exception as ex:
            print(str(ex))
            flash('An error occurred. Artist could not be listed.')
            session['artist_create_form_data'] = request.form
            return redirect(url_for('create_artist_form'))
    error_message = get_form_validation_errors(form)
    flash('An error occurred. Artist {} could not be listed. Errors: {}'.format(form.name.data, error_message))
    session['artist_create_form_data'] = request.form
    return redirect(url_for('create_artist_form'))
