import psycopg2


# What are the most popular three articles of all time?
def get_articles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(
        "SELECT log.path, count(*) as num from log " +
        "INNER JOIN articles ON (REPLACE(log.path, '/article/', '') = articles.slug) " +
        "GROUP BY path order by num desc LIMIT 3")
    articles = cursor.fetchall()
    db.close()
    return articles
