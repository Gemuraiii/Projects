from request_TOK import getCreds, GenerateApis

def GenerateLongLivedAccessToken( params ): 
    """ Get long lived access token
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
	Returns:
		object: data from the endpoint
	"""
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['fb_exchange_token'] = params['longlived_access_token']

    url = params['endpoint_base'] +'oauth/access_token'

    return GenerateApis( url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = GenerateLongLivedAccessToken(params)

print('\n WARNING!: ACCESS TOKEN INFO \n')
print('Access Token: ')
print(response['json_data']['longlived_access_token'])