import psycopg2


# What are the most popular three articles of all time?
def get_articles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "SELECT title, count(*) as num from articles " +
        "JOIN log ON (REPLACE(log.path, '/article/', '') = articles.slug) " +
        "GROUP BY title ORDER BY num DESC LIMIT 3")
    articles = cursor.fetchall()
    db.close()
    return articles
