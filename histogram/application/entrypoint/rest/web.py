import json
import logging

from quart import Blueprint, request, Response

from application.core.use_cases import SourceUC, HistogramUC
from application.core.const import histogram as histogram_const
from application.data_provider import ResponseProvider

bp = Blueprint('web', __name__)
response_provider = ResponseProvider()


@bp.route('/unique_words', methods=['GET'])
async def unique_words():
    params = request.args
    element_type = histogram_const.HISTOGRAM_WORDS
    histogram_uc = HistogramUC('web', 'html', element_type, params)
    data_in_db = await histogram_uc.get_in_db()
    if not data_in_db.check():
        await histogram_uc.get_histogram().storage()

    return response_provider.json(histogram_uc.top())


@bp.route('/hello', methods=['GET'])
def hello():
    logging.info("test hello")
    return response_provider.json({})
