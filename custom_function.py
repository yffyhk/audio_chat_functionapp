from typing import *

import os
import logging
import asyncio
import json
import fastapi_poe as fp

from datetime import datetime

async def get_ai_response(message:fp.ProtocolMessage, bot_name='bot_audio_chat'):
    logging.info('get_ai_response')
    api_key = os.environ['POE_ACCESSKEY']
    
    response = []
    async for partial in fp.get_bot_response(messages=[message], bot_name=bot_name, api_key=api_key):
        response.append(partial.text)
        
    return response


def send_ai(msg:str):
    logging.info('send_ai')
    
    try:
        msg_fp = fp.ProtocolMessage(role='user', content=json.dumps(msg)) 
        response = asyncio.run(get_ai_response(msg_fp))
        
        response_text = ''.join(response)
        logging.info(response_text)
        
        return response_text
    
    except Exception as e:
        logging.error(e)
        return str(e)
        
    
    