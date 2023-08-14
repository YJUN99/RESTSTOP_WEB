var modal = document.getElementById("loginModal");
var btn = document.getElementById("loginBtn");
var span = document.getElementsByClassName("closeBtn")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

btn.onclick = function() {
    fetch("../../loginModal.html")
        .then(response => response.text())
        .then(content => {
            modal.innerHTML = content;
            modal.style.display = "block";
            
            // closeBtn 이벤트 리스너 추가
            modal.querySelector(".closeBtn").onclick = function() {
                modal.style.display = "none";
            };
        });
}
