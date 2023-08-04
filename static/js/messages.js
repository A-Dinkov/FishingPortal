
document.addEventListener("DOMContentLoaded", function() {
  const messages = document.getElementsByClassName("message");

  for (let i = 0; i < messages.length; i++) {
    const message = messages[i];
    message.style.opacity = "1";
    setTimeout(function() {
      message.style.opacity = "0";
    }, 3000);
  }

  setTimeout(function() {
    for (let i = 0; i < messages.length; i++) {
      const message = messages[i];
      message.style.display = "none";
    }
  }, 3500);
});
