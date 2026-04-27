let hintLevel = 1;

async function sendCode(reset = true) {
    const code = document.getElementById("codeInput").value;
    const responseBox = document.getElementById("responseBox");

    if (reset) hintLevel = 1;

    responseBox.innerText = "Loading...";

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code,
                hint_level: hintLevel
            })
        });

        const data = await response.json();

        responseBox.innerText =
            "Hint Level " + hintLevel + ":\n\n" +
            data.hint;

    } catch (error) {
        responseBox.innerText = "Error connecting to backend.";
    }
}

function nextHint() {
    hintLevel++;
    sendCode(false);
}