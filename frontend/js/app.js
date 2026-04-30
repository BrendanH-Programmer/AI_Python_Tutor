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

        const issues = data.issues || [];

        if (issues.length > 0) {

            issues.forEach(err => {
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
            row.innerHTML = `<td colspan="3">No issues detected</td>`;
            tableBody.appendChild(row);
        }

        // -------------------------
        // AI EXPLANATION (optional)
        // -------------------------
        if (data.ai_explanation) {
            const aiBox = document.createElement("div");
            aiBox.className = "ai-box";
            aiBox.innerText = data.ai_explanation;

            responseBox.innerText += "\n\n--- AI EXPLANATION ---\n\n";
            responseBox.innerText += data.ai_explanation;
        }

    } catch (error) {
        responseBox.innerText = "Error connecting to backend.";
        console.error(error);
    }
}

function nextHint() {
    hintLevel++;

    if (hintLevel > 3) hintLevel = 3;

    sendCode(false);
}