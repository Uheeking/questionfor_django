$(document).ready(function () {
  function removeAlerts() {
    $(".alert-auto-dismissible")
      .fadeTo(500, 0)
      .slideUp(500, function () {
        $(this).remove(); // Remove the alert after animation completes
      });
  }

  window.setTimeout(removeAlerts, 1000);
});
