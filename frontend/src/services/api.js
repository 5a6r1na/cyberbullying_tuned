//apis.js
import axios from "axios";

// [TODO]: Update with Gawon's LLM server
const baseURL = "http://localhost:3001/api";
const instance = axios.create({
  baseURL: baseURL,
});

export const getLLMResponse = (data) => {
  return instance.post(
    `http://localhost:5173/api/getLLMResponse`,
    // `http://localhost:8080/getLLMResponse`,
    // `${serverDomain}/getLLMResponse`,
    // `http://localhost:3000/api/chatgpt` // [TODO]: For chatgpt
    // `getLLMResponse`, // [TODO]: open when implemented
    data
  );
};
