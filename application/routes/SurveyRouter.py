from flask import Blueprint
from application.controllers.SurveyController import SurveyController

SurveyRouter = Blueprint('survey_controller', __name__)

SurveyRouter.route('/', methods=['GET'])(SurveyController.index)