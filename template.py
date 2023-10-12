from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 데이터를 저장할 딕셔너리 초기화
members = {}
books = {}

# 홈 페이지
@app.route('/')
def home():
    return render_template('index.html', members=members, books=books)

# 멤버 추가
@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form.get('member_name')
    member_phone = request.form.get('member_phone')
    if member_name and member_phone:
        members[member_name] = {"phone": member_phone, "books": []}
    return redirect(url_for('home'))

# 멤버 삭제
@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_name = request.form.get('member_name')
    if member_name in members:
        del members[member_name]
    return redirect(url_for('home'))

# 책 추가
@app.route('/add_book', methods=['POST'])
def add_book():
    book_name = request.form.get('book_name')
    if book_name:
        books[book_name] = {"status": "available"}  # 책 상태를 딕셔너리로 저장
    return redirect(url_for('home'))

# 책 삭제
@app.route('/delete_book', methods=['POST'])
def delete_book():
    book_name = request.form.get('book_name')
    if book_name in books:
        del books[book_name]
    return redirect(url_for('home'))

# 책 대출
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form.get('member_name')
    book_name = request.form.get('book_name')
    if member_name in members and book_name in books and books[book_name]["status"] == "available":
        members[member_name]["books"].append(book_name)
        books[book_name]["status"] = "checked_out"
    return redirect(url_for('home'))

# 책 반납
@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form.get('member_name')
    book_name = request.form.get('book_name')
    if member_name in members and book_name in books and books[book_name]["status"] == "checked_out":
        members[member_name]["books"].remove(book_name)
        books[book_name]["status"] = "available"
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
