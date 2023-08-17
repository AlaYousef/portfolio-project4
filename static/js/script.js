function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 4000);

  var options = {
    placement: "right", // here
    fallbackPlacements: ["bottom"],
    html: true,
    content: "test text"
  };
  $(document).ready(function () {
    new bootstrap.Popover($(".testpopover"), options)
  });