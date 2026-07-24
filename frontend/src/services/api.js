import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
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