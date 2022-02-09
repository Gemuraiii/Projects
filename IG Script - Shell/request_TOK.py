import requests
import json
import pandas as pd
import numpy as np


def getCreds():

    creds = dict()
    creds['access_token'] = ''
    creds['longlived_access_token'] = ''
    creds['client_id'] = ''
    creds['client_secret'] = ''
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['expiration_date'] = ''
    creds['facebook_page_id'] = ''
    creds['instagram_id'] = ''
    creds['username'] = ''
    creds['media_ids'] = ''
    

    return creds

def GenerateApis( url, endpointParams, debug = 'no') :
    data = requests.get(url, endpointParams )

    response = dict()

    response['url'] = url
    response['endpt_params'] = endpointParams
    response['endpt_params_organized'] = json.dumps( endpointParams,indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_organized'] = json.dumps(response['json_data'], indent = 4)
    response['json_organized'] = data.json()

    if ('yes' == debug) :
        displayAPI(response)

    return response

def displayAPI( response) :
    print('\nURL: ')
    print(response['url'])
    print('\nEndpoint Parameters: ')
    print(response['endpt_params_organized'])
    print('\nEnd_Response')
    print(response['json_data_organized'])
