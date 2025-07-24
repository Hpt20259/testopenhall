import axios from 'axios';
import { Equation } from '../types';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:12000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getEquations = async (): Promise<Equation[]> => {
  const response = await api.get('/api/equations');
  return response.data;
};

export const getEquation = async (id: number): Promise<Equation> => {
  const response = await api.get(`/api/equations/${id}`);
  return response.data;
};

export const createEquation = async (equation: Omit<Equation, 'id' | 'result'>): Promise<Equation> => {
  const response = await api.post('/api/equations', equation);
  return response.data;
};

export const updateEquation = async (id: number, equation: Omit<Equation, 'id' | 'result'>): Promise<Equation> => {
  const response = await api.put(`/api/equations/${id}`, equation);
  return response.data;
};

export const deleteEquation = async (id: number): Promise<void> => {
  await api.delete(`/api/equations/${id}`);
};