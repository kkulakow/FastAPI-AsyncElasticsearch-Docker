<h1> FastAPI, AsyncElasticsearch in Docker container</h1><br>
<p align="center">
  <em>A very simple search engine for the texts of documents.</em><br>
  <em>The data is stored in the <a href="https://fastapi.tiangolo.com/tutorial/sql-databases/" rel="nofollow">SQLite</a> database, the search index is in <a href="https://elasticsearch-py.readthedocs.io/en/7.10.0/async.html" rel="nofollow">AsyncElasticsearch</a>, and all this works inside <a href="https://fastapi.tiangolo.com/" rel="nofollow">FastAPI.</a></em>.
</p>
<hr data-sourcepos="22:1-23:0"><br><br>
<h2>How to deploy</h2><br>
<li>
  <strong>Pull code</strong>
<pre>$ git clone git@github.com:ggtxRU/FastAPI-AsyncElasticsearch-Docker.git</pre>
</li>
<li>
  <strong>Initialize Docker</strong><br><br>
  <ul><em>Make sure that Docker is installed on your machine, and you are in the directory where docker-compose.yml is.</em></ul>
<pre>$ docker-compose up --build</pre>
  <ul><em>After Docker finishes the build, it will deploy the application on port 8000, if you haven't changed them in docker files configuration.</em></ul>
</li><br>
<h2>Interactive API docs</h2><br>
<li><strong>Go to</strong> <a href="http://localhost:8000/docs" rel="nofollow">localhost:8000/docs</a></li><br>
<ul><em>You will see the automatic interactive API documentation.</em></ul><br>

<h2>Try it in action</h2><br>
<li>Fill database with data from a test csv file ---> <a href="http://localhost:8000/docs#/DB/fillingdb_fillingdb_post"><strong>[POST]</strong> /fillingdb</a></li>
<li>Fill Elastic with data from database ---> <a href="http://localhost:8000/docs#/Elasticsearch/filling_fillingES_post"><strong>[POST]</strong> /fillingES</a></li>
<li>Get document by keyword ---> <a href="http://localhost:8000/docs#/Elasticsearch/get_elastic_get__get"><strong>[GET]</strong> /elastic/get/</a></li>
<li>Delete document by id ---> <a href="http://localhost:8000/docs#/Delete%20from%20ES%20%26%20DB/delete_delete__id__delete"><strong>[DELETE]</strong> /elastic/get/</a></li>
