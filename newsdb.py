import psycopg2


# What are the most popular three articles of all time?
def get_articles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "SELECT title, count(*) as num FROM articles " +
        "JOIN log ON (REPLACE(log.path, '/article/', '') = articles.slug) " +
        "WHERE log.status='200 OK' AND log.method='GET' "+
        "GROUP BY title ORDER BY num DESC LIMIT 3"
    )
    articles = cursor.fetchall()
    db.close()
    return articles

# Who are the most popular article authors of all time?
def get_popular_author():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "SELECT name, count(*) as num FROM authors " +
        "INNER JOIN articles ON (authors.id = articles.author) " +
        "INNER JOIN log ON (REPLACE(log.path, '/article/', '') = articles.slug) " +
        "GROUP BY name ORDER BY num DESC"
    )
    authors = cursor.fetchall()
    db.close()
    return authors

 # On which days did more than 1% of requests lead to errors?
def get_errors():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "CREATE VIEW total_req AS " +
        "SELECT date(time), count(*) as total from log " +
        "GROUP BY date(time); "
        "CREATE VIEW error_req AS " +
        "SELECT date(time), count(*) as errors FROM log " +
        "WHERE status != '200 OK' " +
        "GROUP BY date(time); "
        "SELECT error_req.date, errors, total_req.total FROM error_req "+
        "INNER JOIN total_req ON (total_req.date = error_req.date) " +
        "WHERE (100 * errors / total) > 1"
    )
    dates = cursor.fetchall()
    db.close()
    return dates;
