import azure.functions as func
import logging

from custom_function import *

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route='chat')
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    logging.info(req_body)
    
    message = req_body['message']
    logging.info(message)
    
    answer = send_ai(message)

    return func.HttpResponse(
        answer,
        status_code=200
    )