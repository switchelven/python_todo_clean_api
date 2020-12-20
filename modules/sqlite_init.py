from functools import partial

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.exc import InvalidRequestError

db = SQLAlchemy()


def _slack_failed(e, model, e_type):
    """
    :param e:
    :type e:
    :param model:
    :type model:
    :param e_type:
    :type e_type:
    :return:
    :rtype:
    """
    from modules.logger import Logger

    logger = Logger(__name__)
    db.session.rollback()
    logger.error(e)


def delete_func(model, commit=True):
    try:
        db.session.delete(model)
        db.session.flush()
        if commit:
            db.session.commit()
        return True
    except Exception as e:
        _slack_failed(e, model, 'Delete')
        return False


def set_data_func(model, data, fields):
    for field in fields:
        if field in data.keys() and hasattr(model, field):
            setattr(model, field, data[field])


def serialize_func(_):
    return {}


def refresh_func(model):
    db.session.refresh(model)


def link_func(model):
    """
    Link an object to a session. On invalid request (item is already in session) return false
    :param model:
    :type model:
    :return:
    :rtype:
    """
    try:
        insp = inspect(model)
        if insp.detached:
            db.session.add(model)
    except InvalidRequestError as e:
        if 'another instance with key' in str(e):
            return
        raise e


def get_paginated_query_func(
        model, page, per_page,
        filter_by=None, filters=None, orders=None,
        base_query=None
):
    base = base_query if base_query else model.query
    filters = filters if filters else []
    filter_by = filter_by if filter_by else {}
    orders = orders if orders else []
    if not isinstance(orders, list):
        orders = [orders]
    base = base.filter(*filters).filter_by(**filter_by).order_by(*orders)
    return base.limit(per_page).offset(page * per_page).all(), base.count()


def save_func(model, commit=True):
    # from your_talent.errors import InvalidFieldError, MissingFieldError, IDNotFoundError
    try:
        db.session.add(model)
        db.session.flush()
        if commit:
            db.session.commit()
        return True
    except Exception as e:
        _slack_failed(e, model, 'Insert')
        return False


def commit_func():
    db.session.commit()


db.Model.save = save_func
db.Model.set_data = set_data_func
db.Model.serialize = serialize_func
db.Model.delete = delete_func
db.Model.link_to_session = link_func
db.Model.paginated_query = get_paginated_query_func
db.Model.refresh = refresh_func
db.Model.commit = commit_func


def get_from(obj, field, default=None):
    if not obj:
        return default
    return getattr(obj, field, default)


relationship = partial(db.relationship, lazy='select', join_depth=1)
