import requests
from prettyprinter import pprint as pp
from prettytable import PrettyTable
import rich
import pandas as pd
import json
import sqlite3

x = PrettyTable()


url = "https://api.company-information.service.gov.uk/"
payload = {}
headers = {
  'Authorization': 'Basic am5ITVBOLXE0aW5NQXk2UC1kbk1hOTRFV2Yyd3NHeThoZk1MWjMxbDo='
}


def lead_officer_search(name):
  callurl = url + "search/officers?q=" + name
  response = requests.request("GET", callurl, headers=headers, data=payload).json()
  pp(response)





def company_call(company_no):
  callurl = url + "company/" + company_no
  response = requests.request("GET", callurl, headers=headers, data=payload).json()
  # df = pd.json_normalize(response)
  # print(df)

  for i in response:
    companyName = response['company_name']
    print(companyName)

  pp(response)

company_call('11139204')


def officers_call(company_no):
  callurl = url + "company/" + company_no + "/officers/"
  response = requests.request("GET", callurl, headers=headers, data=payload).json()

  pp(response)


def posc(company_no):
  callurl = url + "company/" + company_no + "/persons-with-significant-control/"
  response = requests.request("GET", callurl, headers=headers, data=payload).json()
  pp(response)


# posc('11139204')


# lead_officer_search('benjamin white')


#
#
#
#
# conn = sqlite3.connect('lunch.db')
# c = conn.cursor()
#
# #delete table
# #c.execute('''DROP TABLE meals''')
#
# #create a table
# def creatTable():
#   c.execute('''CREATE TABLE IF NOT EXISTS [posc] (
# [active_count] VARCHAR NULL,
# [ceased_count] VARCHAR NULL,
# [items] JSON NULL,
# [items_per_page] VARCHAR NULL,
# [links.persons_with_significant_control_list] VARCHAR NULL,
# [links.self] VARCHAR NULL,
# [start_index] VARCHAR NULL,
# [total_results] VARCHAR NULL
# );''')
#
# #data to insert
# sandwich = 'chicken'
# fruit = 'orange'
# tablenum = 22
#
# #insert and commit to database
# c.execute('''INSERT INTO posc VALUES'''
# ('integer','integer',[{\"address\":{\"address_line_1\":\"string\"\,\"address_line_2\":\"string\"\,\"care_of\":\"string\"\,\"country\":\"string\"\,\"locality\":\"string\"\,\"po_box\":\"string\"\,\"postal_code\":\"string\"\,\"premises\":\"string\"\,\"region\":\"string\"}\,\"ceased\":\"boolean\"\,\"ceased_on\":\"date\"\,\"country_of_residence\":\"string\"\,\"date_of_birth\":{\"day\":\"integer\"\,\"month\":\"integer\"\,\"year\":\"integer\"}\,\"description\":\"string\"\,\"etag\":\"string\"\,\"identification\":{\"country_registered\":\"string\"\,\"legal_authority\":\"string\"\,\"legal_form\":\"string\"\,\"place_registered\":\"string\"\,\"registration_number\":\"string\"}\,\"kind\":\"string\"\,\"links\":{\"self\":\"string\"\,\"statement\":\"string\"}\,\"name\":\"string\"\,\"name_elements\":{\"forename\":\"string\"\,\"other_forenames\":\"string\"\,\"surname\":\"string\"\,\"title\":\"string\"}\,\"nationality\":\"string\"\,\"natures_of_control\":[\"string\"]\,\"notified_on\":\"date\"}],'integer','string','string','integer','integer');
# conn.commit()
#
# #select all data from table and print
# c.execute('''SELECT * FROM meals''')
# results = c.fetchall()
# print(results)
#
# #close database connection
# conn.close()
#
#
#
#
