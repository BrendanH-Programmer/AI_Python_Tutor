async function sendCode() {
    const code = document.getElementById("codeInput").value;

    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code,
            hint_level: 1
        })
    });

    const data = await response.json();

    document.getElementById("responseBox").innerText =
        JSON.stringify(data, null, 2);
}