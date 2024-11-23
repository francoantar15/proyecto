class Grafico {
    constructor() {
        document.addEventListener('DOMContentLoaded', () => {
            this.cargarJugadasIniciales();
            this.configurarEventos();
        });
    }

    cargarJugadasIniciales() {
        fetch('/api/primeras-jugadas')
            .then(response => response.json())
            .then(data => {
                console.log(data); // Verificar los datos recibidos
                const tableBody = document.getElementById('jugadas-table');
                const jugadasBlancas = new Set();
                const jugadasNegras = new Set();

                data.forEach(jugada => {
                    jugadasBlancas.add(jugada.blancas);
                    jugadasNegras.add(jugada.negras);
                });

                const maxJugadas = Math.max(jugadasBlancas.size, jugadasNegras.size);
                const jugadasBlancasArray = Array.from(jugadasBlancas);
                const jugadasNegrasArray = Array.from(jugadasNegras);

                for (let i = 0; i < maxJugadas; i++) {
                    const row = document.createElement('tr');

                    const blancaCell = document.createElement('td');
                    if (jugadasBlancasArray[i]) {
                        blancaCell.textContent = jugadasBlancasArray[i];
                        blancaCell.classList.add('selectable');
                        blancaCell.dataset.color = 'blancas';
                    } else {
                        blancaCell.textContent = 'seleccion';
                        blancaCell.classList.add('selectable');
                        blancaCell.dataset.color = 'blancas';
                    }
                    row.appendChild(blancaCell);

                    const negraCell = document.createElement('td');
                    if (jugadasNegrasArray[i]) {
                        negraCell.textContent = jugadasNegrasArray[i];
                        negraCell.classList.add('selectable');
                        negraCell.dataset.color = 'negras';
                    } else {
                        negraCell.textContent = 'seleccion';
                        negraCell.classList.add('selectable');
                        negraCell.dataset.color = 'negras';
                    }
                    row.appendChild(negraCell);

                    tableBody.appendChild(row);
                }

                tableBody.addEventListener('click', function(event) {
                    if (event.target.classList.contains('selectable')) {
                        const color = event.target.dataset.color;
                        const selected = tableBody.querySelector(`.selected[data-color="${color}"]`);
                        if (selected) {
                            selected.classList.remove('selected');
                        }
                        event.target.classList.add('selected');
                    }
                });
            })
            .catch(error => console.error('Error:', error));
    }

    configurarEventos() {
        document.getElementById('mostrar-winrate').addEventListener('click', () => {
            const blancas = document.querySelector('.selected[data-color="blancas"]');
            const negras = document.querySelector('.selected[data-color="negras"]');
            if (blancas && negras) {
                this.mostrarWinRate(blancas.textContent, negras.textContent);
            } else {
                alert('Por favor, selecciona una jugada para las blancas y una para las negras.');
            }
        });

        document.getElementById('mostrar-incremento').addEventListener('click', () => {
            const intervaloElo = document.getElementById('elo-select').value;
            this.mostrarIncremento(intervaloElo);
        });

        document.getElementById('mostrar-cantidad-jugadores').addEventListener('click', () => {
            this.mostrarCantidadJugadores();
        });
    }

    mostrarWinRate(blancas, negras) {
        fetch(`/api/winrate?blancas=${blancas}&negras=${negras}`)
            .then(response => response.json())
            .then(data => {
                console.log(data); // Verificar los datos recibidos
                const trace = {
                    x: ['Blancas', 'Negras', 'Empates'],
                    y: [data.white, data.black, data.draw],
                    type: 'bar',
                    marker: {
                        color: ['blue', 'black', 'gray']
                    }
                };
                const layout = {
                    title: `Win Rate para ${blancas} ${negras}`,
                    xaxis: { title: 'Resultado' },
                    yaxis: { title: 'Porcentaje' }
                };
                Plotly.newPlot('grafico', [trace], layout);
            })
            .catch(error => console.error('Error:', error));
    }

    mostrarIncremento(intervaloElo) {
        fetch(`/api/incremento?intervalo=${intervaloElo}`)
            .then(response => response.json())
            .then(data => {
                console.log(data); // Verificar los datos recibidos
                const trace = {
                    labels: Object.keys(data),
                    values: Object.values(data),
                    type: 'pie'
                };
                const layout = {
                    title: `Tipos de Incremento para ELO ${intervaloElo.replace('-', ' a ')}`
                };
                Plotly.newPlot('grafico-incremento', [trace], layout);
            })
            .catch(error => console.error('Error:', error));
    }

    mostrarCantidadJugadores() {
        fetch('/api/cantidad-jugadores')
            .then(response => response.json())
            .then(data => {
                console.log(data); // Verificar los datos recibidos
                const trace = {
                    x: ['Menos de 1000', '1000 a 2000', 'Más de 2000'],
                    y: [data.menos_de_mil, data.mil_a_dosmil, data.mas_de_dosmil],
                    type: 'bar',
                    marker: {
                        color: ['red', 'green', 'blue']
                    }
                };
                const layout = {
                    title: 'Cantidad de Jugadores por Intervalo de ELO',
                    xaxis: { title: 'Intervalo de ELO' },
                    yaxis: { title: 'Cantidad de Jugadores' }
                };
                Plotly.newPlot('grafico-cantidad-jugadores', [trace], layout);
            })
            .catch(error => console.error('Error:', error));
    }
}

// Inicializar la clase Grafico
new Grafico();