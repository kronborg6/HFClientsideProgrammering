//Login Form
function LoginForm(e) {
    document.getElementById("id01").style.display = "block";
}
//Sing up form
function SingUpForm(e) {
    document.getElementById("id02").style.display = "block";
}
//Kontak form
function KontakForm(e) {
    document.getElementById("id03").style.display = "block";
}
//Create Prudt From
function CreatePrudtFrom(e) {
    document.getElementById("id04").style.display = "block";
}

window.addEventListener("click", function(event) {
// When the user clicks on element with class="modal", close it
    console.log(event.target); // element that was clicked
    if (event.target.className === "modal") {
        event.target.style.display = "none";
    }
});

function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}