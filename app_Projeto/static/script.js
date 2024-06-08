$(document).ready(function() {
  // Alterna a presença ao clicar
  $(".presence").click(function() {
    var $span = $(this);
    var studentId = $span.data("aluno-id");
    var isPresent = $span.hasClass("presente");
    var presence = !isPresent;

    // Atualiza a classe e o texto de presença
    $span.toggleClass("presente", presence);
    $span.toggleClass("ausente", !presence); // Adiciona classe ausente quando não presente
    $span.text(presence ? "Presente" : "Ausente");

    // Atualiza a presença usando AJAX
    updatePresence(studentId, presence);
  });

  // Função AJAX para atualizar a presença
  function updatePresence(studentId, presence) {
    $.ajax({
      url: "/update-presence/" + studentId + "/",
      data: {
        presence: presence
      },
      dataType: 'json',
      success: function(data) {
        console.log("Presença atualizada com sucesso");
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log(xhr.responseText);
      }
    });
  }
});
