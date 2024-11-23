from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)

# Cargar los datos de juegos desde el archivo JSON
with open('data/games.json') as f:
    games = json.load(f)

class GameData:
    def __init__(self, games):
        self.games = games

    def get_primeras_jugadas(self):
        jugadas = []
        for game in self.games:
            jugada = {
                'blancas': game['moves'][0],
                'negras': game['moves'][1]
            }
            if jugada not in jugadas:
                jugadas.append(jugada)
        return jugadas

    def get_winrate(self, blancas, negras):
        white_wins = black_wins = draws = 0
        total = 0
        for game in self.games:
            if game['moves'][0] == blancas and game['moves'][1] == negras:
                total += 1
                if game['result'] == '1-0':
                    white_wins += 1
                elif game['result'] == '0-1':
                    black_wins += 1
                else:
                    draws += 1
        return {
            'white': (white_wins / total) * 100 if total > 0 else 0,
            'black': (black_wins / total) * 100 if total > 0 else 0,
            'draw': (draws / total) * 100 if total > 0 else 0
        }

class FilteredGameData(GameData):
    def __init__(self, games):
        super().__init__(games)

    def get_incremento(self, intervalo):
        # Función de filtrado para determinar si un juego pertenece al intervalo de ELO especificado
        def filter_games(game):
            white_rating = int(game['white_rating'])
            black_rating = int(game['black_rating'])
            # Programación lógica: Condiciones para filtrar juegos según el intervalo de ELO
            if intervalo == 'menos-de-mil':
                return white_rating < 1000 and black_rating < 1000
            elif intervalo == 'mil-a-dosmil':
                return 1000 <= white_rating <= 2000 and 1000 <= black_rating <= 2000
            elif intervalo == 'mas-de-dosmil':
                return white_rating > 2000 and black_rating > 2000
            return False

        # Usar la función de filtrado para obtener los juegos que cumplen con la condición lógica
        filtered_games = filter(filter_games, self.games)
        incrementos = {}
        total_games = 0

        for game in filtered_games:
            incremento = game['increment_code']
            total_games += 1
            if incremento in incrementos:
                incrementos[incremento] += 1
            else:
                incrementos[incremento] = 1

        # Agrupar incrementos menores al 2% en "Otros"
        otros = 0
        for incremento in list(incrementos.keys()):
            if (incrementos[incremento] / total_games) * 100 < 2:
                otros += incrementos.pop(incremento)

        if otros > 0:
            incrementos['Otros'] = otros

        return incrementos

    def get_cantidad_jugadores(self):
        menos_de_mil = 0
        mil_a_dosmil = 0
        mas_de_dosmil = 0

        for game in self.games:
            white_rating = int(game['white_rating'])
            black_rating = int(game['black_rating'])
            promedio = (white_rating + black_rating) / 2

            # Programación lógica: Condiciones para contar jugadores según el intervalo de ELO
            if promedio < 1000:
                menos_de_mil += 1
            elif 1000 <= promedio <= 2000:
                mil_a_dosmil += 1
            else:
                mas_de_dosmil += 1

        return {
            'menos_de_mil': menos_de_mil,
            'mil_a_dosmil': mil_a_dosmil,
            'mas_de_dosmil': mas_de_dosmil
        }

game_data = FilteredGameData(games)

# Ruta para servir la página principal
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Ruta para obtener las primeras jugadas
@app.route('/api/primeras-jugadas')
def primeras_jugadas():
    jugadas = game_data.get_primeras_jugadas()
    return jsonify(jugadas)

# Ruta para obtener el win rate basado en las primeras dos jugadas
@app.route('/api/winrate')
def winrate():
    blancas = request.args.get('blancas')
    negras = request.args.get('negras')
    winrate_data = game_data.get_winrate(blancas, negras)
    return jsonify(winrate_data)

# Ruta para obtener el tipo de incremento basado en el intervalo de ELO
@app.route('/api/incremento')
def incremento():
    intervalo = request.args.get('intervalo')
    incremento_data = game_data.get_incremento(intervalo)
    return jsonify(incremento_data)

# Ruta para obtener la cantidad de jugadores por intervalo de ELO
@app.route('/api/cantidad-jugadores')
def cantidad_jugadores():
    cantidad_jugadores_data = game_data.get_cantidad_jugadores()
    return jsonify(cantidad_jugadores_data)

if __name__ == '__main__':
    app.run(debug=True)