from flask import render_template, flash, session, request, redirect, url_for

from app import app
from data_access import db
from data_access.repositories.ShowsRepository import ShowsRepository
from data_access.repositories.ArtistsRepository import ArtistsRepository
from data_access.repositories.VenuesRepository import VenuesRepository
from forms.ShowForm import ShowForm
from helpers import get_form_validation_errors, build_form_from_session


@app.route('/shows')
def shows():
    all_shows = ShowsRepository(db).get_all_shows()
    return render_template('pages/shows.html', shows=all_shows)


@app.route('/shows/create')
def create_shows():
    # renders form. do not touch.
    all_artists = ArtistsRepository(db).get_all_artists()
    all_venues = VenuesRepository(db).get_all_venues()
    form = build_form_from_session(ShowForm, 'show_create_form_data')
    form.artist_id.choices = [(artist["id"], artist["name"]) for artist in all_artists]
    form.venue_id.choices = [(venue["id"], venue["name"]) for venue in all_venues]
    return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    all_artists = ArtistsRepository(db).get_all_artists()
    all_venues = VenuesRepository(db).get_all_venues()
    form = ShowForm()
    form.artist_id.choices = [(artist["id"], artist["name"]) for artist in all_artists]
    form.venue_id.choices = [(venue["id"], venue["name"]) for venue in all_venues]
    if form.validate():
        try:
            ShowsRepository(db).create_show(form)
            flash('Show was successfully listed!')
            return redirect(url_for('index'))
        except Exception as ex:
            print(str(ex))
            flash('An error occurred. Show could not be listed.')
            session['show_create_form_data'] = request.form
            return redirect(url_for('create_shows'))
    error_message = get_form_validation_errors(form)
    flash('An error occurred. Show could not be listed. Errors: {}'.format(error_message))
    session['show_create_form_data'] = request.form
    return redirect(url_for('create_shows'))
