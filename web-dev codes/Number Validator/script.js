document.getElementById("check-btn").addEventListener("click", ()=> {
    const userInput = document.getElementById("user-input").value.trim();
    const resultsDiv = document.getElementById("results-div");

    if (!userInput) {
        alert("Please provide a phone number");
        return;
    }

    const validPattern = /^(1\s?)?(\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{4}$/;

    if (validPattern.test(userInput)) {
        resultsDiv.textContent = `Valid US number`;
        
    } else {
        resultsDiv.textContent = `Invalid US number`;
        
    }
});

document.getElementById("clear-btn").addEventListener("click", function () {
    document.getElementById("user-input").value = "";
    document.getElementById("results-div").textContent = "";
});