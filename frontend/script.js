let socket;
let currentUser = "";

function connect() {
  const u = document.getElementById("username").value;
  const r = document.getElementById("room").value;

  if (!u || !r) {
    alert("Username and room are required");
    return;
  }

  currentUser = u;
  socket = new WebSocket(`ws://localhost:8000/ws/${r}/${u}`);

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === "users") {
      const usersList = document.getElementById("users");
      usersList.innerHTML = "";
      data.users.forEach(user => {
        usersList.innerHTML += `<li>${user}</li>`;
      });
    }

    if (data.type === "message") {
      const messages = document.getElementById("messages");

      const div = document.createElement("div");
      div.classList.add("message");

      if (data.username === currentUser) {
        div.classList.add("me");
      } else {
        div.classList.add("other");
      }

      div.innerHTML = `
        <strong>${data.username}</strong><br>
        ${data.content}
        <span>${data.timestamp || ""}</span>
      `;

      messages.appendChild(div);
      messages.scrollTop = messages.scrollHeight;
    }
  };
}

function send() {
  const msg = document.getElementById("msg");

  if (msg.value.trim()) {
    socket.send(msg.value);
    msg.value = "";
  }
}
document.getElementById("msg").addEventListener("input", function() {
  document.getElementById("sendBtn").disabled = this.value.trim() === "";
});