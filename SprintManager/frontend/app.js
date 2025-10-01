const API_URL = "http://localhost:8080/api";

async function crearSprint() {
    const data = {
        nombre: document.getElementById("sprint-nombre").value,
        fechaInicio: document.getElementById("sprint-inicio").value,
        fechaFin: document.getElementById("sprint-fin").value,
    };
    await fetch(`${API_URL}/sprints`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    alert("Sprint creado!");
}

async function crearHistoria() {
    const data = {
        descripcion: document.getElementById("story-desc").value,
        estimacion: parseInt(document.getElementById("story-est").value)
    };
    await fetch(`${API_URL}/userstories`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    alert("Historia creada!");
}

async function crearMiembro() {
    const data = {
        nombre: document.getElementById("team-nombre").value,
        rol: document.getElementById("team-rol").value
    };
    await fetch(`${API_URL}/team`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    alert("Miembro agregado!");
}