/* Allert messsages */
setTimeout(function () {
  var messages = document.getElementById("msg");
  if (messages != null) {
    var alert = new bootstrap.Alert(messages);
    alert.close();
  }

}, 3000);

/* Arrow button script */
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
