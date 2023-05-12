// const form = document.getElementById("chat-form");
// const input = document.getElementById("chat-input");
// const messages = document.getElementById("chat-messages");
// const apiKey = "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";

// form.addEventListener("submit", async (e) => {
//   e.preventDefault();
//   const message = input.value;
//   input.value = "";

//   messages.innerHTML += `<div class="message user-message">
//   <img src="./icons/user.png" alt="user icon"> <span>${message}</span>
//   </div>`;

//   // Use axios library to make a POST request to the OpenAI API
//   const response = await axios.post(
//     "https://api.openai.com/v1/completions",
//     {
//       prompt: message,
//       model: "text-davinci-003",
//       temperature: 0,
//       max_tokens: 1000,
//       top_p: 1,
//       frequency_penalty: 0.0,
//       presence_penalty: 0.0,
//     },
//     {
//       headers: {
//         "Content-Type": "application/json",
//         Authorization: `Bearer ${apiKey}`,
//       },
//     }
//   );
//   const chatbotResponse = response.data.choices[0].text;

//   messages.innerHTML += `<div class="message bot-message">
//   <img src="./icons/chatbot.png" alt="bot icon"> <span>${chatbotResponse}</span>
//   </div>`;
// });


const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const messages = document.getElementById("chat-messages");
const apiKey = "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";

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value;
  input.value = "";

  messages.innerHTML += `<div class="message user-message">
  <img src="./icons/user.png" alt="user icon"> <span>${message}</span>
  </div>`;

  // Use axios library to make a POST request to the OpenAI API
  const response = await axios.post(
    "https://api.openai.com/v1/completions",
    {
      prompt: message,
      model: "text-davinci-003",
      temperature: 0,
      max_tokens: 1000,
      top_p: 1,
      frequency_penalty: 0.0,
      presence_penalty: 0.0,
    },
    {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
    }
  );
  const chatbotResponse = response.data.choices[0].text;

  messages.innerHTML += `<div class="message bot-message">
  <img src="./icons/chatbot.png" alt="bot icon"> <span>${chatbotResponse}</span>
  </div>`;
});