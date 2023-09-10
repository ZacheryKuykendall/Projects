document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("clickMe");
    const content = document.getElementById("dynamicContent");

    btn.addEventListener("click", function() {
        content.textContent = "Button was clicked!";
    });
});
