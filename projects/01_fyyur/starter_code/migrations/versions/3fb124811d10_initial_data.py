"""Initial migration.

Revision ID: 9a4745913432
Revises: 
Create Date: 2021-03-28 00:19:50.199994

"""
from alembic import op
from sqlalchemy import table, column
from sqlalchemy import String, Integer, Boolean, DateTime
from default_data import DefaultCities, DefaultGenres, DefaultArtists, DefaultVenues, DefaultShows

revision = '3fb124811d10'
down_revision = '3fb124811d0d'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(table('Cities', column('name', String), column('state', String)),
                   [{'name': r["name"], 'state': r["state"]} for r in DefaultCities])
    op.bulk_insert(table('Genres', column('name', String)),
                   [{'name': r} for r in DefaultGenres])

    conn = op.get_bind()

    cities_results = conn.execute('select id, name from "Cities"').fetchall()
    cities = [{'id': city[0], 'name': city[1]} for city in cities_results]

    artists_table = table('Artists',
                          column('name', String), column('phone', String), column('image_link', String),
                          column('website', String), column('facebook_link', String), column('seeking_venue', Boolean),
                          column('seeking_description', String), column('city_id', Integer))
    default_artists = [{"name": r["name"], "phone": r["phone"], "image_link": r["image_link"], "website": r["website"],
                        "facebook_link": r["facebook_link"], "seeking_venue": r["seeking_venue"],
                        "seeking_description": r["seeking_description"],
                        "city_id": next(x for x in cities if x["name"] == r["city"])["id"]}
                       for r in DefaultArtists]
    op.bulk_insert(artists_table, default_artists)

    venues_table = table('Venues',
                         column('name', String), column('phone', String), column('address', String),
                         column('website', String), column('image_link', String), column('facebook_link', String),
                         column('seeking_talent', Boolean), column('seeking_description', String),
                         column('city_id', Integer))
    default_venues = [{"name": r["name"], "phone": r["phone"], "address": r["address"], "image_link": r["image_link"],
                       "website": r["website"], "facebook_link": r["facebook_link"],
                       "seeking_talent": r["seeking_talent"], "seeking_description": r["seeking_description"],
                       "city_id": next(x for x in cities if x["name"] == r["city"])["id"]}
                      for r in DefaultVenues]
    op.bulk_insert(venues_table, default_venues)

    genres_results = conn.execute('select id, name from "Genres"').fetchall()
    genres = [{'id': r[0], 'name': r[1]} for r in genres_results]

    artists_results = conn.execute('select id, name from "Artists"').fetchall()
    artists = [{'id': r[0], 'name': r[1]} for r in artists_results]

    venues_results = conn.execute('select id, name from "Venues"').fetchall()
    venues = [{'id': r[0], 'name': r[1]} for r in venues_results]

    artists_genres_table = table('ArtistsGenres',
                                 column('artist_id', Integer), column('genre_id', Integer))
    default_artists_genres = []
    for artist in DefaultArtists:
        for genre in artist["genres"]:
            default_artists_genres.append({"artist_id": next(x for x in artists if x["name"] == artist["name"])["id"],
                                           "genre_id": next(x for x in genres if x["name"] == genre)["id"]})
    op.bulk_insert(artists_genres_table, default_artists_genres)

    venues_genres_table = table('VenuesGenres',
                                column('venue_id', Integer), column('genre_id', Integer))
    default_venues_genres = []
    for venue in DefaultVenues:
        for genre in artist["genres"]:
            default_venues_genres.append({"venue_id": next(x for x in venues if x["name"] == venue["name"])["id"],
                                          "genre_id": next(x for x in genres if x["name"] == genre)["id"]})
    op.bulk_insert(venues_genres_table, default_venues_genres)

    shows_table = table('Shows',
                        column('start_time', DateTime), column('venue_id', Integer), column('artist_id', Integer))
    default_shows = [{"start_time": r["start_time"],
                      "venue_id": next(x for x in venues if x["name"] == r["venue_name"])["id"],
                      "artist_id": next(x for x in artists if x["name"] == r["artist_name"])["id"]}
                     for r in DefaultShows]
    op.bulk_insert(shows_table, default_shows)


def downgrade():
    op.execute('delete from "Shows"')
    op.execute('delete from "VenuesGenres"')
    op.execute('delete from "ArtistsGenres"')
    op.execute('delete from "Venues"')
    op.execute('delete from "Artists"')
    op.execute('delete from "Genres"')
    op.execute('delete from "Cities"')
