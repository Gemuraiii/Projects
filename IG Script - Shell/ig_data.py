from pandas.io.pytables import duplicate_doc
from request_TOK import getCreds, GenerateApis
import requests
import json
import pandas as pd
import numpy as np
import csv
from datetime import datetime

def extractMediaIds(params) :
	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}
	Returns:
		object: data from the endpoint
	"""
	endpointParams = dict()
	endpointParams['fields'] = 'id, media_type, timestamp, permalink,username'
	endpointParams['access_token'] = params['longlived_access_token']
	url = params['endpoint_base'] + params['instagram_id'] + '/media'

	return GenerateApis( url, endpointParams, params['debug'])

def getMediaInsights( params ) :
	""" Get insights for a specific media id
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}
	Returns:
		object: data from the endpoint
	"""
	endpointParams= dict()
	endpointParams['metric'] = params['metric']
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['media_ids'] + '/insights'

	return GenerateApis(url, endpointParams, params['debug'] )

def getMonthlyInsights( params):
    	""" Get insights for a users account

	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}&since={since}
	Returns:
		object: data from the endpoint
	"""
	endpointParams = dict()
	endpointParams['metric'] = 'impressions,profile_views,reach'
	endpointParams['period'] = 'month'
	endpointParams['since'] = '1633126501'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['instagram_id'] + '/insights'

	return GenerateApis(url, endpointParams, params['debug'])

def getAccountInsights( params ):
	""" Get insights for a users account

	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}&since={since}
	Returns:
		object: data from the endpoint
	"""
	endpointParams = dict()
	endpointParams['metric'] = 'impressions,profile_views,reach'
	endpointParams['period'] = 'day'
	endpointParams['since'] = '1633126501'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['instagram_id'] + '/insights'

	return GenerateApis(url, endpointParams, params['debug'])



params = getCreds()
params['debug'] = 'no'
response = extractMediaIds(params)
ids = response['json_organized']['data']
ig_username = response['json_data']['data'][0]['username']

media_ids = []

#for post in ids:
	#posts = post['id']
	#media_ids.append(posts)

#params['media_ids'] = media_ids
params['ig_username'] = ig_username

if 'VIDEO' == response['json_data']['data'][0]['media_type'] : # media is a video
	params['metric'] = 'engagement,impressions,reach,saved,video_views'
else : # media is an image
	params['metric'] = 'engagement,impressions,reach,saved'


response1 = getMediaInsights(params)
params['debug'] = 'yes'



response2 = getAccountInsights(params)
 
account_insights = []
titles = []
dates = []
for insight in response2['json_data']['data'] : # loop over user account insights # display info
	titles.append(insight['title'])
	for value in insight['values'] : # loop over each value
		dates.append(value['end_time'])
		account_insights.append(value['value'])

impressions = account_insights[:20]
profile_views = account_insights[20:40]
reach = account_insights[40:]
real_dates = []
for date in dates:
	d = datetime.strptime(date[:-14],'%Y-%m-%d').strftime('%m/%d/%Y')
	real_dates.append(d)

review_dates = list(dict.fromkeys(real_dates))
account_dict= {
	'Dates': review_dates,
	'Impressions': impressions,
	'Profile Views': profile_views,
	'Reach': reach
}
account_df = pd.DataFrame(account_dict)
print(account_df)

account_df.to_csv('account_insights.csv', index=False)
