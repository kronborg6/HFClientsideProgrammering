var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}
var Reg = document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === Reg) {
        Reg.style.display = "none";
    }
}

function showhid() {
  var divv = document.getElementById("gfdgdfg");
  divv.classList.toggle('hidden');
}
var div = document.getElementById('newpost');

document.getElementById('button').addEventListener('click', showhide);

function showhide() {
  div.classList.toggle('visible');
}
function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}