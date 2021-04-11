from flask import session
from werkzeug.datastructures import MultiDict


def get_form_validation_errors(form):
    message = []
    for field, err in form.errors.items():
        message.append(field + ' ' + '|'.join(err))
    return str(message)


def build_form_from_session(form_class, session_data_name, initial_data=None):
    result = form_class()
    form_data = session.get(session_data_name, None)
    if form_data:
        result = form_class(MultiDict(form_data))
    else:
        if initial_data:
            result = form_class(MultiDict(initial_data))
    return result
