import facebook as fb
import requests
import argparse
import textblob as tb

FLAGS = None


def sentiment_analysis(post):
    # Here's where the magic happens
    tb_msg = tb(post['message'])
    score = tb_msg.sentiment

    print("Date: %s, From: %s\n", post['created_time'], post['from'])
    print("%s\nShared: %s, Score: %f", post['message'], post['share'], score)


def connect(access_token, user):
    # graph = fb.GraphAPI(access_token)
    graph = fb.GraphAPI(access_token=access_token, version="2.12")
    profile = graph.get_object(user)

    return graph, profile


def main():
    access_token = "e937c086f176478b4a7d3b2cb81a9612"
    user = "cristianqp"

    graph, profile = connect(access_token, user)

    posts = graph.get_connections(profile['id'], 'posts')

    # Let's grab all the posts and analyze them!
    while True:
        try:
            [sentiment_analysis(post=post) for post in posts['data']]
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break


if __name__ == "__main__":
    main()