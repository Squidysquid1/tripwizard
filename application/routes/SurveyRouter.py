from flask import Blueprint
from application.controllers.HowController import HowController

HowRouter = Blueprint('how_controller', __name__)

HowRouter.route('/', methods=['GET'])(HowController.index)