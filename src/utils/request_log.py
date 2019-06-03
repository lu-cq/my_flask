# coding: utf-8

from uuid import uuid4

from libs.logger.rsyslog import rsyslog


__all__ = ['log_request']

hidden_fields = ['password']


def log_request(request, response, module_name):
    """Record request log"""
    try:
        req_id = uuid4().hex
        req_remote_addr = request.remote_addr
        req_host = request.host
        req_url = request.path
        req_args = request.args.to_dict().__str__()
        body_args = request.form.to_dict()
        body_json = request.get_json()
        if body_json:
            body_args = dict(body_args, **request.get_json())
        for k in body_args:
            if k in hidden_fields:
                body_args[k] = '***'

        req_body = body_args.__str__()
        req_head = request.headers.items().__str__()
        request_log_format = ('req_id={0}, req_remote_addr={1},, host={2}, url={3}, head={4},'
                              'args={5}, req_body={6}, resp_status={7}, resp_body={8}')
        response_body = response.data if response.status_code not in [200, 201] else ''
        response_body = str(response_body).replace('\n', '').replace(' ', '')
        log_content = request_log_format.format(
            req_id, req_remote_addr, req_host, req_url, req_head, req_args, req_body,
            response.status_code, response_body)
        rsyslog.send(log_content, tag=module_name)
    except Exception as e:
        rsyslog.send(str(e), tag='log_request')
        pass
