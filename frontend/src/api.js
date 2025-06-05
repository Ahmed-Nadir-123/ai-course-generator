import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',
});

export const sendChat = (message, session_id) =>
  api.post('/chat', { message, session_id });

export const getHistory = (session_id) =>
  api.get('/history', { params: { session_id } });

export const generatePPT = (course_content) =>
  api.post('/generate_ppt', { course_content });

export const generatePDF = (course_content) =>
  api.post('/generate_pdf', { course_content });

export const generateLabSheet = (course_content) =>
  api.post('/generate_lab_sheet', { course_content });

export const downloadFile = (file_id) =>
  api.get(`/download/${file_id}`, { responseType: 'blob' });

export const listFiles = () =>
  api.get('/files');

export const listCourses = () =>
  api.get('/courses');

export const getCourse = (course_id) =>
  api.get(`/course/${course_id}`);

export default api;
