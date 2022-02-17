import requests
import re

def generate_gmail(ID: int):
  
  # access the API
  url = "https://temp-gmail.p.rapidapi.com/get"
  querystring = {"id":ID,"type":"alias"}
  headers = {
    'x-rapidapi-host': "temp-gmail.p.rapidapi.com",
    'x-rapidapi-key': "YOUR PRIVATE KEY"
    }
  
  # send a request to the API
  response = requests.request("GET", url, headers=headers, params=querystring)
  
  # convert the response to JSON format 
  json_response = response.json()
  # get gmail address
  gmail = json_response['items']['username']
  # get gmail password
  password = json_response['items']['key']

  print('Gmail address: %s' % str(gmail))
  print('Password: %s' % str(password))


    # Input Example:
    # generate_gmail(ID=3)

    # Output Example:
    # Gmail address: lauraburm.rs.131.9.8.8@gmail.com 
    # Password: ***********R094ngJVIKMdXhfVCiMEEElE82Es

def check_inbox(gmail: str, password: str):

  # access the API
  url = "https://temp-gmail.p.rapidapi.com/check"
  querystring = {"username":gmail,"key":password}
  headers = {
      'x-rapidapi-host': "temp-gmail.p.rapidapi.com",
      'x-rapidapi-key': "YOUR PRIVATE KEY"
      }
  
  # send a request to the API
  response = requests.request("GET", url, headers=headers, params=querystring)
  
  # convert the response to JSON format 
  json_response = response.json()
  
  # print the message from the API
  print('API message: %s' % str(json_response['msg']))

  # check whether the inbox is empty or not
  if json_response['items'] == []:
    print("inbox is empty")

  # if the inbox is not empty, print the details of the newest mail
  else:
    message_id = json_response['items'][0]['mid']
    print('Message ID: %s' % str(message_id))
    print('From: %s' % str(json_response['items'][0]['textFrom']))
    print('Date: %s' % str(json_response['items'][0]['textDate']))
    print('Subject: %s' % str(json_response['items'][0]['textSubject']))

    # Input Example
    # MyGmail = "lauraburmr.s13198.8@gmail.com"
    # MyPassword = "***********QEQfM4cFqy2aie6sA6kPpxEMKGFNSQl4"

    # check_inbox(gmail=MyGmail, password=MyPassword)
    
    # Output Example
    # Message ID: 17e5dd60676eed04 
    # From: aergashev
    # Date: 2022–01–15 20:03:22 
    # Subject: TEST EMAIL




def read_message(gmail: str, message_id: str):
    # access the API
    url = "https://temp-gmail.p.rapidapi.com/read"
    querystring = {"username":gmail,"message_id":message_id}
    headers = {
      'x-rapidapi-host': "temp-gmail.p.rapidapi.com",
      'x-rapidapi-key': " YOUR PRIVATE KEY"
      }
  
    # send a request to the API
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    # convert the response to JSON format 
    json_response = response.json()
    
    # remove the html tags from the body of the mail
    body_message = re.sub(r'<.*?>', '', json_response['items']['body'])
    print('Body message: %s' % str(body_message))

    # Input Example:
    # MyGmail = 'lauraburmr.s13198.8@gmail.com'
    # MessageID = '17e5dd60676eed04'

    # read_message(gmail=MyGmail, message_id=MessageID)

    # Output Example:
    # Body message: This is a test mail sent by aergashev



def restore_gmail(gmail: str):
  
  # access the API
  url = "https://temp-gmail.p.rapidapi.com/restore"
  querystring = {"username":gmail}
  headers = {
      'x-rapidapi-host': "temp-gmail.p.rapidapi.com",
      'x-rapidapi-key': " YOUR PRIVATE KEY"
      }
  
  # send a request to the API
  response = requests.request("GET", url, headers=headers, params=querystring)
  
  # convert the response to JSON format 
  json_response = response.json()

  print('Gmail address: %s' % str(json_response['items']['username']))
  print('Password: %s' % str(json_response['items']['key']))
