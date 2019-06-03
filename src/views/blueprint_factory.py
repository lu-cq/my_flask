# coding: utf-8

from __future__ import absolute_import

from flask import Blueprint, jsonify, request, g
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError

from src.errors import GBaseError
from src.utils.request_log import log_request


class BlueprintFactory(object):
    def __init__(self, blueprint_class, url_package='api'):
        self.blueprint_class = blueprint_class
        self.url_package = url_package

    def __call__(self, name, version, package_name, **kwargs):
        """Creates blueprint to sort the API views.

        :param name: The endpoint name.
        :param version: The API version.
        :param package_name: Always be ``__name__``.
        :param url_prefix: The prefix of relative URL.
        """
        blueprint = self.make_blueprint(name, version, package_name, **kwargs)
        blueprint = self.init_blueprint(blueprint)
        return blueprint

    def make_blueprint(self, name, version, package_name, **kwargs):
        url_prefix = kwargs.pop('url_prefix', '')
        url_prefix = '/{url_package}{url_api_version}{url_prefix}'.format(
            url_package=self.url_package, url_api_version='/' + version if version else '',
            url_prefix=url_prefix)
        blueprint_name = '{url_package}-{version}.{name}'.format(
            url_package=self.url_package, name=name, version=version)
        return Blueprint(
            blueprint_name, package_name, url_prefix=url_prefix, **kwargs)

    def init_blueprint(self, blueprint):

        blueprint.errorhandler(GBaseError)(self.handle_base_error)
        blueprint.errorhandler(ValidationError)(self.handle_validation_error)
        # blueprint.errorhandler(Exception)(self.handle_exception)
        blueprint.errorhandler(400)(self.handle_http_exception)
        blueprint.errorhandler(401)(self.handle_http_exception)
        blueprint.errorhandler(403)(self.handle_http_exception)
        blueprint.errorhandler(404)(self.handle_http_exception)
        blueprint.errorhandler(405)(self.handle_http_exception)
        blueprint.errorhandler(410)(self.handle_http_exception)
        blueprint.errorhandler(503)(self.handle_http_exception)
        blueprint.after_request(self.after_request)

        return blueprint

    def handle_base_error(self, e):
        return jsonify(status='error', message=e.message, code=e.errno), 200

    def handle_validation_error(self, e):
        return jsonify(status='error', message=e.message, code=400), 400

    def handle_http_exception(self, error):
        messages = (error.description).decode('utf-8')
        return jsonify(status='error', message=messages), error.code

    def after_request(self, response):
        log_request(request, response, self.url_package)

        return response
