#!/usr/bin/env python3

# internal reporting about news site's user activity

import psycopg2
from datetime import date

DBNAME = "news"

# queries
query1 = ("select articles.title, count(*) as views "
            "from articles, log "
            "where log.path like concat('/article/',articles.slug) "
            "group by articles.title "
            "order by views desc "
            "limit 3; ")

query2 = ("select name, views "
            "from (select * from articles "
                "left join authors "
                "on articles.author = authors.id) as a, "
                "(select author, count (*) as views "
                "from articles, log "
                "where log.path like concat('/article/',articles.slug) "
                "group by author) as b "
            "where a.author = b.author "
            "group by name, b.views "
            "order by views desc; "
            )

query3 = ("select date, percenterror "
            "from (select date(time), round(100.0*sum(case log.status "
                "when '200 OK' then 0 else 1 end)/count(log.status),2) "
                "as percenterror "
                "from log "
                "group by date(time)) as a "
            "where a.percenterror > 1 "
            "group by date, a.percenterror; ")

# returns query results
def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# creates a dictionary for each query
query_1_results = {}
query_1_results['title'] = "\nThe 3 most popular articles of all time:\n"
query_1_results['results'] = get_results(query1)

query_2_results = {}
query_2_results ['title'] = "\nThe most popular authors of all time:\n"
query_2_results ['results']= get_results(query2)

query_3_results = {}
query_3_results ['title'] = "\nDays with more than 1% of requests that lead to an error:\n"
query_3_results ['results']= get_results(query3)

# format query result for printing
def print_views_result(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t"' + str(result[0]) + '" ——— ' + str(result[1]) + ' views')

def print_error_result(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0].strftime('%B %d, %Y')) + ' ——— ' + str(result[1]) + ' %')

# print formatted results
print_views_result(query_1_results)
print_views_result(query_2_results)
print_error_result(query_3_results)
