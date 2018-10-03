from flaskblog import celery_down


@celery_down.task
def download_text(content):
    with open('blog.txt', 'w') as file_handler:
        file_handler.write(content)
    return 'blog.txt'
