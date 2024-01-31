from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
            {'musica': 'Someone Like You', 'autor': 'Adele Adkins'},
            {'musica': 'Shape of You', 'autor': 'Ed Sheeran'},
            {'musica': 'Halo', 'autor': 'Beyoncé Knowles'},
            {'musica': 'Billie Jean', 'autor': 'Michael Jackson'},
            {'musica': 'Blank Space', 'autor': 'Taylor Swift'}

]

#Rota GET padrão - http://localhost:7777
@app.route('/')
def obter_musicas():
    return jsonify(musicas)

#GET com id - http://localhost:7777/3
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musica_com_id(indice):
    return jsonify(musicas[indice])


#POST - Enviar recursos
@app.route('/musicas', methods=['POST'])
def enviar_musica():
    musica = request.get_json()
    musicas.append(musica)
    #O envio é feito pelo POSTMAN, usando o padrão da API

    return jsonify(f'A musica: {musica} foi adicionada com sucesso', 200)

#PUT - Alterar um recurso existente
@app.route('/musicas/<int:indice>', methods=['PUT'])
def atualizar_musicas(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)
    
    return jsonify(musicas[indice], 200)

#DELETE - Excluir um recurso - http://localhost:7777/3

@app.route('/musicas/<int:indice>', methods=['DELETE'])
def deletar_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluida a música {musicas[indice]}', 200)
    except:
        return jsonify('Não foi possível localizar a música ou autor.')
    




app.run(port=7777, host='localhost', debug= True)