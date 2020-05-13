function openPost() {
    var x = document.getElementById("postForm");
    if (x.style.display == "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
}

function openReply(a) {
    var x = document.getElementById("replyForm" + a + "");
    if (x.style.display == "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
}