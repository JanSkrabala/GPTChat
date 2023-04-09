$(document).ready(function() {
  $("#chat-form").submit(function(event) {
    event.preventDefault();
    var text = $("#text").val();
    $.post("/chat", { text: text }, function(response) {
      var chatBox = $("#chat-box");
      var chatBubble = $("<div>")
        .addClass("chat-bubble me")
        .text(text);
      chatBox.append(chatBubble);
      var chatBubble = $("<div>")
        .addClass("chat-bubble aiassist")
        .text(response);
      chatBox.append(chatBubble);
      $("#text").val("");
      chatBox.scrollTop(chatBox[0].scrollHeight);
    });
  });
});