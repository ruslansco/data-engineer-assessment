# Getting Started

Welcome to Data Engineer take-home skills test! Please refer to the following
document for instructions.

You will require a local installation of Python 3.9+ during development.
There are no other hard prerequisites, although there are many external packages that
you may want to install/use as dependencies.

# The Problem

The maintainers of every key-value store have decided to delete all of their
code and retire early. They managed to convince every organization to delete any backups
they may have made of their code base and binaries. That means no more `redis`, 
`memcached`, `etcd`, and so on.

This is bad news for us at MAPMG: we were just about to deploy a project that required a
key-value store! Now we will have to implement one from scratch.

# Your Solution

You will have to implement a *very basic* key-value store as a locally-hosted REST API.

We only need the ability to store and retrieve strings, without concerns for atomicity.

Your solution will have to implement the following endpoints:
  * `/set`: Sets a key in the store.
    * This will be a POST request that can receive JSON matching the following schema:
    * ```
      "key": str 
      "val": str
      ```

  * /get/\<key\>: Retrieves the value of a given key.
    * This will be a GET request that returns JSON matching the following schema:
    * ```
      "key": str
      "val": str
      ```
    * If a given key does not have a value associated with it, then this should return
    a 404 HTTP error.

Your solution should also pre-populate a handful of keys on startup, based on the
contents of a local SQLite3 database (`input.db`), which will be located at the top
level of this repo. Crucially, you will not have access to this database during
development, although the table specification is available to you.

# Deployment Specs

We will be evaluating your solution both manually (looking at your code) and
automatically (running secret unit tests).

At the very least, your code should be installable by running
`pip install -e .` at the top level of this repo, and
runnable via `python -m mapmg_data_engineer_takehome`. You can add any files you need,
as long as those 2 constraints hold. Note that `python -m` will run everything under
the specified package's `__main__.py` file (assuming it's installed and importable).

If you wish, you can opt to use a virtual environment
(e.g. the `venv` package + `requirements.txt`, or similar),
or provide a Dockerfile that will install dependencies for us. If you do so, please
provide any necessary documentation for how to install/run your solution.
 
Regardless of what you do, your code should be runnable on an
arbitrary machine. You can assume that we will already have Python 3.9+ 
and `docker` (but *not* `docker-compose`) installed. Any other dependencies you 
may require should be documented (and easily installable under the usual methods).

# Bonus Points

Inspect the Git history of this repo to see if you can locate the secret code! Further
instructions are present in the same location. If you don't do this, we won't hold it
against you.