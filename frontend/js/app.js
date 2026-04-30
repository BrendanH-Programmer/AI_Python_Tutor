let hintLevel = 1;

async function sendCode(reset = true) {
    const code = document.getElementById("codeInput").value;
    const responseBox = document.getElementById("responseBox");
    const tableBody = document.querySelector("#errorTable tbody");

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

        // -------------------------
        // HINT DISPLAY
        // -------------------------
        responseBox.innerText =
            "Hint Level " + hintLevel + ":\n\n" +
            (data.hint || "No hint available");

        // -------------------------
        // ERROR TABLE DISPLAY
        // -------------------------
        tableBody.innerHTML = "";

        if (data.errors && data.errors.length > 0) {

            data.errors.forEach(err => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${err.error_type || "Unknown"}</td>
                    <td>${err.priority || "-"}</td>
                    <td>${err.message || "No message"}</td>
                `;

                tableBody.appendChild(row);
            });

        } else {
            const row = document.createElement("tr");
            row.innerHTML = `<td colspan="3">No errors detected</td>`;
            tableBody.appendChild(row);
        }

    } catch (error) {
        responseBox.innerText = "Error connecting to backend.";
        console.error(error);
    }
}

function nextHint() {
    hintLevel++;

    // cap at level 3 (important for your design)
    if (hintLevel > 3) hintLevel = 3;

    sendCode(false);
}