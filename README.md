# Open trivia open questions
https://github.com/el-cms/Open-trivia-database

# Open trivia multiple choice
https://github.com/uberspot/OpenTriviaQA/tree/master/categories

# Elasticsearch docs
https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html

# Elasticsearch bulk API
https://www.elastic.co/guide/en/elasticsearch/reference/7.0/docs-bulk.html
https://kb.objectrocket.com/elasticsearch/how-to-bulk-import-into-elasticsearch-using-curl

# curl commands
curl -H "Content-Type: application/x-ndjson" -XPOST "localhost:9200/open-trivia/_bulk?pretty" --data-binary @es-data.json


# GET commands for testing
# Returns the top 10 results
GET localhost:9200/open-trivia/_doc/1
GET localhost:9200/open-trivia/_search

# Get indices
GET localhost:9200/_cat/indices?v=true

# Create index with a mapping
PUT localhost:9200/open-trivia
{
  "mappings": {
    "properties": {
      "category": {
        "type": "keyword"
      },
      "question": {
        "type": "text"
      },
      "type": {
        "type": "keyword"
      },
      "answer": {
        "type": "text"
      },
      "choices": {
        "type": "text"
      }
    }
  }
}

# Get mapping definition
GET localhost:9200/open-trivia/_mapping

# Example document
{
    "_index": "open-trivia",
    "_type": "_doc",
    "_id": "1",
    "_version": 1,
    "_seq_no": 0,
    "_primary_term": 1,
    "found": true,
    "_source": {
        "category": "music",
        "question": "The controversial lyrics of this song by The Rolling Stones include, Its Down to me, the way she talks when shes spoken to",
        "type": "multiple-choice",
        "answer": "Under My Thumb",
        "choices": [
            "Heart of Stone",
            "Under My Thumb",
            "Play With Fire",
            "Its All Over Now"
        ]
    }
}

# Fetch a record
POST localhost:9200/open-trivia/_search
{
  "query" : {
    "query_string" : {
      "query" : "3",
      "fields"  : ["_id"]
    }
  }
}

# Get all categories
POST localhost:9200/open-trivia/_search
{
  "size": 0,
  "aggregations": {
    "category": {
      "terms": {
        "field": "category"
      }
    }
  }
}

# Get a random document where category is music
POST localhost:9200/open-trivia/_search
{
  "size": 1,
  "query": {
    "function_score": {
      "query": { "match": { "category": "music" } },
      "boost": "5",
      "random_score": {}, 
      "boost_mode": "multiply"
    }
  }
}