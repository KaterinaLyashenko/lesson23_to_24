from typing import Union, Tuple, Dict, List

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema, BatchRequest

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    # Принять запрос от пользователя
    data: Dict[str, Union[List[dict], str]] = request.json
    # Обработать запрос,валидировать значения
    try:
        validated_data = BatchRequest().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    # Выпoлнить запрос
    result = None
    for query in validated_data['queries']:
        result = build_query(
           cmd=query['cmd'],
           value=query['value'],
           file_name=validated_data['file_name'],
           data=result,
    )

    return jsonify(result)