from flask import Flask, request

app = Flask(__name__)

@app.route('/enviar', methods=['POST'])
def receber_dados():
    nome = request.form.get('login')
    mensagem = request.form.get('senha')

    print(f"Nome: {login}")
    print(f"Mensagem: {senha}")

    return "Dados recebidos no backend!", 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)