function apagar_compra(id){
    fetch(`compras/excluir/${id}`, {
        method: 'GET',
    }).then(response => {
        if(response.ok){
            window.location.reload();
        }
    }).then(error => {
        console.log(error)
    });
}
