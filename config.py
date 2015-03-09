# secret key for the application used in session
secret_key = "4yug68r8vu6ibtvu76yj"

# the URL pointing to the sweet store this application will sweet to
swtstoreURL = 'http://localhost:5001'

# the URL at which your application is hosted
# when you are deploying the app locally, by default this should be
#app_url= 'http://localhost:5000'
app_url = 'http://localhost:5000'

# the app_id or client_id you have recieved when you registered this
# application to swtstore
app_id = 'QKsks3q7m88oLhRiAEjJIAulczl2RCtG8WfKAykX'

# the app_secret or client_secret you have recieved when you registered this
# application to swtstore
app_secret = '4WspdVjvV08rrFFy9fxgUqCmZfBxa9oi87yO4ZwT4dagKsH7Lm'

# the absolute url of the OAuth2.0 redirect endpoint
# this is the endpoint where the second part of the oauth handshake happen and
# the endpoint passes the client secret and the recvd code for the final call
# to recieve the OAuth token. For this app, the endpoint is /authenticate
redirect_uri = 'http://localhost:5000/authenticate'