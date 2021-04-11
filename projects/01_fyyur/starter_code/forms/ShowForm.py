from datetime import datetime

from flask_wtf import Form
from wtforms import DateTimeField, SelectField
from wtforms.validators import DataRequired


class ShowForm(Form):
    artist_id = SelectField(u'Artist', validators=[DataRequired()])
    venue_id = SelectField(u'Venue', validators=[DataRequired()])
    start_time = DateTimeField(u'Start Time', validators=[DataRequired()], default=datetime.today)
