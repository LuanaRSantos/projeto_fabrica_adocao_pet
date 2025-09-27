# 1 instalar terminal o flask com o comando pip install flask
# 2 adicionar as bicliotecas que usaremos no projeto

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import resend 

resend.api_key = 're_VtASXur2_CbnqTcRKHSdJCmQ4fNiBYSrZ' # chave da API para o envio das mensagens

app= Flask(__name__)
with open('dados.json','r', encoding='utf-8') as arquivo:
    dados= json.load(arquivo)
    
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST': 
        nome=request.form['name']
        email=request.form['email']
        mensagem=request.form['message']
        # montar dicionário da nova mensagem
        dados_mensagem = {
            'nome':nome,
            'email': email,
            'mensagem':mensagem,
            'data': f'{datetime.today()}'
        }
    # adiconar e salvar o json
        dados. append(dados_mensagem)
        with open('dados.json', 'w',encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
        # envia email usando resend
    


        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "luanaribeirodos0688@gmail.com",
        "subject": f"Solicitação de Adoção {nome}",
        "html": f"<p>Email: {email} <br>{mensagem}</p>"
        })
        
# Após o POST - redirecione para enviar reenvio do formulario    

        return redirect(url_for('index'))
# Get - renderizar a página 
    return render_template('index.html') 
        

if __name__ == '__main__':
    app.run(debug=True)
    
    
    