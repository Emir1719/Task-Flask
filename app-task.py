from app import create_app, db

app = create_app()

if __name__ == "__main__":
    # Veritabanını başlatmak için tabloları oluşturun
    with app.app_context():
        db.create_all()  # Tüm tabloları oluşturur

    app.run(debug=True, host='0.0.0.0', port=5000)
