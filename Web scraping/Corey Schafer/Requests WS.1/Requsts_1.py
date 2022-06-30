import requests
# 1. https: // www.youtube.com/watch?v = tb8gHvYlCFs

r = requests.get('https://xkcd.com/353/')
print(dir(r))
# dir let's you see all of the attributes and methods available to you

#####
# help function shows a more detailed explanation for the object

r = requests.get('https://xkcd.com/353/')
print(help(r))

#####

# shows the html of the website we input in the r object

r = requests.get('https://xkcd.com/353/')
print(r.text)

#####

# download an image using the image url and the content function
# you can see the text it is made of

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)

#####

# ('name', 'mode')
# wb mode = write bytes
# .write function writes it into a new file and .content function takes the image url and turns it into the image

r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic1.png', 'wb') as f:
    f.write(r.content)

#####

# check the status code to make sure you get a good response
# 200's are success
# 300's are redirects
# 400's are client errors - example: if you don't have access to the webpage
# 500's are server errors - example: when a site is crashed and cannot access it

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.status_code)

# gives back True for anything under 400

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.ok)

#####

# gives back all of the headers

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.headers)

#####

# httpbin.org is used to test your http requests
# payload is a dictionary of terms as to not make typo mistakes
# params is just the parameters/arguments for the url

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
# in this it printed out the correct url at the bottom using the params

#####

# prints out the correct url based on the params
# known as get parameters

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

#####

# pass in form data and get a JSON response back
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

#####

# create a python dictionary from the JSON response
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.json())

#####

# set the object to the json response
# get out the form submissions in a string format
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()

print(r_dict['form'])

#####

# see that you get authenticated is the parameters are correct
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

print(r.text)

#####

# if you put in the wrong password then you can see that it will return a 401 error code showing that you were not authenticated
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'abc'))

print(r)

#####

# add in the timeout so that it doesn't just sit there endlessly loading
r = requests.get('https://httpbin.org/basic-auth/corey/testing',
                 timeout=3, auth=('corey', 'testing'))

print(r)

#####

# ReadTimeout exception after 3 seconds
r = requests.get('https://httpbin.org/delay/6', timeout=3)

print(r)
