function openPost() {
    var x = document.getElementById("postForm");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}

function openReply(a) {
    var x = document.getElementById("replyForm" + a + "");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}