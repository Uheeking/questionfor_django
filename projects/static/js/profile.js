var modal = document.getElementById("myModal");
var btn = document.getElementById("modalButton");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
  modal.style.background = "rgba(0, 0, 0, 0.8)";
  modal.styletransform = "translate(-50%, -50%)";
};

span.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
