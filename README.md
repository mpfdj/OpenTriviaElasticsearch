# Open trivia open questions
https://github.com/el-cms/Open-trivia-database

# Open trivia multiple choice
https://github.com/uberspot/OpenTriviaQA/tree/master/categories


# Elasticsearch bulk API
https://www.elastic.co/guide/en/elasticsearch/reference/7.0/docs-bulk.html
https://kb.objectrocket.com/elasticsearch/how-to-bulk-import-into-elasticsearch-using-curl

# curl commands
curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/open-trivia/arts-and-literature/_bulk?pretty' --data-binary @arts_and_literature.json


# GET commands for testing
# Returns the top 10 results
GET localhost:9200/open-trivia/arts-and-literature/_search
GET localhost:9200/open-trivia/arts-and-literature/1