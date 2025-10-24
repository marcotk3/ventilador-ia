
async function actualizarEstado() {
    const res = await fetch('/estado');
    const data = await res.json();
    document.getElementById('temp').textContent = data.temperatura ?? '--';
    document.getElementById('hum').textContent = data.humedad ?? '--';
    document.getElementById('fan').textContent = data.ventilador ?? '--';
    document.getElementById('conf').textContent = data.confianza ?? '--';
}

setInterval(actualizarEstado, 3000);

function reentrenar() {
    fetch('/reentrenar', { method: 'POST' })
        .then(res => res.json())
        .then(data => alert(data.mensaje));
}

function exportar() {
    fetch('/exportar')
        .then(res => res.json())
        .then(data => alert(data.mensaje));
}
