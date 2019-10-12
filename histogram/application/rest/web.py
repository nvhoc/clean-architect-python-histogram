import json
from flask import Blueprint, request, Response

from application.core.use_cases import SourceUC, HistogramUC
from application.core.const import histogram as histogram_const
from application.data_provider import ResponseProvider

bp = Blueprint('web', __name__)

@bp.route('/unique_words', methods=['GET'])
def unique_words():
    params = request.args
    element_type = histogram_const.HISTOGRAM_WORDS
    histogram_uc = HistogramUC('web', 'html', element_type, params)
    if not histogram_uc.get_in_db().check():
        histogram_uc.get_histogram().storage()
        
    return ResponseProvider(histogram_uc.top())
