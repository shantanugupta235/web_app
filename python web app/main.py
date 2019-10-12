# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime

from flask import Flask, render_template,request

app = Flask(__name__)

def power(x, y): 
    if y==0: 
        return 1
    if y%2==0: 
        return power(x, y/2)*power(x, y/2) 
    return x*power(x, y/2)*power(x, y/2) 
  

def order(x): 
  

    n = 0
    while (x!=0): 
        n = n+1
        x = x/10
    return n 
  


def isArmstrong (x): 
    n = order(x) 
    temp = x 
    sum1 = 0
    while (temp!=0): 
        r = temp%10
        sum1 = sum1 + power(r, n) 
        temp = temp/10
  

    return (sum1 == x) 

@app.route('/',methods=['POST','GET'])
def root():
    dummy_times = []
    message=''
    if request.method=='POST':
        number = int(request.form["number1"])
        if request.form['submit_button'] == 'Check Armstrong':
            if(isArmstrong(number)):
                message=request.form["number1"]+' is a Armstrong Number.'
            else:
                message=request.form["number1"] + ' is not a Armstrong number'
        else:
            i=1
            dummy_times.append('All armstrong numbers till '+request.form["number1"]+' are :')
            while i<=int(request.form["number1"]):
                if(isArmstrong(i)):
                    dummy_times.append(i)
                i=i+1
    return render_template('index.html',message=message,times=dummy_times)

#@app.route('/input',methods=['POST'])
#def input():
#	if request.method == 'POST':
#		number = int(request.form["number1"])
#		The neon number are 
#	return number

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
