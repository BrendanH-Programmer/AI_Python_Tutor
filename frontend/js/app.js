async function sendCode() {
    const code = document.getElementById("codeInput").value;
    const responseBox = document.getElementById("responseBox");

    responseBox.innerText = "Loading...";

    try {
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

        responseBox.innerText = JSON.stringify(data, null, 2);

    } catch (error) {
        responseBox.innerText = "Error connecting to backend.";
        console.error(error);
    }
}