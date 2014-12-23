from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from analytics import Client


class SegmentIO(object):
    def __init__(self, app=None):
        self.app = app
        self._client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("SEGMENTIO_WRITE_KEY", "")
        app.config.setdefault("SEGMENTIO_DEBUG", False)
        app.config.setdefault("SEGMENTIO_SEND", True)
        app.config.setdefault("SEGMENTIO_MAX_QUEUE_SIZE", 100000)

        app.extensions = getattr(app, "extensions", {})
        app.extensions["segmentio"] = self
        self.app = app

    @property
    def client(self):
        assert self.app is not None, \
            "The segmentio extension was not registered " \
            "to the current application. Please make sure " \
            "to call init_app() first"

        if self._client is None:
            self._client = Client(
                self.app.config["SEGMENTIO_WRITE_KEY"],
                debug=self.app.config["SEGMENTIO_DEBUG"],
                send=self.app.config["SEGMENTIO_SEND"],
                on_error=self._on_error,
                max_queue_size=self.app.config["SEGMENTIO_MAX_QUEUE_SIZE"],
                )
        return self._client

    def track(self, *args, **kwargs):
        return self.client.track(*args, **kwargs)

    def identify(self, *args, **kwargs):
        return self.client.identify(*args, **kwargs)

    def alias(self, *args, **kwargs):
        return self.client.alias(*args, **kwargs)

    def group(self, *args, **kwargs):
        return self.client.group(*args, **kwargs)

    def page(self, *args, **kwargs):
        return self.client.page(*args, **kwargs)

    def screen(self, *args, **kwargs):
        return self.client.screen(*args, **kwargs)

    def flush(self):
        self.client.flush()

    def _on_error(self, exc, batch):
        pass
