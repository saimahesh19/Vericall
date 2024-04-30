// Add your JavaScript code here
document.getElementById("pick-btn").addEventListener("click", function() {
    fetch("/pick", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message + " Audio Type: " + data.audio_type);
        } else {
            alert("Failed to pick call.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to pick call.");
    });
});

document.getElementById("hang-btn").addEventListener("click", function() {
    fetch("/hang", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
        } else {
            alert("Failed to hang call.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to hang call.");
    });
});
