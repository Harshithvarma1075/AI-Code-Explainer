import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const analyzeCode = async (code) => {
  const response = await api.post("/chat", {
    question: code,
  });

  return response.data;
};

export default api;