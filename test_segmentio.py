from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest


@pytest.fixture(scope="session")
def app(request):
    from flask import Flask

    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SEGMENTIO_SEND"] = False
    app.config["SEGMENTIO_WRITE_KEY"] = "testing"
    return app


@pytest.fixture(scope="session")
def analytics(app):
    from flask_segmentio import SegmentIO

    analytics = SegmentIO(app)
    return analytics


@pytest.fixture()
def unitialized():
    from flask_segmentio import SegmentIO

    analytics = SegmentIO()
    return analytics


def test_client_initialized(analytics):
    from analytics import Client
    assert analytics.client.__class__ == Client


def test_client_unitialized(unitialized):
    with pytest.raises(AssertionError) as exc:
        unitialized.track("johndoe", "commented")
    assert "init_app()" in str(exc.value)


def test_init_app(app, analytics):
    assert app.extensions["segmentio"] == analytics
    assert analytics.app == app


def test_track(analytics):
    result = analytics.track("johndoe", "Commented")
    assert result[0] is False


def test_identify(analytics):
    result = analytics.identify("johndoe")
    assert result[0] is False


def test_alias(analytics):
    result = analytics.alias("123", "johndoe")
    assert result[0] is False


def test_group(analytics):
    result = analytics.group("johndoe", "admin-group")
    assert result[0] is False


def test_page(analytics):
    result = analytics.page("johndoe", "docs", "python")
    assert result[0] is False


def test_screen(analytics):
    result = analytics.screen("johndoe", "settings", "enabled")
    assert result[0] is False
