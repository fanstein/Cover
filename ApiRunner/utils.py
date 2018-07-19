# coding:utf8

def diff_response(resp_obj, expected_resp_json):
    diff_content = {}
    resp_info = parse_response_object(resp_obj)
    diff_content=diff_json(resp_info, expected_resp_json)
    # 对比 status_code，将差异存入 diff_content
    # 对比 Headers，将差异存入 diff_content
    # 对比 Body，将差异存入 diff_content
    return diff_content

def parse_response_object(resp_obj):
    try:
        resp_body = resp_obj.json()
    except ValueError:
        resp_body = resp_obj.text
    return {
        'status_code': resp_obj.status_code,
        'headers': resp_obj.headers,
        'body': resp_body
    }

def diff_json(current_json, expected_json):
    json_diff = {}
    for key, expected_value in expected_json.items():
        value = current_json.get(key, None)
        if str(value) != str(expected_value):
            json_diff[key] = {
                'value': value,
                'expected': expected_value
            }
    return json_diff