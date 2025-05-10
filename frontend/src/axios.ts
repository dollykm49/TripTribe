// frontend/src/axios.ts
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api', // change if your FastAPI server is elsewhere
  withCredentials: true, // if using cookies/sessions
});

export default instance;
