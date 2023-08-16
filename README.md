# PipelineGPT: Generate Daily Report with OpenAI

Demo project to build an enriched ChatGPT responses using embeddings.

## Requirements

- Python 3
- A OpenAI API account
- A Starter Plan Pinecone account (free)

## Installation

1. Clone the repository
2. Create a virtualenv for Python:
    ```bash
    $ virtualenv venv
    $ source venv/bin/activate
    ```
3. Install dependencies
    ```bash
    $ pip install -r requirements.txt
    ```
4. Initialize environment file. Add your Pinecone and OpenAI API Keys
    ```bash
    $ cp env-example .env
    $ nano .env
    ```

## Create embeddings database

1. Update your database connection in .env file
    ```bash
    # MYSQL ENVIRONMENT
    DB_HOST='localhost'
    DB_PORT='3306'
    DB_USER='root'
    DB_PASSWORD='password'
    DB_NAME='demo_db'
    ```
2. Create a Pinecone database
    ```bash
    $ source venv/bin/activate
    $ source .env
    $ cd database
    $ python db_create.py
    ```
3. Create embeddings and upload them to Pinecone. 
    ```bash
    $ source venv/bin/activate
    $ source .env
    $ cd database
    $ python index_docs.py

    Extracted 100 from rs database: hapo_rs_stg
    Example data: [...]
    Creating embeddings and uploading vectors to database
    100%|███████████████████████████████████████████████████████████████████████████████████| 2/2 [00:06<00:00,  3.40s/it]
    Database contains 33 vectors.
    ```

## Run your query

```bash
$ source venv/bin/activate
$ source .env
$ python query.py "Create daily report for 2021-04-06"
Found 22 contexts for your query
Working on your query...

Daily Report - 2021-04-06

Tasks Completed:
- Exported csv file for data analysis.
- Investigated issues with cronjob and identified the root cause.
- Reviewed and approved pull requests for code changes.
- Deployed server updates.

Next Steps:
- Continue working on the assigned tasks for the next day.

Challenges Faced:
- Encountered some difficulties while investigating the cronjob issues, but managed to resolve them with the help of the team.

Additional Notes:
- The csv export was successful and the data is ready for analysis.
- The server deployment went smoothly and all updates are now live.

```

