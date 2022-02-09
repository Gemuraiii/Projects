from request_TOK import getCreds, GenerateApis

def getInstagramID( params ):
    """ Get instagram account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account
	Returns:
		object: data from the endpoint
	"""

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + params['facebook_page_id']

    return GenerateApis(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = getInstagramID(params)

