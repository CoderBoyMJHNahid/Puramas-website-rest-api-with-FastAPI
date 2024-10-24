import requests
from db.conn import conn, connection
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BLOG_ID = os.environ.get("BLOG_ID")
base_url = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts'

def fetch_all_posts():
    posts = []
    next_page_token = None
    while True:
        params = {'key': API_KEY}
        if next_page_token:
            params['pageToken'] = next_page_token
        
        response = requests.get(base_url, params=params)
        data = response.json()
        posts.extend(data.get('items', []))
        next_page_token = data.get('nextPageToken')
        
        if not next_page_token:
            break

    return posts


def get_post():
    data = fetch_all_posts()
    # return {"data":data}
    sql = """
        INSERT INTO `posts` (`title`, `post_description`, `blog_id`, `item_id`, `kind`, `labels`, `etag`, `published`, `updated`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    sql2 = "SELECT * FROM posts WHERE item_id = %s"
    for item in data:
        
        conn.execute(sql2,(item['id'],))

        exist = conn.fetchall()
        
        if not exist:

            labels = ', '.join(item.get('labels', []))
            value = (item['title'],item['content'],item['blog']['id'],item['id'],item['kind'],labels,item['etag'],item['published'],item['updated'])
            conn.execute(sql,value)
        
        connection.commit()
     
    print({"message": "Successfully inserted all posts", "status" : True}) if conn.rowcount else print({"massage":"Something is wrong"})
    # return {"message": "Successfully inserted all posts", "status" : True} if conn.rowcount else {"massage":"Something is wrong"}

if __name__ == "__main__":
    get_post()