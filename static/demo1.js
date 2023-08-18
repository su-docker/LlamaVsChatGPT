const sendMessage = async (windowSelector) => {
  const loadingIndicator = document.querySelector(
    `#${windowSelector} .lds-dual-ring`
  );
  const newMessageInput = document.querySelector(
    `#${windowSelector} .chat-input`
  );
  const question = newMessageInput.value;
  appendMessage(question, true, windowSelector);
  newMessageInput.value = "";

  loadingIndicator.style.display = "block";
  const url = windowSelector == "window1" ? "/llama" : "/chatgpt";
  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify({
      question: `${question}`,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const responseText = await response.text();
  appendMessage(responseText, false, windowSelector);
  loadingIndicator.style.display = "none";
};

function appendMessage(message, isSender, windowSelector) {
  const msgWindow = document.querySelector(`#${windowSelector} .chat-body`);
  const newMessage = MessageToElement(message, isSender);
  msgWindow.appendChild(newMessage);
  msgWindow.scrollTop = msgWindow.scrollHeight;
}

function MessageToElement(message, isSender) {
  var template = document.createElement("template");
  template.innerHTML = `
  <div class="chat-message ${isSender ? "sent" : "received"}">
    <div class="chat-bubble">${message}</div>
  </div>`;
  return template.content;
}
