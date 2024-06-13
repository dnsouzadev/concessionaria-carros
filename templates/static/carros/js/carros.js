function apagar_carro(id){
    console.log('clicou')
    fetch(`excluir/${id}`, {
        method: 'GET',
    }).then(response => {
        if(response.ok){
            window.location.reload();
        }
    }).then(error => {
        console.log(error)
    });
}

function pesquisar_carro() {
    let query = document.getElementById('query').value;
    fetch(`buscar_carro/${query}`, {
        method: 'GET',
    }).then(response => {
        if(response.ok){
            return response.json(); // Converte a resposta para JSON
        }
        throw new Error('Erro ao buscar carros');
    }).then(data => {
        const hidden = document.getElementById('hidden')
        const show = document.getElementById('show')

        hidden.style.display = 'none'
        show.style.display = 'block'

        let carros = data.carros; // Pega os dados da resposta JSON

        atualizarTabela(carros); // Atualiza a tabela com os dados recebidos

    }).catch(error => {
        console.error(error); // Captura e exibe qualquer erro
    });
}


function atualizarTabela(carros) {
    let tabela = document.getElementById('tabela-carros');
    tabela.innerHTML = ''; // Limpa os dados anteriores da tabela
    carros.forEach(carro => {
        let row = tabela.insertRow();
        row.innerHTML = `
            <td>${carro.modelo}</td>
            <td>${carro.marca}</td>
            <td>${carro.ano}</td>
            <td>${carro.preco_formatado}</td>
            <td>${carro.cor}</td>
            <td>${carro.estoque}</td>
            <td>
                <a href="{% url 'editar_carro' carro.id %}" class="btn btn-warning btn-sm">
                    <i class="fas fa-edit"></i>
                </a>
                <a onclick="apagar_carro(${carro.id})" class="btn btn-danger btn-sm">
                    <i class="fas fa-trash"></i>
                </a>
            </td>
        `;
    });
}
