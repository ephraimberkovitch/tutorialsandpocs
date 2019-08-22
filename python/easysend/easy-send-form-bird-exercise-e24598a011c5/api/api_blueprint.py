from flask import Blueprint

api_blueprint = Blueprint(
    'api',
    __name__,
)

# noinspection PyUnresolvedReferences
import health_api
# noinspection PyUnresolvedReferences
import game_state_api
