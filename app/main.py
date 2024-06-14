from flask import Flask, request, jsonify
from logging_config import LoggerSetup
import logging

logger_setup = LoggerSetup()

logger = logging.getLogger(__name__)

app = Flask(__name__)

blog_posts = []

class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}

@app.route('/blog', methods=['POST'])
def create_blog_post():
    try:
        logger.warning('Criação de um novo blog - POST')
        data = request.get_json()
        blog_posts.append(BlogPost(data['id'], data['title'], data['content']))
        return jsonify({'status':'sucess'}), 201
    except KeyError:
        logger.warning('Erro na criação de um novo blog - POST')
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/blog', methods=['GET'])
def get_blog_posts():
    logger.warning('Listagem de todos os blogs - GET')
    return jsonify({'posts': [blog.toJson() for blog in blog_posts]}), 200


@app.route('/blog/<int:id>', methods=['GET'])
def get_blog_post(id):
    logger.warning(f"Listagem de um blog específico id {id}- GET")
    for post in blog_posts:
        if post.id == id:
            logger.warning(f"Listagem de um blog específico id {id} - GET - Encontrado")
            return jsonify({'post': post.__dict__}), 200
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['DELETE'])
def delete_blog_post(id):
    logger.warning(f"Deletar um blog específico id {id} - DELETE")
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return jsonify({'status':'sucess'}), 200
    return jsonify({'error': 'Post not found'}), 404

@app.route('/blog/<int:id>', methods=['PUT'])
def update_blog_post(id):
    try:
        logger.warning(f"Atualização de um blog específico id {id} - PUT")
        data = request.get_json()
        for post in blog_posts:
            if post.id == id:
                post.title = data['title']
                post.content = data['content']
                logger.warning(f"Atualização de um blog específico id {id} - PUT - Realizado")
                return jsonify({'status':'sucess'}), 200
        logger.warning(f"Atualização de um blog específico id {id} - PUT - Não encontrado")
        return jsonify({'error': 'Post not found'}), 404
    except KeyError:
        return jsonify({'error': 'Invalid request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)