    function messagesending(e) {
      document.getElementById("id01").style.display = "block";
    }
    function refusealert(e) {
      document.getElementById("id02").style.display = "block";
    }
    function confirmalert(e) {
      document.getElementById("id03").style.display = "block";
    }
    function Test(e) {
      document.getElementById("id04").style.display = "block";
    }

    window.addEventListener("click", function(event) {
      // When the user clicks on element with class="modal", close it
      console.log(event.target); // element that was clicked
      if (event.target.className === "modal") {
        event.target.style.display = "none";
      }
    });