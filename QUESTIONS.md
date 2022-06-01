Think about these questions while you build your implementation. Then, before you
submit, please provide written answers to the following:

  * Why did you choose the specific architecture, packages, etc. that you used to
  implement your solution? What alternate options did you try, if any?

  * Answer: I've decided to implement my solution using FAST API because it's a high-performing, 
  asynchronous, non-blocking framework to build API's that allows to use async callbacks on each calls
  and aggregate them once we have the results. My alternate option was using Flask or Django.

  * How will your implementation handle multiple concurrent requests? How would it 
  handle them in an ideal situation (regardless of your specific implementation, 
  which is allowed to be minimal)?

  * Answer: To my knowledge sqlite3 library that communicates with the database doesn't have support for using 
  async/await therefore, I wasn't able to fully take advantage of FAST API's asynchronism, concurrency 
  and parallelism. Also this implementation might not behave as intented for operations that involve 
  many concurrent requests because I used a server library called Uvicorn that runs a single process.
  When deploying it to a real server, I would need to use Gunicorn with Uvicorn worker processes that 
  provides replication of processes to take advantage of multiple cores and to be able to handle more requests.

  * How will your implementation perform with hundreds of thousands of keys? 
  With millions?

  * Answer: My implementation should be capable of performing operations with hunderds of thousands of keys since SQLite doesn't 
  need to fit a dataset to RAM. By default, it caches up to cache_size pages.

  * How will your implementation handle restarts? Will it keep previously stored values,
  or will it lose them between startups?

  * Answer: My implementation will not be able to handle restarts, because it won't start automatically on server startup. 
  To achieve this, I would need to use a separate resources that would make sure the app is starts up after restarts.
  Example Tools:  Docker, Kubernetes, Systemd, Supervisor and etc..

  * In the real world (e.g. outside of the arbitrary constraints of this problem) how
  would you go about solving the request (providing a simple key-value store API)?
  How would you deploy it?

1) SQLiteDict or SQLAlchemy ORM.
2) Using Pydantic or ORM models.
3) Using Fast API's Async/Await.
4) Alembic Database Migration Tool.
5) Docker or Kubernetes.
6) CI/CD Pipeline.
7) NGINX/Apache.