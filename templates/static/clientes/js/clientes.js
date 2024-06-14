function deletar_cliente(id){
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
