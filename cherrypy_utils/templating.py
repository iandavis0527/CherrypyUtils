import pathlib
import cherrypy

from jinja2 import Environment, FileSystemLoader, select_autoescape


env = None


def initialize(template_location):
    global env
    cherrypy.log("Loading jinja template engine using filesystem location: {0}".format(template_location))
    env = Environment(
        loader=FileSystemLoader(template_location),
        autoescape=select_autoescape(["html", "xml"]),
    )


def get_env():
    return env