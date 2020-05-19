function openPost() {
    var x = document.getElementById("postForm");
    if (x.style.display == "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
}

function openLikes(post) {
    var x = document.getElementById("likesList" + post);
    if (x.style.display == "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
}