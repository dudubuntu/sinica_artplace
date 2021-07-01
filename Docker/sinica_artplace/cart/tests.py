import pytest
import requests
import json


class TestCartApi:
    def test_get_return_formatted_json(self):
        response = requests.get('http://localhost:8000/api/v1/cart/get_cart/').json()
        assert 'length' in response
        assert 'total_price' in response
        assert 'articul_list' in response
        assert isinstance(response['articul_list'], list)

    @pytest.mark.parametrize( "expected_status, data, headers", [
        pytest.param(
            415, {}, {'Content-Type': 'text/plain'}, id='no_fields'
        ),

        pytest.param(
            400, {}, {'Content-Type': 'application/json'}, id='no_fields'
        ),
        pytest.param(
            400, {'articul': '1000'}, {'Content-Type': 'application/json'}, id='no_extra'
        ),
        pytest.param(
            400, {'extra': {'quantity': 1, 'price': 8000}}, {'Content-Type': 'application/json'}, id='no_articul'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'price': 8000}}, {'Content-Type': 'application/json'}, id='no_extra_quantity'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'quantity': 1}}, {'Content-Type': 'application/json'}, id='no_extra_price'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'price': 'sdfds', 'quantity': 1}}, {'Content-Type': 'application/json'}, id='extra_pice_str'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'price': 8000, 'quantity': 'sdfdsf'}}, {'Content-Type': 'application/json'}, id='extra_quantity_str'
        ),

        pytest.param(
            200, {'articul': '1000', 'extra': {'price': 8000, 'quantity': 5}}, {'Content-Type': 'application/json'}, id='basic'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'price': 8000, 'quantity': -1}}, {'Content-Type': 'application/json'}, id='quantity_negative'
        ),
        pytest.param(
            400, {'articul': '1000', 'extra': {'price': -1, 'quantity': 1}}, {'Content-Type': 'application/json'}, id='price_negative'
        ),
    ])
    def test_add_item(self, expected_status, data, headers):
        response = requests.post('http://localhost:8000/api/v1/cart/add_item/', data=json.dumps(data), headers=headers)
        assert response.status_code == expected_status