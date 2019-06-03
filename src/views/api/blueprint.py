# coding: utf-8

from __future__ import absolute_import, unicode_literals

from flask import Blueprint

from src.views.blueprint_factory import BlueprintFactory

__all__ = ['create_blueprint']

create_blueprint = BlueprintFactory(
    blueprint_class=Blueprint, url_package='api')
