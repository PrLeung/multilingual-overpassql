# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

dashscope.api_key='sk-2b7834debe694f9c89f4cd13e5f83347'

def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a highly skilled translator with expertise in many languages. Your task is to translate the text in English into Chinese while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version. Wrap your answer in []'},
                {'role': 'user', 'content': 'Nature reserves in current view with a note matching the regular expression \"Schild\" from 2016-07-01 12:00:00.'}]
    response = dashscope.Generation.call(
        model='llama2-13b-chat-v2',
        messages=messages,
        result_format='message',  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()
