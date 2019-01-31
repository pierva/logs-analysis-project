import psycopg2


# What are the most popular three articles of all time?
def get_articles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "SELECT title, count(*) as num FROM articles " +
        "JOIN log ON (REPLACE(log.path, '/article/', '') = articles.slug) " +
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
