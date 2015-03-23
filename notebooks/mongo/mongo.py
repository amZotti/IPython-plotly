
# coding: utf-8

# <h1>Using Plotly, Node.js, and MongoDB together to Create TimeSeries Graphs</h1>
# I recently learned about Plotly and used it to make a <a href='https://github.com/amZotti/TweetTracker.js'>awesome data visualizations of Twitter data</a>.
# Plotly is a free web-based platform for making graphs. You can keep graphs private, make them public, and run <a href= 'https://plot.ly/product/enterprise/'>Plotly on your own servers.</a>
# Plotly integrates very well with Node.js and MongoDB. I will take this time to discuss how I
# configured MongoDB and Plotly together, and how those two entities interacted with each
# other. I will be going step by step so you can follow along with me!</p>
# <h2>Step 1: Install MongoDB</h2>
# <p>Installing MongoDB is refreshingly easy. Here I will outline the steps neccessarry to get MongoDB up and
# running. <b>Note</b>: <i>This guide assumes you are running OSX with <a href='http://brew.sh/'>Homebrew</a>
# installed. If difficulties arise please refer to <a href='http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/'>the
# Mongo documentation.</a></i></p>
# <ol>
#   <li>
#     <i>Update homebrew</i>
#     <pre>brew update</pre>
#   </li>
#   <li>
#     <i>Install MongoDB</i>
#     <pre>brew install mongodb</pre>
#   </li>
#   <li>
#     <i>
#       <a href='http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/'>
#         Specify a directory for datastore:
#       </a>
#     </i> 
#     <pre>mkdir -p /data/db</pre>
#   </li>
#   <li>
#     <i> 
#       <a href='http://docs.mongodb.org/manual/reference/program/mongod/#bin.mongod'>
#         Run MongoDB
#       </a> 
#     </i>
#     <pre>mongod</pre></li>
# </ol>
# <h2>Step 2: Configure MongoDB for Node.js</h2>
# <p>If you do not already have <a href=https://nodejs.org/'>Node.js</a>installed, then the first thing you are
# going to want to do is install it via homebrew by simply typing <code>brew install
# node</code> in terminal. Assuming you have Node.js successfully installed on your
# machine, all we need to do is simply create a new Node.js app and download the
# MongoDB drivers for Node via <a href='https://www.npmjs.com/'>npm</a>.</p>
# <ol>
#   <li>
#     <i>
#       Create a new directory for our awesome Node.js app
#     </i>
#     <pre>mkdir appName</pre>
#   </li>
#   <li>
#     <i>
#       cd into directory
#     </i>
#     <pre>cd appName</pre>
#   </li>
#   <li>
#     <i>
#       Initialize npm
#     </i>
#     <pre>npm init</pre> 
#     After you will receive  a series of prompts asking you for additional information for setup. Just keep pressing
#     enter.
#   </li>
#     <img src='http://i.imgur.com/9V1T0dB.png' />
#   <li>
#     <i>
#       Install mongoDB client for Node
#     </i>
#       <pre>npm install mongodb --save</pre>
#   </li>
#   <img src='http://i.imgur.com/8l5vdyn.png'/>
# </ol>
# <h2>Step 3: Configure Plotly for Node.js</h2>
# <ol>
#   <li>
#     <i>
#       Install plotly adapter for Node.js from root directory of app
#     </i>
#     <pre>npm install plotly</pre>
#   </li>
#   <li>
#     <i>
#       Create a new file in app directory named <code>app.js</code>
#     </i>
#     <pre>touch app.js</pre>
#     <p>Since we are going to be using Plotly API to create awesome graphs, now
# would be a good time to create a <a href='https://plot.ly/ssi/'>free plotly
# account</a>. After logging into your plotly account navigate to <a
# href='https://plot.ly/settings/api'>API settings</a>. You will need the provided
# Username and API Key in the next step. From there open the <code>app.js</code>
# file we previously created in your favorite editor of choice.</p>
#   </li>
#   <li>
#     <i>
#       require plotly package and fill in private API information
#     </i>
#     <pre>var plotly = require('plotly')(<i>your API Username here</i>,Your API Key here</i> );</pre>
#   </li>
# </ol>
# <h2>Step 4: Generating Sample Data with MongoDB</h2>
# <p>We now have a file named <code>app.js</code>; this is going to be where we
# pull data from MongoDB and use it to create awesome graphs in real time with
# Plotly API. But first we need to fill MongoDB with some sample data to make our
# awesome graphs with. Create a new file in the app directory named
# <code>testFill.js</code> and include the following code</p>
# <b>testFill.js</b>
# <pre>
# var MongoClient = require('mongodb').MongoClient;
# var tweets = [ 
#   {'message': 'I love barbeque', 'time': '10:44'},
#   {'message': 'When I had it, so I was drunk last night I bought a lizard.', 'time': '10:44'},
#   {'message': 'Finale - thoughts? Check out - an amazing project. and Ed Sheerans latest album please', 'time': '10:44'},
#   {'message': 'A surface preparation? During smoking, Collagen gets turned into Gelatin creating a rub into Gelatin.', 'time': '10:45'},
#   {'message': 'Please sign up at to use the free Twitter Calls service Please sign up at to use the free Twitter Calls.', 'time': '10:46'},
#   {'message': 'Sunday and my happy times.', 'time': '10:46'},
#   {'message': 'Daaaaaaang work to tease me = Omg = do kids hang out digits', 'time': '10:46'},
#   {'message': 'Payday loans in ga loan today all 191 sourcesRelated', 'time': '10:47'}
# ]
# MongoClient.connect('mongodb://127.0.0.1:27017/test10', function(err, db) {
#   var data = db.collection('data');
#     for (var i = 0;i < tweets.length;i++) {
#     data.insert(tweets[i], function(err, success) {
#       if (err)
#         console.log(err);
#       else
#         console.log(success);
#     });
#   }
# });
# </pre>
# <p>After running this code, if you were to go into mongoDB at this point and check the database you
# persisted the <code>data</code> collection into, you would see the list of tweet
# objects we created.</p>
# <img src='http://i.imgur.com/FK9DVUA.png'/>
# <p><i>Note: In the examples I will be showing you we will be using database <code>test10</code></i></p>
# <h2>Step 5: Integrating Plotly and MongoDB</h2>
# <p>Now, let's get back into <code>app.js</code> and use this new Tweet data to
# make an awesome <a href='https://plot.ly/nodejs/time-series/'>time series
# graph</a></p>
# <b>app.js</b>
# <pre>
# var plotly = require('plotly')(<i>your API Username here</i>,Your API Key here</i> );
# var MongoClient = require('mongodb').MongoClient;
# MongoClient.connect('mongodb://127.0.0.1:27017/test10', function(err, db) {
#   var data = db.collection('data')
#     data.find().toArray(function(err, tweets) {
#     var tweetData = formatTweetData(tweets);
#     var data = [{x: tweetData.timeDate, y: tweetData.frequency, type: 'scatter'}];
#     var graphOptions = {
#       'filename': 'TweetTrackr', 
#       'fileopt': 'overwrite', 
#       'layout': {
#         'title': 'Ratio of tweets per minute'
#       },
#       'world_readable': true
#     };
#     plotly.plot(data, graphOptions, function (err, msg) {
#       if (err) return console.log(err);
#       console.log(msg);
#     });
#   });
# });
# function formatTweetData(tweets) {
#   var timeCount = {};
#   var frequency = [];
#   var timeDate = [];
#   for (var i = 0;i < tweets.length;i++) {
#     var time = tweets[i].time;
#     timeCount[time] = timeCount[time] || 0;
#     timeCount[time]++;
#   }
#   for (var key in timeCount) {
#     frequency.push(timeCount[key]);
#     timeDate.push(key);
#   }
#   return {frequency: frequency, timeDate: timeDate};
# }
# </pre>
# <p>The above code will retrieve all entries in our MongoDB <code>data</code>
# collection and convert all that data into an array. After that we call
# the <code>formatTweetData</code> helper function on our array of tweet objects.
# We need the function <code>formatTweetData</code> because the Plotly API
# requires us to provide two arrays. The first array represents all the x coordinates,
# and the second array represents all the y coordinates. There is a one-to-one
# mapping between each element in the two arrays. The first element in the array
# which represents the x coordinate should correspond to the first element in the
# array which represents the y coordinate. This is the line of code where this
# magic happens:
# <pre>
#   var data = [{x: tweetData.timeDate, y: tweetData.frequency, type: 'scatter'}];
# </pre>
# As you can see, we are also including <code>type: 'scatter'</code>. This is
# where we specify the type of graph we want. After we put our graph data in the
# correct format all you need to do is create our <code>graphOptions</code>object
# and pass it all to <code>plotly.plot</code> along with a callback. The callback
# will return an object with a <code>url</code> property.</p> 
# <img src='http://i.imgur.com/g3rrD5O.png?1'/>
# <p>This property contains the url where the graph will be accessible.</p>
# <img src='http://imgur.com/FET85TO.png'/>
# 
