from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import current_user

from apps.app import db
from apps.board.models import Board, Reply

reply = Blueprint(
  "reply",
  __name__
)

@reply.route('/new/<board_id>', methods=['POST'])
def new_reply(board_id):
  content = request.form['content'] # html에 name=content인 것
  # reply = Reply(content=content, user_id=current_user.id, board_id=board_id)
  # db.session.add(reply)
  # db.session.commit()

  board = Board.query.get(board_id)
  reply = Reply(content=content, user_id=current_user.id)
  board.reply_list.append(reply) 
  # board.reply_list : 게시글에 등록된 댓글 목록들을 가져옴
  # user.user_replies : 특정 사용자가 작성한 (게시글, 댓글) 목록들을 가져옴

  db.session.commit()

  return redirect(url_for('board.detail', board_id=board_id))


@reply.delete('/<reply_id>')
def delete_reply(reply_id):
  reply = Reply.query.get(reply_id)

  try:
    db.session.delete(reply)
    db.session.commit()
    return jsonify({'message' : '댓글 삭제 완료'}), 200
  except Exception:
    db.session.rollback()
    return jsonify({'message' : '댓글 삭제 실패'}), 500
  


@reply.put('/<reply_id>')
def edit_reply(reply_id):
  data = request.json
  
  try:
    reply = Reply.query.get(reply_id)
    reply.content = data.get('content')
    db.session.commit()
    return jsonify( {'status':'success', 'message':'댓글 수정 완료'} ), 200
  except Exception:
    db.session.rollback()
    return jsonify( {'status':'error', 'message':'댓글 수정 실패'} ), 500