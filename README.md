<h1> FastAPI, AsyncElasticsearch in Docker container</h1><br>
<p align="center">
  <em>A very simple search engine for the texts of documents.</em><br>
  <em>The data is stored in the <a href="https://fastapi.tiangolo.com/tutorial/sql-databases/" rel="nofollow">SQLite</a> database, the search index is in <a href="https://elasticsearch-py.readthedocs.io/en/7.10.0/async.html" rel="nofollow">AsyncElasticsearch</a>, and all this works inside <a href="https://fastapi.tiangolo.com/" rel="nofollow">FastAPI.</a></em>.
</p>
<hr data-sourcepos="22:1-23:0"><br><br>
<h2>How to use it</h2><br>
<li>
  <strong>Pull code</strong>
<pre>$ git clone git@github.com:ggtxRU/FastAPI-AsyncElasticsearch-Docker.git</pre>
</li>
<li>
  <strong>Initialize Docker</strong><br><br>
  <ul><em>Make sure that Docker is installed on your machine, and you are in the directory where docker-compose.yml is.</em></ul>
<pre>$ docker-compose up --build</pre>
  <ul><em>After Docker finishes the build, it will deploy the application on port 8000, if you haven't changed them in docker files configuration.</em></ul>
</li>
<h2>Interactive API docs</h2><br>
<li><strong>Go to</strong> <a href="http://localhost:8000/docs" rel="nofollow">localhost:8000/docs</a></li><br>
<ul><em>You will see the automatic interactive API documentation.</em></ul>
