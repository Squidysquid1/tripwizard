from flask import Blueprint
from application.controllers.ItineraryController import ItineraryController

ItineraryRouter = Blueprint('itinerary_controller', __name__)

ItineraryRouter.route('/', methods=['GET'])(ItineraryController.index)