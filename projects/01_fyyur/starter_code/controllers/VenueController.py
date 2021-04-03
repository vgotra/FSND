from flask import render_template, request, flash, redirect, url_for, make_response
from werkzeug.datastructures import MultiDict

from app import app
from data_access import db
from data_access.repositories.VenuesRepository import VenuesRepository
from forms.VenueForm import VenueForm


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
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    form = VenueForm()
    if form.validate():
        VenuesRepository(db).create_venue(form)
        flash('Venue ' + request.form['name'] + ' was successfully listed!')
        return redirect(url_for('index'))
    flash('An error occurred. Venue ' + form.name.data + ' could not be listed.')
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    print("remove venue")
    try:
        VenuesRepository(db).delete_venue(venue_id)
        return make_response('Venue with id: ' + str(venue_id) + ' was successfully deleted!', 200)
    except Exception as ex:
        print(str(ex))
        return make_response('An error occurred. Venue with id: ' + str(venue_id) + ' could not be deleted.', 500)


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = VenuesRepository(db).get_venue_by_id(venue_id)
    form = VenueForm(MultiDict(venue))
    return render_template('forms/edit_venue.html', form=form)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    form = VenueForm()
    if form.validate():
        VenuesRepository(db).save_venue(venue_id, form)
        return redirect(url_for('show_venue', venue_id=venue_id))
    return render_template('forms/edit_venue.html', form=form)
