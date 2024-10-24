from fastapi import APIRouter
from ..db.conn import conn,connection

router = APIRouter()

@router.get("/posts/")
def fetch_posts():
    
    sql = "SELECT * FROM `fr_posts` ORDER BY `id` ASC"
    conn.execute(sql)
    posts = conn.fetchall()
    column_names = [i[0] for i in conn.description] 

    formatted_posts = []
    for post in posts:
        formatted_posts.append(dict(zip(column_names, post)))
    
    return {
        "data": formatted_posts,
        "status": True
    }
    

@router.get("/post/{item_id}")
def fetch_single_post(item_id:int):
    sql = "SELECT * FROM `fr_posts` WHERE id = %s"
    conn.execute(sql,(item_id,))
    posts = conn.fetchall()
    column_names = [i[0] for i in conn.description] 

    formatted_posts = []
    for post in posts:
        formatted_posts.append(dict(zip(column_names, post)))
    
    return {
        "data": formatted_posts,
        "status": True
    }