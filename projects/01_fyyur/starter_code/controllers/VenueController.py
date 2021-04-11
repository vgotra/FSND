from flask import render_template, request, flash, redirect, url_for, make_response, session

from app import app
from data_access import db
from data_access.repositories.VenuesRepository import VenuesRepository
from forms.VenueForm import VenueForm
from helpers import get_form_validation_errors, build_form_from_session


@app.route('/venues')
def venues():
    all_venues = VenuesRepository(db).get_venues_grouped_by_city()
    return render_template('pages/venues.html', areas=all_venues)


@app.route('/venues/search', methods=['POST'])
def search_venues():
    search_term = request.form.get('search_term', '')
    results = VenuesRepository(db).search_venues(search_term)
    return render_template('pages/search_venues.html', results=results, search_term=search_term)


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    venue = VenuesRepository(db).get_venue_with_shows_by_id(venue_id)
    return render_template('pages/show_venue.html', venue=venue)


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = build_form_from_session(VenueForm, 'venue_create_form_data')
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    form = VenueForm()
    if form.validate():
        try:
            VenuesRepository(db).create_venue(form)
            flash('Venue {} was successfully listed!'.format(request.form['name']))
            return redirect(url_for('index'))
        except Exception as ex:
            print(str(ex))
            flash('An error occurred. Venue could not be listed.')
            session['venue_create_form_data'] = request.form
            return redirect(url_for('create_venue_form'))
    error_message = get_form_validation_errors(form)
    flash('An error occurred. Venue {} could not be listed. Errors: {}'.format(form.name.data, error_message))
    session['venue_create_form_data'] = request.form
    return redirect(url_for('create_venue_form'))


@app.route('/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    try:
        VenuesRepository(db).delete_venue(venue_id)
        return make_response('Venue with id: {} was successfully deleted!'.format(venue_id), 200)
    except Exception as ex:
        print(str(ex))
        return make_response('An error occurred. Venue with id: {} could not be deleted.'.format(venue_id), 500)


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = VenuesRepository(db).get_venue_by_id(venue_id)
    form = build_form_from_session(VenueForm, 'venue_edit_form_data', venue)
    return render_template('forms/edit_venue.html', form=form)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    form = VenueForm()
    if form.validate():
        try:
            VenuesRepository(db).save_venue(venue_id, form)
            flash('Venue was successfully updated!')
            return redirect(url_for('show_venue', venue_id=venue_id))
        except Exception as ex:
            print(str(ex))
            flash('An error occurred. Venue could not be listed.')
            session['venue_edit_form_data'] = request.form
            return redirect(url_for('edit_venue', venue_id = venue_id))
    error_message = get_form_validation_errors(form)
    flash('An error occurred. Venue {} could not be saved. Errors: {}'.format(form.name.data, error_message))
    session['venue_edit_form_data'] = request.form
    return redirect(url_for('edit_venue', venue_id = venue_id))
