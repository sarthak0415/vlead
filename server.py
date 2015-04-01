from flask import Flask, session, request, make_response, url_for, redirect,\
    render_template, jsonify, abort
import requests
import json
from datetime import datetime, timedelta

import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret_key

@app.route("/")
def index():

    print 'In index printing session \n'
    print session
    print '\ndone\n'

    if 'auth_tok' in session:
        auth_tok = session['auth_tok']

        # check if it has expired
        oauth_token_expires_in_endpoint = config.swtstoreURL + '/oauth/token-expires-in'
        resp = requests.get(oauth_token_expires_in_endpoint)
        expires_in = json.loads(resp.text)['expires_in']

        check = datetime.utcnow() - auth_tok['issued']
        if check > timedelta(seconds=expires_in):
            print 'access token expired'
            auth_tok = {'access_token': '', 'refresh_token': ''}
        else:
            print 'access token did not expire'

    else:
        auth_tok = {'access_token': '', 'refresh_token': ''}

    return render_template('index.html',
                           access_token=auth_tok['access_token'],
                           refresh_token=auth_tok['refresh_token'],
                           config=config)

@app.route("/downloadMusic")
def downloadMusic():
    try :
        url = request.args.get("url")
        #url = "http://www-mmsp.ece.mcgill.ca/documents/AudioFormats/WAVE/Samples/AFsp/M1F1-mulaw-AFsp.wav"
        
        print "in downloadMusic with content\t"
        print url
        music_file_parse_url = url.split("/")
        music_file_name = music_file_parse_url[-1]
        music_file_path = 'static/music_files/'+music_file_name
        response = requests.get(url)
        data = response.content
        open(music_file_path, 'wb').write(data)
        #print data
        
    except :
        print 'sorry couldn download the file'
        #return redirect(url_for('index'))
    else:
        return make_response(music_file_path, 200)
        #return render_template('index.html')
    
@app.route("/authenticate")
def authenticateWithOAuth():
    
    auth_tok = None
    code = request.args.get('code')
    
    print code 

    # prepare the payload
    payload = {
        'scopes': 'email sweet',
        'client_secret': 'config.app_secret',
        'code': code,
        'redirect_uri': config.redirect_uri,
        'grant_type': 'authorization_code',
        'client_id': config.app_id
    }

    # token exchange endpoint
    oauth_token_x_endpoint = config.swtstoreURL + '/oauth/token'
    resp = requests.post(oauth_token_x_endpoint, data=payload)
    auth_tok = json.loads(resp.text)
    print 'recvd auth token from swtstore'
    print auth_tok

    if 'error' in auth_tok:
        print auth_tok['error']
        return make_response(auth_tok['error'], 200)

    # set sessions etc
    session['auth_tok'] = auth_tok
    session['auth_tok']['issued'] = datetime.utcnow()
    
    return redirect(url_for('index'))

@app.route("/signOut")
def signOut():
    user = request.args.get("user")

    print "in sign out the user\t"
    print user

    print session
    if 'auth_tok' in session:
        del(session['auth_tok'])
    print '\nsession deleted'
    print session
    print '\nnew session above'
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    
    app.debug = True
    app.run()
